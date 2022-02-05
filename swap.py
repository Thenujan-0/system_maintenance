import subprocess
from time import sleep
from PyQt5 import QtWidgets , uic, QtCore,QtGui
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPalette
import sys
import threading
import traceback
import subprocess
import os
import logging

HOME=os.getenv('HOME')
PATH= os.path.dirname(os.path.realpath(__file__))

subprocess.run([f'mkdir -p  {HOME}/.system_maintenance'],shell=True)

if __name__ == '__main__':

    subprocess.run([f'touch {HOME}/.system_maintenance/swap.log'],shell=True)

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f'{PATH}/.system_maintenance/swap.log'),
        logging.StreamHandler()
    ],
)



# QIntValidator doesnt work the way i expected it to lets create our own validator for limiting the input between 
# a range 

class HashIntValidator(QtGui.QIntValidator):
    """ warning this validator only returns acceptable 
    or invalid and just checks if the input is in range of two numbers [arg1,arg2] """
    min:int;
    max:int;
    def __init__(self,min,max):
        super(HashIntValidator, self).__init__()
        self.min=min
        self.max=max


    def validate(self,arg1,arg2):
        print(arg1,arg2)
        print(QtGui.QValidator.Acceptable)
        
        
        try:

            num = int(arg1)
            
            if num>=self.min and num<=self.max:
                return(QtGui.QValidator.Acceptable,arg1,arg2)

            else:
                return(QtGui.QValidator.Invalid,arg1,arg2)

        except:
            if arg1=='':
                return(QtGui.QValidator.Acceptable,arg1,arg2)
            else:
                return (QtGui.QValidator.Invalid, arg1,arg2)
        

        
class WorkerSignals(QtCore.QObject):
    """
    Defines the signals available from a running worker thread
    
    supported signals are
    
    finished 
        No data
        
    error 
        tupe(exectype,value,traceback.format_exc())

    result 
        object data returned from the processing , could by anything
    
    
    """
    finished =QtCore.pyqtSignal()
    error =QtCore.pyqtSignal(tuple)
    result =QtCore.pyqtSignal(object)
    

class Worker(QtCore.QRunnable):
    """
    Worker Thread
    Inherits from QRunnable to handler worker thread setup , signals and wrap up.
    
    :param callback : this function cllback to run on this worker thread supplied args
            and kwargs will be passed through the runner
            
    :type callback :function
    :param args: Arguments to pass the callbck function
    :param kwargs: Keywords to pss the callback function
    
    
    """
    
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        #store constructor arguments as they will be reused for procesing
        self.fn =fn
        self.args=args
        self.kwargs=kwargs
        self.signals=WorkerSignals()
        
    @QtCore.pyqtSlot()
    def run(self):
        """
        initialise the runner function with passed args and kwargs
        """
        
        try:
            result = self.fn(*self.args,**self.kwargs)
        
        except:
            traceback.print_exc()
            exctype,value = sys.exc_info()[:2]
            self.signals.error.emit((exctype,value,traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('swap_wid.ui',self)

        
        self.threadpool=QtCore.QThreadPool()
        

        out =subprocess.check_output(['swapon'],shell=True).decode()
        linesCount = len(out.splitlines())
        print('linesCount',linesCount)
        if linesCount>0:
            out = subprocess.check_output([f'swapon | tail -n -{linesCount-1}'],shell=True).decode()
        else:
            out=''
        lines = out.splitlines()
        for j in range(len(lines)):
            words = lines[j].split()
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)

            
            for i in range(len(words)):
                
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(words[i])
                self.tableWidget.setItem(j, i, item)
        
        
        

        header = self.tableWidget.horizontalHeader()
        header.setMinimumSectionSize(100)      
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)       
        self.btn_add_swap_partition.clicked.connect(self.btn_add_swap_partition_callback)
        self.btn_add_swapfile.clicked.connect(self.btn_add_swapfile_callback)
        self.onlyInt =QtGui.QIntValidator()
        self.ledit_swapfile_size.setValidator(self.onlyInt)



        
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.setUiElements)
        self.timer.start(1000)
        
        validator=QtGui.QIntValidator(0,100)
        validator=HashIntValidator(0,100)
        # print(validator.validate('11',1),'validaot ou')

        validator.setRange(0,100)
        self.ledit_swappiness.textChanged.connect(self.swappiness_changed)
        self.ledit_swappiness.setValidator(validator)

        #this only sets the tableWidget
        self.setUiElements()

        self.update_ui_swappiness()
    
    def update_ui_swappiness(self):
        """ sets the current swappiness value in ui """

        self.ledit_swappiness.blockSignals(True)
        swappiness= subprocess.check_output(['cat /proc/sys/vm/swappiness'],shell=True).decode()
        print(swappiness[-1],'last part of swappiness')
        swappiness=swappiness.splitlines()[0]
        if swappiness[-1]==' ':
            swappiness= swappiness[:-1]
        print('changing text in swappiness')
        self.ledit_swappiness.setText(swappiness)
        print('changed')
        self.ledit_swappiness.blockSignals(False)


    def insertInto(self,layout,index,widget):
        """ a function to insert an element into a layout in a specific position"""
        items=[]
        for i in reversed(range(layout.count(),index)):
            item =self.itemAt(i).widget()
            item.setParent(None)
            items.append(item)
            print(item,'item')
            
        print('widget',widget)
            
        layout.addWidget(widget)
        for i in reversed(range(len(items))):
            layout.addWidget(items[i])

    def swappiness_changed(self,text):
        print('swappiness changed to %s'%text)
        # subprocess.Popen([f'pkexec sysctl vm.swappiness={text}'],shell=True)
        # self.update_ui_swappiness()
        print(self.HLayout_swappiness.count())

        last_index =self.HLayout_swappiness.count()-1
        print(self.HLayout_swappiness.itemAt(last_index).widget())
        if 'QPushButton' not in str(self.HLayout_swappiness.itemAt(last_index-1).widget()):

            self.apply_swappiness= QtWidgets.QPushButton()
            self.apply_swappiness.setText('Apply swappiness')
            # 
            # self.insertInto(self.HLayout_swappiness, last_index-2, self.apply_swappiness)
            self.HLayout_swappiness.removeItem(self.HLayout_swappiness.itemAt(last_index))
            self.HLayout_swappiness.addWidget(self.apply_swappiness)

            #as the index is negative the space will be added to the end
            self.HLayout_swappiness.insertStretch(-1)

    # def systemdswap_callback(self):
        # pass
    
    def enable_systemdswap(self):
        subprocess.run(['pkexec sh -c \' systemctl enable systemd-swap.service && systemctl start systemd-swap.service\' '],shell=True)
        self.setUiElements()
    
    def disable_systemdswap(self):
        subprocess.run(['pkexec sh -c \' systemctl stop systemd-swap.service && systemctl disable systemd-swap\''],shell=True)
        self.setUiElements()
    
    def post_install(self):
        pass
    def install_enable_systemdswap(self):
        self.install_systemdswap()
        self.enable_systemdswap()
        
    def install_systemdswap(self):
        worker=Worker(self.installer)
        worker.signals.finished.connect(self.post_install)
        self.threadpool.start(worker)

    def installer(self):
        self.install_output =subprocess.check_output(['pkexec pacman -S systemd-swap --noconfirm'],shell=True)
    
    def reconnect(self,signal ,new_handler=None,old_handler=None):
        try:
            if old_handler is not None:
                while True:
                    signal.disconnect(old_handler)
            else:
                signal.disconnect()
        except TypeError:
            pass
        if new_handler is not None:
            print(signal)
            signal.connect(new_handler)
    
    def refresh_ui_background(self):
        def refresher(self):
            while True:
                sleep(1)
                self.setUiElements()
                self.signals.finished.emit
        worker = Worker(refresher)
        worker.signals.finished.connect(self.setUiElements)
        
    def setUiElements(self): 
        """Refreshes Ui elements  only refreshes swap table """




        sysd_swap= self.systemd_swap_status()
        # print(sysd_swap)
        if sysd_swap=='not installed':
            self.lbl_systemdswap_status.setText("systemd-swap is not installed")
            self.btn_systemdswap.setText('Install and enable systemd-swap')
            self.reconnect(self.btn_systemdswap.clicked,self.install_enable_systemdswap)
        elif sysd_swap=='active':
            self.lbl_systemdswap_status.setText('Systemd-swap is now active')
            self.btn_systemdswap.setText('Disable systemd-swap')
            self.reconnect(self.btn_systemdswap.clicked,self.disable_systemdswap)
            
        elif sysd_swap=='not active':
            self.lbl_systemdswap_status.setText('Systemd-swap is now disabled')
            self.btn_systemdswap.setText('Enable systemd-swap')
            self.reconnect(self.btn_systemdswap.clicked,self.enable_systemdswap)
        out =subprocess.check_output(['swapon'],shell=True).decode()
        linesCount = len(out.splitlines())
        # print('linesCount',linesCount)
        if linesCount>0:
            out = subprocess.check_output([f'swapon | tail -n -{linesCount-1}'],shell=True).decode()
        else:
            out=''
        lines = out.splitlines()
        # print(len(lines),'number of lines in  output '+f'swapon | tail -n -{linesCount-1}')


        # the problem is that it wouldnt iterate over j if len(lines)==0 in order to avoid it
        if len(lines)==0:
            self.tableWidget.setRowCount(0)            

        for j in range(len(lines)):
            words = lines[j].split()
            # print(j)
            self.tableWidget.setRowCount(j+1)

            
            for i in range(len(words)):
                
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(words[i])
                self.tableWidget.setItem(j, i, item)
    def systemd_swap_status(self):
        """returns 'active' or 'not installed' or 'not active' 
        #! todo here maybe not here but continue from here
        """
        out =subprocess.check_output(["systemctl status systemd-swap.service | head -n 3 | awk '{print $2}'"],shell=True).decode()
        if 'not-found' in out:
            return 'not installed'
        
        elif 'loaded' in out :
            if 'inactive' not in out and 'active' in out:
                return 'active'
            elif 'failed' in out or 'dead' in out or 'inactive' in out:
                return 'not active'
        elif len(out)==0:
            
            return 'not installed'

        else:
            logging.error("ERROR: couldnt find the status of systemd-swap")
        
    def btn_add_swap_partition_callback(self):
        readPartitions()
        self.partitions_ui =PartitionsUi()
        self.partitions_ui.show()        
        # self.btn_add_partition.clicked.connect(self.btn_add_callback)
    def post_create_swap_file(self):
        pass
    def btn_add_swapfile_callback(self):
        size = self.ledit_swapfile_size.text()
        size_extention=self.comboBox_swapfile_size_extention.currentText()

        print(size+size_extention)
        self.add_swap_file(size, size_extention)

    def add_swap_file(self,size,ext):
        file_name=''
        if os.path.exists('/swapfile'):
            file_name='swapfile'

        i=0
        while True:
            i+=1
            if not os.path.exists(f'/swapfile{i}'):
                file_name=f'/swapfile{i}'
                break
        if ext=='GB':
            size_in_mb=int(size)*1024

        self.progress_window=ProgressUi()
        self.progress_window.show()

        def create_swap_file():
            # process=subprocess.Popen([f'stdbuf -i0 -o0 -e0 pkexec dd if=/dev/zero of=/swapfile bs=1M count={size_in_mb} status=progress'],
            # stdout=subprocess.PIPE,
            # stderr=subprocess.STDOUT,
            # shell=True).communicate()
            cmd = f'pkexec  dd if=/dev/zero of=/swapfile bs=1M count={size_in_mb} status=progress '
            #todo for line in process.stdout update another window (which's ui hasnt yet been created by me)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True,shell=True)
            for line in p.stdout:
                sys.stdout.write(line)
                self.progress_window.update_details(line)
            p.wait()

                
                # if type(process.stdout.decode()) ==str:
                    # for line in process.stdout:
                        # print(line.decode())
                        # print('line exists')
            # for line in process.stdout:
            #     self.progress_window.update_details(line.decode())
            #     print(line,'line')
            #     sys.stdout.write(line.decode())
        worker=Worker(create_swap_file)
        worker.signals.finished.connect(self.post_create_swap_file)
        self.threadpool.start(worker)


class Device():
    name='/dev/sdX'
    partitions=[]
    
    def __init__(self,name,partitions):
        self.name = name
        self.partitions=partitions
        
    def addPartition(self,partition):
        self.partitions.append(partition)
        

class Partition():
    name:str
    size:str
    
    def __init__(self,name,size):
        self.name=name
        self.size=size


def readPartitions():
    with open ('out.txt','r') as f:
        a =f.read()
    lines= a.splitlines()
    target_lines=[]
    for line in lines:
        if line[:7] =='/dev/sd':
            print(line)
            target_lines.append(line)
            
    
    global device_list
    device_list=[]

    for line in target_lines:
        words=line.split()
        if len(device_list)==0:
            if '*' ==words[1]:
                device_list.append(Device(words[0][0:8],[Partition(words[0],words[5])]))
            else:
                device_list.append(Device(words[0][0:8],[Partition(words[0],words[4])]))
        else:
            if device_list[-1].name==words[0][0:8]:
                if '*' ==words[1]:
                    device_list[-1].addPartition(Partition(words[0][0:9],words[5]))
                else:
                    device_list[-1].addPartition(Partition(words[0][0:9],words[4]))
            else:
                device_list.append(Device(words[0],[words[0]]))

class PartitionsUi(QtWidgets.QMainWindow):
    def __init__(self):
        super( PartitionsUi,self).__init__()
        uic.loadUi('partitions.ui',self)
        self.total_partitions=0
        self.swap_available_partitions=[]


        self.btn_select.clicked.connect(self.btn_select_callback)
        self.btn_cancel.clicked.connect(self.btn_cancel_callback)
        # a variable that stores the selection status of a partition by default no partition is selected so None
        # it stores the row object of the selected partition
        self.selected = None

        # get the total memory and total swap
        out =subprocess.check_output(['free | tail -n 2 | awk \'{print $2}\''],shell=True).decode()
        out = out.splitlines()
        ram = out[0]
        ram = int(ram)

        #find the ram in giga bites
        ram_g =ram /1000000
        print(ram_g)
        suitable_for_swap_count=0
        for device in device_list:
            item0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item0.setText(0,device.name)
            # todo in temp2.py
            
            for partition in device.partitions:
                self.total_partitions+=1
                item = QtWidgets.QTreeWidgetItem(item0)
                item.setText(0,partition.name)
                item.setText(1,partition.size)
                if'G' in partition.size :
                    if float(partition.size[:-1])>8:

                        f = item.font(0)
                        f.setStrikeOut(True)
                        item.setFont(0,f)
                    
        
        if self.total_partitions < 6:
            self.treeWidget.expandAll()
            self.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) 

        
        self.treeWidget.itemClicked.connect(self.treeWidget_on_item_clicked)

    def treeWidget_on_item_clicked(self,it,col):

        # as the col argument isnt used anywhere else in the code fake arguments does get passed as col
        # to this function so be carefull

        self.selected= it
        # print(self.sender(),col,it)
        print(it.text(0))
        f = it.font(0)
        if not f.strikeOut():
            self.close()

        else:
            self.dialog_ui= DialogUi()
            self.dialog_ui.label.setText('The partition you have selected is too large. Please select another partition')
            self.dialog_ui.show()


        self.btn_select.setEnabled(True)

    def btn_select_callback(self):
        self.treeWidget_on_item_clicked(self.selected,'fake argument')


    def btn_cancel_callback(self):
        self.close()

class DialogUi(QtWidgets.QDialog):
    def __init__(self):
        super(DialogUi,self).__init__()
        print(PATH)
        uic.loadUi(f'{PATH}/dialog.ui',self)


        self.btn_ok.clicked.connect(self.btn_ok_callback)

    def btn_ok_callback(self):
        self.close()

class ProgressUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProgressUi,self).__init__()
        uic.loadUi(f'{PATH}/progress.ui',self)
        self.btn_show_details.clicked.connect(self.btn_show_details_callback)
        self.lbl_details_text=''
        self.lbl_details=None


    def btn_show_details_callback(self):
        btn =self.sender()
        if btn.text() == 'Show details':
            self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 266, 42))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.lbl_details = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.lbl_details.setObjectName("lbl_details")
            self.gridLayout_2.addWidget(self.lbl_details, 0, 0, 1, 1)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.verticalLayout.addWidget(self.scrollArea)
            self.lbl_details.setText(self.lbl_details_text)

            btn.setText('Hide details')
    def update_details(self,arg):

        text=self.lbl_details_text
        self.lbl_details_text = text+'\n'+arg

        if self.lbl_details is not None:
            self.lbl_details.setText(self.lbl_details_text)

if __name__ == "__main__":    
    app= QtWidgets.QApplication(sys.argv)
    window= Ui()
    window.show()
    app.exec_()