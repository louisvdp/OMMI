# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 11:54:21 2019

@author: johnstonlab

Script containing all fct in relation with arduino communication.

"""

import serial
import time
import serial.tools.list_ports as lsports

#The function (comports())returns an iterable that yields tuples of three strings:
    ## port name as it can be passed to serial.Serial or serial.serial_for_url()
    ## description in human readable form
    ## sort of hardware ID. E.g. may contain VID:PID of USB-serial adapters.
portsList = lsports.comports()

#Scan each ports to find the Teensy board (Cyclops' Arduino) and connect to it
for i in range(0,len(portsList)):
    try:
        print "Trying...",portsList[i][0]
        if 'Teensy' in portsList[i][1]:
            ser = serial.Serial(portsList[i][0], 9600)
            print 'Arduino connected'
            break
        else:
            print 'Wrong port'
            i+=1
    except:
        print "Failed to connect on",portsList[i][0]
        i+=1


for i in range(10):
    time.sleep(0.5)
    ser.write(b'H')   # send the pyte string 'H'
    time.sleep(0.5)   # wait 0.5 seconds
    ser.write(b'L')   # send the byte string 'L'
ser.close()
print 'ser closed'