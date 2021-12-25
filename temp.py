import subprocess

out =subprocess.check_output(['swapon'],shell=True).decode()

linesCount = len(out.splitlines())
print('linesCount',linesCount)

out = subprocess.check_output([f'swapon | tail -n -{linesCount}'],shell=True).decode()
print(out)
lines = out.splitlines()
for line in lines:
    words = line.split()
    for i in range(len(words)):
        
        
