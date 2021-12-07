import re
import subprocess
import os

PATH=os.path.dirname(os.path.realpath(__file__))
print(PATH)


def readJournal():
    
    file='/etc/systemd/journald.conf'
    global SystemMaxUse
    #! edit later on final release
    file='/opt/temp.txt'
    
    with open(file) as f:
        data = f.read()
        indexList=[]
        for value in re.finditer('SystemMaxUse=',data):
            indexList.append((value.start(),value.end()))
        
        #index list now has start ,end index of SystemMaxUse=
        
        
        #if only one occurence was found
        if len(indexList)==1:
            
            if data[indexList[0][0]-1]=='#':
                SystemMaxUse=None
            else:
                stringAfterTargetLine=data[indexList[0][1]:]
                #examples of stringAfterTargetLine
                #50G
                ##SystemKeepFree=
                
                
                lines=stringAfterTargetLine.split()
                if len(lines)>0:
                    regex_list= re.findall('\d+\.\d+[A-Z]|\d+[A-Z]',lines[0])
                    if len(regex_list)>1:
                        return ('looks like /etc/systemd/journald.conf is not configured correctly. ',1)
                    elif len(regex_list)==1:
                        SystemMaxUse=regex_list[0]
                        
                # SystemMaxUse=
        elif len(indexList)==0:
                SystemMaxUse=None
    return (SystemMaxUse,0)

def setJournalConfig(replacementString):
    file='/etc/systemd/journald.conf'
    #! edit later on final release
    file='/opt/temp.txt'
    global SystemMaxUse
    
    with open(file) as f:
        data = f.read()
        indexList=[]
        for value in re.finditer('SystemMaxUse=',data):
            indexList.append((value.start(),value.end()))
        
        #index list now has start ,end index of SystemMaxUse=
        
        
        
        
        #if only one occurence was found
        print('index list',indexList)
        if len(indexList)==1:
            print(data[indexList[0][0]:indexList[0][1]],'part of data in index list')
            
            stringAfterTargetLine=data[indexList[0][1]:]
            print('stringAfterTargetLine')
            print(stringAfterTargetLine)
            nextNewLineChar =stringAfterTargetLine.find('\n')+ indexList[0][1]
            print('start value of data index list',data[indexList[0][0]])
            print(indexList[0][1],'index list [0][1]')
            print(stringAfterTargetLine.find('\n'))
            if data[indexList[0][0]-1]=='#':
                SystemMaxUse=None
                print('replacing '+data[indexList[0][0]-1:nextNewLineChar]+' with '+replacementString)
                
                data =data.replace(data[indexList[0][0]-1:nextNewLineChar],replacementString)
            else:
                print('replacing '+data[indexList[0][0]:nextNewLineChar]+' with '+replacementString)
                data =data.replace(data[indexList[0][0]:nextNewLineChar],replacementString)

                        
                # SystemMaxUse=
        elif len(indexList)==0:
            if data[-2:]!='\n':
                print('data[-2',data[-2],'data[-2')
                data=data+replacementString
            else:
                data=data+replacementString
            
            
    with open(PATH+'/journaldconf.txt','w') as f:
        f.write(data)

def editJournal():
    #! edit later on final release
    file='/opt/temp.txt'
    
        
    subprocess.run([f'pkexec cp -f  "{PATH}/journaldconf.txt"  '+file],shell=True)
        
    