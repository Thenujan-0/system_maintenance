import subprocess
from time import sleep
from PyQt5 import QtWidgets , uic, QtCore
from PyQt5.QtCore import Qt
import sys
import threading

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('swap_wid.ui',self)

        import subprocess

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
        
        
        self.setUiElements()
        
    def systemdswap_callback(self):
        pass
    
    def enable_systemdswap(self):
        pass
        #! todo here
    def install_systemdswap(self):
        subprocess.Popen(['pkexec pacman -S systemd-swap --noconfirm'],shell=True)
        
    def setUiElements(self): 
        """Refreshes Ui elements"""
        sysd_swap= self.systemd_swap_status()
        if sysd_swap=='not installed':
            self.lbl_systemdswap_status.setText("systemd-swap is not installed")
            self.btn_systemdswap.setText('Install and enable systemd-swap')
        elif sysd_swap=='active':
            self.lbl_systemdswap_status.setText('Systemd-swap is now active')
            self.btn_systemdswap.setText('Disable systemd-swap')
            
        elif sysd_swap=='not active':
            self.lbl_systemdswap_status.setText('Systemd-swap is now disabled')
            self.btn_systemdswap.setText('Enable systemd-swap')
        
        
    def systemd_swap_status(self):
        """returns 'active' or 'not installed' or 'not active' 
        #! todo here maybe not here but continue from here
        """
        out =subprocess.check_output(["systemctl status systemd-swap.service | head -n 3 | awk '{print $2}'"],shell=True).decode()
        if 'not-found' in out:
            return 'not installed'
        
        elif 'loaded' in out :
            if 'active' in out:
                return 'active'
            elif 'failed' in out:
                return 'not active'
        
        
        
    def btn_add_swap_partition_callback(self):
        readPartitions()
        self.partitions_ui =PartitionsUi()
        self.partitions_ui.show()
        
        
        # self.btn_add_partition.clicked.connect(self.btn_add_callback)
def readPartitions():
    with open ('out.txt','r') as f:
        a =f.read()
    lines= a.splitlines()
    target_lines=[]
    for line in lines:
        if line[:7] =='/dev/sd':
            print(line)
            target_lines.append(line)
            
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
        for device in device_list:
            item0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item0.setText(0,device.name)
            
            
            for partition in device.partitions:
                self.total_partitions+=1
                item = QtWidgets.QTreeWidgetItem(item0)
                item.setText(0,partition.name)
                item.setText(1,partition.size)
                
        
        if self.total_partitions < 6:
            self.treeWidget.expandAll()
            self.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) 

        
        


if __name__ == "__main__":    
    app= QtWidgets.QApplication(sys.argv)
    window= Ui()
    window.show()
    app.exec_()