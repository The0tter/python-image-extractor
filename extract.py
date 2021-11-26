#!/usr/bin/python3

"""Extract JPG data from files"""

import argparse

parser = argparse.ArgumentParser(description='Name of the file to address')

parser.add_argument('--file', dest='FileName', type=str, help='Filename containing images to process')

args = parser.parse_args()

print (args.FileName)

f=open(args.FileName,'rb')
tdata = f.read()
f.close()

#
#  The ss and se flags are set for the JFIF/JPG magic numbers.  Modify these if you are looking for a different file type.
#

ss = b'\xff\xd8'
se = b'\xff\xd9'

count = 0
start = 0
while True:
    x1 = tdata.find(ss,start)
    if x1 < 0:
        break
    x2 = tdata.find(se,x1)
    jpg = tdata[x1:x2+1]
    count += 1
    fname = f'extracted{count:03}.jpg'
    fw = open(fname,'wb')
    fw.write(jpg)
    fw.close()
    start = x2+2
