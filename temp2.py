import subprocess



# assumes that
out= subprocess.check_output(['df -Th'],shell=True).decode()

print(out)
lines =out.splitlines()

#store the indexes of the lines that are suitable for swap
target_line_indexes=[]


for line in lines:
    words=line.split()

    if '/dev/' in words[0] and words[5]=='0%':
        target_line_indexes.append(lines.index(line))
    
for targ_line_ind in target_line_indexes:
    print(lines[targ_line_ind])
