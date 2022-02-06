
import re

tar ='1073741824 bytes (1.1 GB, 1.0 GiB) copied, 3.59557 s, 299 MB/s'


matches =re.search(r'\(\d*.?\d [A-Z][A-Z],',tar)
print(matches.group(0))