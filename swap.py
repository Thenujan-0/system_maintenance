import subprocess
from time import sleep
from PyQt5 import QtWidgets , uic, QtCore,QtGui
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPalette

import sys
import threading
import traceback
import subprocess


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
    
#! todo here define Worker class

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
            exctype,value = sys.exe_info()[:2]
            self.signals.error.emit((exctype,value,traceback.format_exc()))
        else:
            self.signls.result.emit(result)
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
        
        self.setUiElements()
    
    def systemdswap_callback(self):
        pass
    
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
        """Refreshes Ui elements"""
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
            print("ERROR: couldnt find the status of systemd-swap")
        
    def btn_add_swap_partition_callback(self):
        readPartitions()
        self.partitions_ui =PartitionsUi()
        self.partitions_ui.show()        
        # self.btn_add_partition.clicked.connect(self.btn_add_callback)

    def btn_add_swapfile_callback(self):
        size = self.ledit_swapfile_size.text()
        size_extention=self.comboBox_swapfile_size_extention.currentText()

        print(size+size_extention)
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
        out =subprocess.check_output(['free | tail -n 2 | awk \'{print $2}\''],shell=True).decode()
        print(out)
        out = out.splitlines()
        ram = out[0]
        ram = int(ram)
        ram_g =ram /1000000
        print(ram_g)
        for device in device_list:
            item0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item0.setText(0,device.name)
            
            
            for partition in device.partitions:
                self.total_partitions+=1
                item = QtWidgets.QTreeWidgetItem(item0)
                item.setText(0,partition.name)
                item.setText(1,partition.size)
                if'G' in partition.size :
                    if float(partition.size[:-1])>8:
                        # brush =QtGui.QBrush(QtGui.qRed(0))
                        # item.setStyleSheet("color:red")
                        # item.setForeground(0,brush)
                        # item.setTextColor(QtGui.QRed())
                        # QPalette().color(QPalette.Window)
                        # item.setForeground(0,QPalette().color(QPalette.Highlight))
                        # item.setText(0,item.text(0)+'(too big)')
                        f = item.font(0)
                        f.setStrikeOut(True)
                        item.setFont(0,f)

        
        if self.total_partitions < 6:
            self.treeWidget.expandAll()
            self.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) 

        
        self.treeWidget.itemClicked.connect(self.treeWidget_on_item_clicked)

    def treeWidget_on_item_clicked(self,it,col):
        # print(self.sender(),col,it)
        print(it.text(0))
        if '(too big)' not in it.text(0):
            self.close()


if __name__ == "__main__":    
    app= QtWidgets.QApplication(sys.argv)
    window= Ui()
    window.show()
    app.exec_()