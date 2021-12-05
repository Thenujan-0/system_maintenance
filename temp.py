import subprocess
import sys
from time import sleep
sys.stdout.write('hi')
cmd = " journalctl --vacuum-size=50G"
## run it ##
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
## But do not wait till netstat finish, start displaying output immediately ##
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(str(out))
        sleep(5)
        sys.stdout.flush()