import subprocess
import argparse

parser = argparse.ArgumentParser(description='create a swap file and configure it')
parser.add_argument('file_name',  type=str, 
                    help='size of the swap file')


args = parser.parse_args()

file_name=args.file_name
subprocess.run([f'bash -c "swapoff \\{file_name} && rm \\{file_name}"'],shell=True)
print(f'bash -c "swapoff \\{file_name} && rm \\{file_name}"')

# remove entry from fstab
with open(f'/etc/fstab') as f:
    data=f.read()

lines=data.splitlines()

for line in lines:
    if line==f'{file_name} none swap defaults 0 0':
        data =data.replace(f'{file_name} none swap defaults 0 0','')
        break
with open(f'/etc/fstab','w') as f:
    f.write(data)