import subprocess
from  time import sleep
import argparse
import os
import sys
import re
import math
from elevate import elevate
""" This is file is supposed to be executed as root
    THis file was created with an intention of avoiding so many pkexec usage when creating and configuring a swap file
    swap.py has to make the changes to the GUI by the output of this process
 """


def is_root():
    return os.getuid() == 0

parser = argparse.ArgumentParser(description='create a swap file and configure it')
parser.add_argument('size',  type=int, 
                    help='size of the swap file')
parser.add_argument('ext',type=str,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
# print(args.size,args.ext)

if is_root():
    print('Im root')

size=args.size
ext=args.ext 
if ext not in ['GB','TB']:
    raise Exception("Invalid swap file extension")

elevate()
# print('done ')
def create_swap_file_name():
    file_name=''
    if not os.path.exists('/swapfile'):
        file_name='/swapfile'
    else:
        i=0
        while True:
            i+=1
            if not os.path.exists(f'/swapfile{i}'):
                file_name=f'/swapfile{i}'
                break
    
    print(file_name,'file_name for swap')
    return file_name


global caught_authotization_error
caught_authotization_error=False

def create_swap_file(size,ext,file_name):

    if ext=='GB':
        size_in_mb=int(size)*1024
    elif ext=='TB':
        size_in_mb=int(size)*1024*1024
    else:
        logger.error('Error:Unrecognized extension when creating swap file')

    cmd = f'dd if=/dev/zero of={file_name} bs=1M count={size_in_mb} status=progress '
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True,shell=True)
    
    caught_authotization_error = False
    
    for line in p.stdout:
        
        #check if user didnt finish polkit authorization
        if 'Error executing command as another user: Not authorized' in line:
            # global caught_authotization_error
            caught_authotization_error=True
            print('Caught authorization error')
            break


        sys.stdout.write(line)
        sys.stdout.flush()
        patern=r'\d*.?\d [A-Z][a-z][A-Z]'
        matches =re.search(patern,line)
        if matches is not None:
            copied=matches.group(0)
            # print(copied,'copied')
            ext_patern=r'[A-Z][a-z][A-Z]'
            size_patern=r'\d+.?\d'
            ext_match=re.search(ext_patern,copied)
            size_match=re.search(size_patern,copied)
            if ext_match and size_match:
                # print(size_match.group(0),'size match',ext_match.group(0),'ext match')
                copied_size=size_match.group(0)
                copied_ext=ext_match.group(0)

                #dont know how it works but when i try to create a 3GB swap file it ends up creating 3GiB swap file So..
                if copied_ext.replace('i','')== ext:
                    percentage = math.floor(100 * (float(copied_size)/float(size)))
                    print(f'creating swap file completed {percentage}%')
        
    p.wait()

    post_create_swap_file(file_name)

def post_create_swap_file(file_name):

    #catch user authentication error
    if not caught_authotization_error:

        # print('created swap file')
        # print(file_name,'file_name of swap')
        filename=file_name
        def set_swap_file():
            subprocess.run([f'pkexec sh -c "chmod 600 {filename} && mkswap {filename} && swapon {filename}"'],shell=True)
            # print('executed the following line')
            # print(f'sh -c "chmod 600 {filename} && mkswap {filename} && swapon {filename}"')

        def post_set_swap_file(file_name):
            print('finished setting up swap file')


            #edit /etc/fstab

            with open('/etc/fstab') as f:
                data = f.read()
            
            lines =data.splitlines()
            already_configured=False
            for line in lines:
                if line ==f'{file_name} none swap defaults 0 0':
                    already_configured=True
                    break

            if not already_configured:
                print('fstab not already configured')
                subprocess.run([f'bash -c "echo {file_name} none swap defaults 0 0 >> /etc/fstab"'],shell=True)
                print('finished editing /etc/fstab')

        set_swap_file()
        post_set_swap_file(file_name)


    else:
        print('caught authentication error')




            
create_swap_file(size,ext,create_swap_file_name())
