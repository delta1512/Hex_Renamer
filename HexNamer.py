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
length = 7

print(wd)

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
    if len(f[:f.index('.')]) > thresh:
        randHex = randomHex()
        print('Changed: ' + f + ' to: ' + randHex + f[f.index('.'):])
        if not Collision_Check(randHex):
            os.rename(f, randHex + f[f.index('.'):])
            pass
        else:
            while Collision_Check(randHex):
                randHex = randomHex()
            os.rename(f, randHex + f[f.index('.'):])
