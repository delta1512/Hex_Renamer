import os
import glob
import random
from sys import argv

global File_List
File_List_jpgs = glob.glob('*.jpg')
File_List_pngs = glob.glob('*.png')
File_List = File_List_jpgs + File_List_pngs

def Collision_Check(hexString):
    for file in File_List:
        if file[:len(file)-4] == hexString:
            return True
    return False

def Random_Hex():
    randNum = random.randint(16**6, (16**8)-1)
    randHex = str(hex(randNum))[2:]
    if randNum < 16**7:
        randHex = '0' + randHex
    if len(randHex) > 7:
        randHex = randHex[:len(randHex)-1]
    return randHex

for i, file in enumerate(File_List):
    if len(file)-4 != 7:
        randHex = Random_Hex()
        #print('Changed: ' + file + ' to: ' + randHex + file[len(file)-4:])
        if not Collision_Check(randHex):
            os.rename(File_List[i], randHex + file[len(file)-4:])
        else:
            #print('collision!')
            while Collision_Check(randHex):
                randHex = Random_Hex()
            os.rename(File_List[i], randHex + file[len(file)-4:])
