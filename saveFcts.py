# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:59:59 2019

@author: Louis Vande Perre

ADD DESCRIPTION
"""
import numpy as np
from tifffile import imsave
from datetime import date
import os

date = str(date.today())
savePath="C:/data_OIIS/"+date[2:4]+date[5:7]+date[8:10]

if not os.path.exists(savePath):
    os.makedirs(savePath)

def saveImage(mmc):
      mmc.snapImage()
      img = mmc.getImage()
      imsave('test.tif', img)
      
def saveAsMultipageTifPath(datap,dirPath,namep="defaultName",datatype=None,k=1024):
    # S L O W 
    #namep = path
    dirPath=savePath
    
    try:
        if datatype == None:
            datatype=datap.dtype
    except:
        print("datatype "+str(datatype))
    #k -> number of page per tif
    
    nFrames=datap.shape[0] #.shape returns the dimensions of the array (rows, columns)
    n=0
    #datap=datap.astype('uint16')
    
    #if not os.path.exists(path+'/'+namep):
    #    os.makedirs(path+'/'+namep)​
    
    #os.path.split(path)[1]+'_' #get the name of the subfolder    ​
    for i in range(0,int(nFrames/k)):
        print("file "+str(i))
        image = datap[i*k:(i*k)+k,:,:]
        filename = dirPath+"/"+namep+'%(number)04d.tif' % {"number": i}
        imsave(filename, image.astype(datatype))
        n=i
    
        
    if (nFrames % k > 0 ):
        print("last file")
        image = datap[nFrames-(nFrames % k):nFrames] ###fixed -1]
        filename = dirPath+"/"+namep+'%(number)04d.tif' % {"number": n+1}
        imsave(filename, image.astype(datatype))                                                                                                                                                                                                                                                        
