import subprocess

with open ('out.txt','r') as f:
    a =f.read()
lines= a.splitlines()
for line in lines:
    if line[:7] =='/dev/sd':
        print(line)