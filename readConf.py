import re
import subprocess
import os

PATH=os.path.dirname(os.path.realpath(__file__))
print(PATH)


def readJournal():
    
    file='/etc/systemd/journald.conf'
    global SystemMaxUse
    
    with open(file) as f:
        data = f.read()
        indexList=[]
        for value in re.finditer('SystemMaxUse=',data):
            indexList.append((value.start(),value.end()))
        print(indexList,'indexList')
        print(data[13])
        
        #index list now has start ,end index of SystemMaxUse=
        
        
        #if only one occurence was found
        if len(indexList)==1:
            
            if data[indexList[0][0]-1]=='#':
                SystemMaxUse=None
            else:
                stringAfterTargetLine=data[indexList[0][1]:]
                print(stringAfterTargetLine,'stringAfterTargetLine')
                #examples of stringAfterTargetLine
                #50G
                ##SystemKeepFree=
                
                
                lines=stringAfterTargetLine.split()
                if len(lines)>0:
                    regex_list= re.findall('\d+\.\d+[A-Z]|\d+[A-Z]',lines[0])
                    print(regex_list,'regex_list')
                    if len(regex_list)>1:
                        return ('looks like /etc/systemd/journald.conf is not configured correctly. Found more than one occurences of SystemMaxUse',1)
                    elif len(regex_list)==1:
                        SystemMaxUse=regex_list[0]
                        
                # SystemMaxUse=
                
    return (SystemMaxUse,0)

def setJournalConfig(replacementString):
    file='/etc/systemd/journald.conf'
    global SystemMaxUse
    
    with open(file) as f:
        data = f.read()
        indexList=[]
        for value in re.finditer('SystemMaxUse=',data):
            indexList.append((value.start(),value.end()))
        print(indexList,'indexList')
        print(data[value.start():value.end()])
        
        #index list now has start ,end index of SystemMaxUse=
        
        
        
        stringAfterTargetLine=data[indexList[0][1]:]
        
        nextNewLineChar =stringAfterTargetLine.find('\n')+ indexList[0][1]
        print(nextNewLineChar,'nextNewLineChar')
        print(data[nextNewLineChar],'data[nextNewLineChar]')
        #if only one occurence was found
        if len(indexList)==1:
            data.replace(data[indexList[0][0]:nextNewLineChar-1],replacementString)
            if data[indexList[0][0]-1]=='#':
                SystemMaxUse=None
            else:
                stringAfterTargetLine=data[indexList[0][1]:]
                print(stringAfterTargetLine,'stringAfterTargetLine')
                #examples of stringAfterTargetLine
                #50G
                ##SystemKeepFree=
                
                
                lines=stringAfterTargetLine.split()
                if len(lines)>0:
                    regex_list= re.findall('\d+\.\d+[A-Z]|\d+[A-Z]',lines[0])
                    print(regex_list,'regex_list')
                    if len(regex_list)>1:
                        return ('looks like /etc/systemd/journald.conf is not configured correctly. Found more than one occurences of SystemMaxUse',1)
                    elif len(regex_list)==1:
                        SystemMaxUse=regex_list[0]
                        
                # SystemMaxUse=
        with open(PATH+'/journaldconf.txt','w') as f:
            print('wrote it on de file')
            f.write(data)

print(readJournal())
setJournalConfig('hello')
def editJournal():
    #! edit later on final release
    file='/opt/temp.txt'
    with open('/etc/systemd/journald.conf') as f:
        data = f.read()
    
    with open(PATH+'/journaldconf.txt','w') as f:
        print('wrote it on de file')
        f.write(data)
        
    subprocess.run([f'pkexec cat  "{PATH}/journaldconf.txt" > '+file],shell=True)
    print(f'pkexec cp -f  "{PATH}/journaldconf.txt" > '+file)
        
    