import sys
import unittest
import os
PATH=os.path.dirname(os.path.dirname(__file__))

sys.path.append(PATH)

import swap

class BaseTest(unittest.TestCase):


    def test_shell_subprocess(self):
        with open(PATH+'/swap.py', 'r') as f:
            data=f.read()
        lines=data.splitlines()
        for line in lines:
            if 'subprocess.' in line and not 'shell=True'in line:
                self.assertEqual(f"Missing shell=True {line} ",False)




if __name__ == '__main__':
    unittest.main()