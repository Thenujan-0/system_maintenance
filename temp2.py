import subprocess

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
        
        
        
        
        