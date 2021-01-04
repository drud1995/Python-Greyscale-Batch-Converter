# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 03:08:37 2020

@author: drud1
"""
import os
from PIL import Image


#Takes all file names in RGB subfolder and inserts into array "arr"
arr = os.listdir("./RGB")


#Loop through array "arr"
for indexer, x in enumerate(arr):
    stringer = arr[indexer]
    
    #appends "greyscale_" to start of image to distinguish
    stringer_greyscale = "greyscale_"
    
    stringer_greyscale += stringer
    
    #Remove original file extension and make it a ".png"
    splitter = '.'
    stripped_stringer_greyscale = stringer_greyscale.split(splitter, 1)[0]
    stripped_stringer_greyscale += ".png"
    
    #Joins image path
    path = os.path.join("./RGB", stringer)
    img = Image.open(path).convert('LA') 
    
    #Save path for "img" variable
    greyscale_save = "./Greyscale/"
    greyscale_save += stripped_stringer_greyscale
    img.save(greyscale_save)
    
    #Operation complete. Close "img" variable for next loop iteration.
    img.close()




