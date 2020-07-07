# -*- coding: utf-8 -*-
"""
Spyder Editor

This programm searches for dcm files with a specific information in medadata
"""

import numpy as np
import imageio
import pydicom
import re
import os

"""



"""

clear = lambda: os.system('clear')

path = "/home/temuuleu/CSB_NeuroRad/1000p/DWIVOL/"

os.chdir(path)
clear()

start_dir = os.getcwd()

i = 0

for roots,dirs,files in os.walk(start_dir):
    print("searching in dir:" + roots)
    
    for name in files:
        if name.endswith('.' + "dcm"):
            
            try:
                dicom_image = pydicom.dcmread(roots +"/" +name)
            
                if (re.search("AXIS2", str(dicom_image) )):
                    print("found in : "+roots +"/" +name)
                    break;
                    
            except:
                print("DICOM couldnt load")

    # if i ==19:
    #     break
    
    # i +=1






