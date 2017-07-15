#!/usr/bin/python3

import os
import glob
import random
from sys import argv

global wd, length
wd = glob.glob('*.*')
File_List = []
extensions = []
thresh = 0

if '-l' in argv:
    length = int(argv[argv.index('-l') + 1])
else:
    length = 7

if '-t' in argv:
    thresh = int(argv[argv.index('-t') + 1])
else:
    thresh = 0

if '-x' in argv:
    for arg in argv[argv.index('-x')+1:]:
        if not arg[0] == '-':
            extensions.append(arg)
        else:
            break
    for f in wd:
        for ext in extensions:
            if f[-len(ext):] == ext and not f in File_List:
                File_List.append(f)
else:
    File_List = wd

def Collision_Check(hexString):
    for f in wd:
        if f[:f.index('.')] == hexString:
            return True
    return False

def randomHex():
    randHex = str(hex(random.randint(16**(length-2), (16**length)-1)))[2:]
    if len(randHex) < length:
        randHex = '0' + randHex
    return randHex

for f in File_List:
    if len(f[:f.index('.')]) >= thresh:
        randHex = randomHex()
        while Collision_Check(randHex):
            randHex = randomHex()
        print('Changed: ' + f + ' to: ' + randHex + f[f.index('.'):])
        os.rename(f, randHex + f[f.index('.'):])
