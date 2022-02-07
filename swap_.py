import subprocess
from  time import sleep
import argparse

parser = argparse.ArgumentParser(description='create a swap file and configure it')
parser.add_argument('file-size', metavar='-s', type=int, 
                    help='size of the swap file')
parser.add_argument('ext',metavar='-e',type=str,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.file-size)


""" This is file is supposed to be executed as root
    THis file was created with an intention of avoiding so many pkexec usage when creating and configuring a swap file
    swap.py has to make the changes to the GUI by the output of this process
 """


def post_create_swap_file(file_name,result):

    #catch user authentication error
    if not caught_authotization_error:

        print('result is ',result)
        pro_win=progress_window
        lbl_status=pro_win.lbl_status
        print('created swap file')
        filename=file_name
        pro_win.update_details_text('setting the created file as swap file')
        def set_swap_file():
            subprocess.Popen([f'pkexec sh -c "chmod 600 {filename} && mkswap {filename} && swapon {filename}"'],shell=True)

        def post_set_swap_file(file_name,result):
            print('result is',result)
            print('finished setting up swap file')
            pro_win.update_details_text('Finished setting up swap file')
            main_process_running=False


            #edit /etc/fstab

            with open('/etc/fstab') as f:
                data = f.read()
            
            lines =data.splitlines()
            already_configured=False
            for line in lines:
                if line =='echo /swapfile none swap defaults 0 0':
                    already_configured=True
                    break

            if not already_configured:
                print('not already configured')
                subprocess.Popen(['pkexec bash -c "echo /swapfile none swap defaults 0 0 >> /etc/fstab"'],shell=True)



        worker=Worker(set_swap_file)
        worker.signals.result.connect(partial(post_set_swap_file,file_name))
        threadpool.start(worker)

    else:
        progress_window.close()
        #a variable used to tract if some main process (worker thread )is running 
        # as we use variables to tract if processes exited sucessfully
        main_process_running=False



def add_swap_file(size,ext):
    file_name=''
    if not os.path.exists('/swapfile'):
        file_name='swapfile'
    else:
        i=0
        while True:
            i+=1
            if not os.path.exists(f'/swapfile{i}'):
                file_name=f'/swapfile{i}'
                break
    
    print(file_name,'file_name for swap')
    progress_window=ProgressUi()
    progress_window.show()

    def create_swap_file(size,ext,file_name):
        # process=subprocess.Popen([f'stdbuf -i0 -o0 -e0 pkexec dd if=/dev/zero of=/swapfile bs=1M count={size_in_mb} status=progress'],
        # stdout=subprocess.PIPE,
        # stderr=subprocess.STDOUT,
        # shell=True).communicate()
        progress_window.lbl_status.setText('Creating swap file')
        if ext=='GB':
            size_in_mb=int(size)*1024
        elif ext=='TB':
            size_in_mb=int(size)*1024*1024
        else:
            logger.error('Error:Unrecognized extension when creating swap file')

        cmd = f'pkexec  dd if=/dev/zero of={file_name} bs=1M count={size_in_mb} status=progress '
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True,shell=True)
        
        caught_authotization_error = False
        
        for line in p.stdout:
            
            #check if user didnt finish polkit authorization
            if 'Error executing command as another user: Not authorized' in line:
                caught_authotization_error=True
                break


            sys.stdout.write(line)
            progress_window.update_details_text(line)
            patern=r'\d*.?\d [A-Z][a-z][A-Z]'
            matches =re.search(patern,line)
            if matches is not None:
                copied=matches.group(0)
                print(copied,'copied')
                ext_patern=r'[A-Z][a-z][A-Z]'
                size_patern=r'\d+.?\d'
                ext_match=re.search(ext_patern,copied)
                size_match=re.search(size_patern,copied)
                if ext_match and size_match:
                    print(size_match.group(0),'size match',ext_match.group(0),'ext match')
                    copied_size=size_match.group(0)
                    copied_ext=ext_match.group(0)

                    #dont know how it works but when i try to create a 3GB swap file it ends up creating 3GiB swap file So..
                    if copied_ext.replace('i','')== ext:
                        percentage = math.floor(100 * (float(copied_size)/float(size)))
                        progress_window.progressBar.setValue(percentage)
        p.wait()

            
            # if type(process.stdout.decode()) ==str:
                # for line in process.stdout:
                    # print(line.decode())
                    # print('line exists')
        # for line in process.stdout:
        #     progress_window.update_details_text(line.decode())
        #     print(line,'line')
        #     sys.stdout.write(line.decode())
    worker=Worker(create_swap_file,file_name=file_name,ext=ext,size=size)
    worker.signals.result.connect(partial(post_create_swap_file,file_name))
    threadpool.start(worker)
