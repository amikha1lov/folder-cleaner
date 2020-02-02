#!/usr/bin/python3
import sys, os
import shutil

if len(sys.argv) <= 1 or not os.path.isdir(sys.argv[1]):
    mypath = '/mnt/files/photos/'
else:
    if sys.argv[1].endswith('/'):
        mypath = sys.argv[1]
    else:
        mypath = sys.argv[1] + '/'
    

for (dirpath, dirnames, filenames) in os.walk(mypath):
    for f in filenames:
        filedate = f[4:12]
        correct_path = mypath + filedate
        abs_filename = mypath + f
        if os.path.isdir(correct_path):
            shutil.move(abs_filename, correct_path)
        else:
            os.mkdir(correct_path)
            shutil.move(abs_filename, correct_path)
    break

