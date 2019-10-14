# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:51:18 2019

@author: Louis Vande Perre

Main file of ISOI software.
v2 - using thread to launch an acquisition.

"""

#Packages import
import sys
import MMCorePy
import cv2
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from time import time
from os import path



#Class import
from SequenceAcquisition import SequenceAcquisition
from LiveHistogram import LiveHistogram
from SignalInterrupt import SignalInterrupt 

#Function import
from histogram import histoInit, histoCalc
from crop import crop_w_mouse
from camInit import camInit, defaultCameraSettings
from saveFcts import fileSizeCalculation, cfgFileLoading
from Labjack import labjackInit, greenOn, greenOff, redOn, redOff, blueOn, blueOff, waitForSignal, trigImage
from ParsingFiles import load2DArrayFromTxt, get_immediate_subdirectories, getTifLists, splitColorChannel
#from ArduinoComm import connect, sendExposure, sendLedList, close




class isoiWindow(QtWidgets.QMainWindow):
    ### Class attributes - needed for displays information ###
    
    #trackbar
    div=100
    step=1/float(div)
    
    #Exposure (just here to keep it as global var)
    #expMin=0.0277
    expMin=5.0
    expMax=99.0
    
    #LEDs Ratio
    ledFrameNbMax=10
    ledFrameNbMin=0
    
    #File Size params
    framePerFileDefault =512
    
    #LED lit time (as a ratio of the exposure time) 
    ratioMin = 0.05
    ratioMax = 2.
    ratioDefault = 1.1
    ratioStep = 0.05
    
    #PyQt Signals definition, allows communication between different devices
    updateFramesPerFile = pyqtSignal() ##Better to use pyqtSlot ?
    settingsLoaded = pyqtSignal()
    
    #Bit depth (cam properties)
    bit= ['12-bit (high well capacity)','12-bit (low noise)',"16-bit (low noise & high well capacity)"]
    
    #Binning (cam properties)
    binn=['1x1','2x2','4x4','8x8']
    
    #Color mode in R-B acquisition
    rbColorModes = ['Red and Blue', 'Red only', 'Blue only']
    
    #LED trigger modes 
    ledTriggerModes = ['Labjack', 'Cyclops']
    
    def __init__(self, mmc, DEVICE, labjack,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.loadUi('isoi_window_V2.ui', self)
        
        ### Instance attributes ##
        self.mmc = mmc
        self.DEVICE = DEVICE
        self.labjack = labjack
        
        # Connect push buttons
        self.cropBtn.clicked.connect(self.crop)
        self.histoBtn.clicked.connect(self.oldHisto)
        self.runSaveBtn.clicked.connect(self.paramCheck)
        self.runSaveBtn.setEnabled(False)
        #self.trigBtn.clicked.connect(self.launchHisto)
        self.abortBtn.setEnabled(False)
        self.arduinoBtn.setEnabled(False)
        #self.arduinoBtn.clicked.connect(self.arduinoSync)
        self.loadBtn.clicked.connect(self.loadZyla)
        self.unloadBtn.clicked.connect(self.unloadDevices)
        self.approxFramerateBtn.clicked.connect(self.approxFramerate)
        self.testFramerateBtn.clicked.connect(self.testFramerate)
        self.loadSettingsFileBtn.clicked.connect(self.loadjsonFile)
        self.defaultSettingsBtn.clicked.connect(self.defaultSettings)
        self.savingPathBtn.clicked.connect(self.browseSavingFolder)
        
        self.loadFileBtn.clicked.connect(self.loadFolder)
        self.splitBtn.clicked.connect(self.processExperiment)
        self.splitAllBtn.clicked.connect(self.processAllExperiments)
        
        #Connect Signals
        self.updateFramesPerFile.connect(self.fileSizeSetting)
        
        ###### ComboBoxes ######
        
        #Binning selection
        self.binBox.addItem(isoiWindow.binn[0])
        self.binBox.addItem(isoiWindow.binn[1])
        self.binBox.addItem(isoiWindow.binn[2])
        self.binBox.addItem(isoiWindow.binn[3])
        self.binBox.setCurrentText(self.mmc.getProperty(self.DEVICE[0], 'Binning'))
        self.binBox.currentTextChanged.connect(self.binChange)
        
        #Bit depth selection
        self.bitBox.addItem(isoiWindow.bit[0])
        self.bitBox.addItem(isoiWindow.bit[1])
        self.bitBox.addItem(isoiWindow.bit[2])
        self.bitBox.setCurrentText(self.mmc.getProperty(self.DEVICE[0], 'Sensitivity/DynamicRange'))
        self.bitBox.currentTextChanged.connect(self.bitChange)
        
        #Shutter mode selection
        self.shutBox.addItem("Rolling")
        self.shutBox.addItem("Global")
        self.shutBox.setCurrentText(self.mmc.getProperty(self.DEVICE[0], 'ElectronicShutteringMode'))
        self.shutBox.currentTextChanged.connect(self.shutChange)
        
        #Trigger mode selection
        self.triggerBox.addItem('Internal (Recommended for fast acquisitions)')
        #self.triggerBox.addItem('Software (Recommended for Live Mode)')
        #self.triggerBox.addItem('External Start')
        #self.triggerBox.addItem('External Exposure')
        self.triggerBox.addItem('External')
        self.triggerBox.setCurrentText(self.mmc.getProperty(self.DEVICE[0], 'TriggerMode'))
        self.triggerBox.currentTextChanged.connect(self.triggerChange)
        
        #Overlap Mode
        self.overlapBox.addItem('On')
        self.overlapBox.addItem('Off')
        self.overlapBox.setCurrentText(self.mmc.getProperty(self.DEVICE[0], 'Overlap'))
        self.overlapBox.currentTextChanged.connect(self.overlapChange)

        
        #LEDs trigger mode selection
        self.ledTrigBox.addItem(isoiWindow.ledTriggerModes[1])
        self.ledTrigBox.addItem(isoiWindow.ledTriggerModes[0])
        self.ledTrigBox.setCurrentText(isoiWindow.ledTriggerModes[0])
        self.ledTrigBox.currentTextChanged.connect(self.ledTrigChange)
        
        #Color mode of rb alternance box
        self.rbColorBox.addItem(isoiWindow.rbColorModes[0])
        self.rbColorBox.addItem(isoiWindow.rbColorModes[1])
        self.rbColorBox.addItem(isoiWindow.rbColorModes[2])
        self.rbColorBox.setCurrentText(isoiWindow.rbColorModes[0])
        
        ####### Slider #####
        self.expSlider.setMinimum(isoiWindow.expMin)
        self.expSlider.setMaximum(isoiWindow.expMax)
        self.expSlider.setValue(self.mmc.getExposure())  
        self.expSlider.valueChanged.connect(self.exposureChange)
        self.expSlider.setSingleStep(isoiWindow.step*10) ##doesn't affect anything 
        
        #### Spinboxes ###
        
        #EXPOSURE
        self.C_expSb.setMaximum(isoiWindow.expMax)
        self.C_expSb.setMinimum(isoiWindow.expMin)
        self.C_expSb.setValue(self.mmc.getExposure())
        self.C_expSb.valueChanged.connect(self.exposureChange)
        self.C_expSb.setSingleStep(isoiWindow.step)
        
        #Experiment duration
        self.experimentDuration.setSingleStep(float(isoiWindow.step))
        self.experimentDuration.setMaximum(1000)
        
        #LEDs ratios
        self.gRatio.setMinimum(isoiWindow.ledFrameNbMin)
        self.rRatio.setMinimum(isoiWindow.ledFrameNbMin)
        self.bRatio.setMinimum(isoiWindow.ledFrameNbMin)
        self.gRatio.setMaximum(isoiWindow.ledFrameNbMax)
        self.rRatio.setMaximum(isoiWindow.ledFrameNbMax)
        self.bRatio.setMaximum(isoiWindow.ledFrameNbMax)
        
        #File size
        self.framePerFileBox.setValue(isoiWindow.framePerFileDefault)
        self.framePerFileBox.valueChanged.connect(self.updateFramesPerFile.emit)
      
        #Interval Ms
        self.expRatio.setValue(isoiWindow.ratioDefault)
        self.expRatio.setMaximum(isoiWindow.ratioMax)
        self.expRatio.setSingleStep(isoiWindow.ratioStep)
        self.expRatio.setMinimum(isoiWindow.ratioMin)
        
        #####
        
        #Name text area
        self.experimentName.insert("DefaultName")
        
        #Initialize frames per files text label
        self.fileSizeSetting()
        
        #Initialize exposure label
        self.realExp.setText(str(self.mmc.getExposure()))
        
        #Initialize framerate label
        self.approxFramerate()
        
        #ProgressBar
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        
        #LEDs toggle buttons
        self.Green.stateChanged.connect(self.green)
        self.Red.stateChanged.connect(self.red)
        self.Blue.stateChanged.connect(self.blue)
        
        #Led sequence mode toogle buttons
        self.rgbMode.stateChanged.connect(self.ledSequenceModeCheck)
        self.rbMode.stateChanged.connect(self.ledSequenceModeCheck)
    
    
            

        
    
    
    #################################
    #### Camera settings methods ####
    #################################
    
    ###Button related###
    #Organized like the GUI panel
    
    def exposureChange(self, expVal):
        """
        Change the exposure in the camera settings and update the GUI 
        with the real exposure.
        """
        #exp=expVal/float(div)
        self.C_expSb.setValue(expVal) #update spinbox value
        self.expSlider.setValue(expVal) #update slider value
        print 'exposure wanted : ', expVal
        try:
            self.mmc.setExposure(DEVICE[0], expVal)
            self.realExp.setText(str(self.mmc.getExposure()))
        except:
            print "CMM err, no possibility to set exposure"
    
    def approxFramerate(self):
        """
        This function approximate the framerate. Approximation based on Zyla
        specifications mentioned in the hardware user guide.
        """
        print('Approximation of the framerate')
        ##### From Hardware User Guide #####
        ### settings > Global Shutter and external/software triggering,
        ### Sensor Readout Rate = 560MHz 
        row =  9.24E-6      #(s)
        fullFrame= 9.98E-3  #(s)
        interFrame= 9*row
        startDelay= 2*row
        #Overlap Off :
            #CycleTime = exposure + 1 Frame + 1 interframe + 5 rows
        #Overlap On :
            #CycleTime =  exposure dependant (look at documentation)
        
        if self.binBox.currentText() == '4x4':
            fullFrameNbPix = 640*540 #Binning4x4
        elif self.binBox.currentText() == '1x1':
            fullFrameNbPix = 2560*2160 #Binning1x1
        elif self.binBox.currentText() == '2x2':
            fullFrameNbPix = 1280*1080 #Binning2x2
        elif self.binBox.currentText() == '8x8':
            fullFrameNbPix = 320*270 #Binning1x1
            
        exposure = float(self.realExp.text())*1E-3 #conversion in s
        print('exposure : ',exposure)
        ROI = self.mmc.getROI()
        print('ROI : ',ROI)
        nbPix = ROI[-1]*ROI[-2] #(horizontal nb of pix) * (vertical nb of pix), last objects of ROI list
        
        print('nbPix : ',nbPix)
        frameRatio = float(nbPix)/fullFrameNbPix #One must be float to have a float div
        print('frameRatio : ',frameRatio)
        
        #Cycle time calculation
        #Note that it doesn't take the LED triggering by the labjack in count
        cycleTime = exposure + fullFrame*frameRatio+interFrame+5*row+startDelay
        print('cycleTime : ',cycleTime)
        self.approxFramerateLabel.setText(str(round(1/cycleTime,2)))
        
    def testFramerate(self):
        """
        This function test the framerate. Fire an image using the external 
        trigger and mesure the cycle time.
        """
        cycleTime = None
        previousTriggerMode = self.mmc.getProperty(self.DEVICE[0], 'TriggerMode')
        triggerMode = 'External'
        print('test of the framerate')
        self.triggerChange(triggerMode)
        if self.triggerModeCheck(triggerMode):
            self.mmc.startContinuousSequenceAcquisition(1)
            print('acquisition start')
            waitForSignal(self.labjack, "TTL", "AIN", 0)
            start = time()
            #One acquisition begin
            trigImage(self.labjack)
            waitForSignal(self.labjack, "TTL", "AIN", 0)
            #When the ARM signal back in high state, acquisition is done
            end = time()
            self.mmc.stopSequenceAcquisition()
            cycleTime = end-start
            print(cycleTime)
            self.testFramerateLabel.setText(str(round(1/cycleTime,2)))
        self.triggerChange(previousTriggerMode)
        return cycleTime
    
    
    def binChange(self, binn):
        """
        Change the Binning in the camera settings and update the GUI.
        """
        try:
            self.mmc.setProperty(self.DEVICE[0], 'Binning', str(binn))
            realBinning = self.mmc.getProperty(self.DEVICE[0],'Binning')
            self.binBox.setCurrentText(realBinning) #Ensure that the change are effective
                                                    #and update the GUI
        except:
            print 'CMM err, no possibility to set Binning'

    def bitChange(self, bit):
        """
        Change the Sensitivity/DynamicRange in the camera settings and update the GUI.
        """
        try:
            self.mmc.setProperty(self.DEVICE[0], 'Sensitivity/DynamicRange', str(bit))
            actualBitDepth = self.mmc.getProperty(self.DEVICE[0],'Sensitivity/DynamicRange')
            self.bitBox.setCurrentText(actualBitDepth)
        except:
            print 'CMM err, no possibility to set Sensitivity/DynamicRange'
            
    def shutChange(self,shutterMode):
        """
        Change the ElectronicShutteringMode in the camera settings and update the GUI.
        """
        try:
            self.mmc.setProperty(self.DEVICE[0],'ElectronicShutteringMode',str(shutterMode))
            actualShutterMode = self.mmc.getProperty(self.DEVICE[0], 'ElectronicShutteringMode')
            self.shutBox.setCurrentText(actualShutterMode)
        except:
            print 'CMM err, no possibility to set ElectronicShutteringMode'
        
    def triggerChange(self, triggerMode):
        """
        Change the TriggerMode in the camera settings and update the GUI.
        """
        try:
            self.mmc.setProperty(self.DEVICE[0],'TriggerMode',str(triggerMode))
            actualTriggerMode = self.mmc.getProperty(self.DEVICE[0], 'TriggerMode')
            self.triggerBox.setCurrentText(actualTriggerMode)
        except:
            print 'CMM err, no possibility to set TriggerMode'

    def overlapChange(self, overlap):
        """
        Change the TriggerMode in the camera settings and update the GUI.
        """
        try:
            self.mmc.setProperty(self.DEVICE[0],'Overlap', str(overlap))
            actualOverlap = self.mmc.getProperty(self.DEVICE[0], 'Overlap')
            self.overlapBox.setCurrentText(actualOverlap)
        except:
            print "CMM err, no possibility to set Overlap mode"
            
    def loadZyla(self):
        """
        Load a device on the MMC API.
        The device loaded will be used to acquire images.
        """
        try:
            self.DEVICE = camInit(self.mmc)
            print 'Device ',self.DEVICE[0],' loaded'
        except:
            print 'CMM error : fail to load device'
    
    def unloadDevices(self):
        """
        Unload all devices from the MMC API > closing communication.
        """
        try:
            self.mmc.unloadAllDevices()
            print 'all devices UNLOADED'
        except:
            print 'CMM error : fail to unload all devices'
    
    
    ###LED ligtening###
    def green(self,toggle_g):
        """
        Turn on or off the green LED in function of the QCheckBox state.
        """
        if toggle_g:
            greenOn(self.labjack)
        else :
            greenOff(self.labjack)
          
    def red(self,toggle_r):
        """
        Turn on or off the red LED in function of the QCheckBox state.
        """
        if toggle_r:
            redOn(self.labjack)
        else :
            redOff(self.labjack)    
            
    def blue(self,toggle_b):
        """
        Turn on or off the blue LED in function of the QCheckBox state.
        """
        if toggle_b:
            blueOn(self.labjack)
        else :
            blueOff(self.labjack)
    
    ### CROP CAMERA IMAGE ###
    def crop(self):
        """
        Set the ROI of the camera.
        If a ROI is mouse drawn on the screen > this ROI is selected.
        Else the ROI is reset() to the default one. 
        """
        triggerMode = 'Internal (Recommended for fast acquisitions)'
        if self.triggerModeCheck(triggerMode):
            self.mmc.clearROI()
            self.mmc.snapImage()
            img = self.mmc.getImage()
            (x,y,w,h) = crop_w_mouse(img,self.mmc.getROI())
            self.mmc.setROI(x,y,w,h)
            print "image width: "+str(self.mmc.getImageWidth())
            print "image height: "+str(self.mmc.getImageHeight())
            cv2.destroyAllWindows()
            self.updateFramesPerFile.emit()
    
    ### LOADING EXPERIMENT SETTINGS ###    
    
    def defaultSettings(self):
        """
        Reset the camera and acquisition settings.
        """
        print 'default settings loading'
        
        # Reset Camera Settings 
        defaultCameraSettings(self)
        # Reset Acquisition Settings #TO DO ?

    
    def loadjsonFile(self):
        """
        Use QFileDialog to display a window and ask for a file to load with
        a filter on .json file.
        """
            
        selectedFile = QFileDialog.getOpenFileName(self, 'Open configuration file', filter=('JSON configuration file (*.json)'))
        #FileName contains the file name and the filter so we select only first component
        fileName=selectedFile[0]
        if path.isfile(fileName):
            self.loadSettings(fileName)
        else:
            print('No file selected')
        
    
    def loadSettings(self, settingsPath):
        """
        Load the CFG file, update all the experiment settings with infos from the file.
        """
        print 'Loading : ',settingsPath
        #POP UP window to avoid none path calling
        cfgDict = cfgFileLoading(settingsPath)
        
        ### Load camera settings ###
        try:
            camSettingsDict = cfgDict['Camera settings']
            ROI = camSettingsDict["ROI"]
            self.mmc.setROI(ROI[0],ROI[1],ROI[2],ROI[3])
            self.exposureChange(camSettingsDict["Exposure"])
            self.binChange(camSettingsDict["Binning"])
            self.bitChange(camSettingsDict["Bit depth"])
            self.shutChange(camSettingsDict["Shutter mode"])
            self.triggerChange(camSettingsDict["Trigger mode"])
            self.overlapChange(camSettingsDict["Overlap mode"])
        except:
            print 'Camera settings dictionary is not accessible'
            
        ### Load acquisiton settings
        try:
            acqSettings = cfgDict["Acquisition settings"]
            self.expRatio.setValue(acqSettings['LED illumination time (% of exposure)'])
            self.ledTrigBox.setCurrentText(acqSettings['LED trigger mode'])
            ledSequenceMode = acqSettings['LED switching mode']
            if ledSequenceMode == "rgbMode":
                self.rgbMode.setChecked(True)
                self.rbMode.setChecked(False)
                self.rRatio.setValue(acqSettings["(RGB) LED ratio"][0])
                self.gRatio.setValue(acqSettings["(RGB) LED ratio"][1])
                self.bRatio.setValue(acqSettings["(RGB) LED ratio"][2])
            elif ledSequenceMode == "rbMode":
                self.rgbMode.setChecked(False)
                self.rbMode.setChecked(True)
                self.gInterval.setValue(acqSettings["(RB) Green frames interval"])
                self.rbColorBox.setCurrentText(acqSettings["(RB) Color(s)"])
        except:
            print 'Acquisition settings dictionary is not accessible'
        try:
            self.experimentDuration.setValue(cfgDict['Global informations']['Duration'])
        except:
            print 'Global informations are not accessible'
            
        self.settingsLoaded.emit()
    
    ### Msg display ###
    def triggerModeCheck(self, triggerMode):
        """
        Check if the camera trigger mode is set to the triggerMode argument.
        Pop-up window is generated if the wrong trigger mode is set on.
        """
        print triggerMode
        if self.mmc.getProperty(self.DEVICE[0], 'TriggerMode') != triggerMode:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Set the trigger mode to : \n" + triggerMode)
            msg.setWindowTitle("Trigger mode warning")
            msg.exec_()
            return False
        else:
            return True
        
    
    ######################################
    #### Acquisition settings methods ####
    ######################################
    
    def ledTrigChange(self):
        """
        Handle a change in the LED trigger mode.
        """
        #Only Labjack mode for the moment so not implemented for the moment.
        print 'm'
    
    def ledSequenceModeCheck(self):
        """
        Check wich LED sequence mode is selected and enable the good buttons.
        Return the mode selected
        """
        mode = None
        if self.rgbMode.isChecked() and self.rbMode.isChecked() :
            self.runSaveBtn.setEnabled(False)
        elif self.rgbMode.isChecked():
            self.runSaveBtn.setEnabled(True)
            mode ="rgbMode"
        elif self.rbMode.isChecked():
            self.runSaveBtn.setEnabled(True)
            mode ="rbMode"
        else:
            self.runSaveBtn.setEnabled(False)
        return mode
    
    def fileSizeSetting(self):
        """
        Calculate the size of each .tif file in function of the number of frames
        per file wanted.
        """
        framePerFile = self.framePerFileBox.value()
        #sizeMax = self.fileSize.value()
        ROI = self.mmc.getROI()
        bitDepth = self.bitBox.currentText()
        if bitDepth == isoiWindow.bit[2]:
            bitPPix = 16 #Nb of bits per pixel
        else:
            bitPPix = 12
        
        sizeMax = fileSizeCalculation(framePerFile, ROI, bitPPix)
        self.sizePerFileLabel.setText(str(sizeMax))
    
    ### SAVING FOLDER CHOICE ###
    
    def browseSavingFolder(self):
        """
        Use QFileDialog to display a window and ask for a folder selection.
        """
        
        folderName = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        if path.isdir(folderName):
            self.savingPath.clear()
            self.savingPath.insert(folderName)
        else:
            print('No folder selected')

    
    ######################################
    #### Sequence acquisition section ####
    ######################################
    
    def paramCheck(self):
        """ 
        Check that the user is well informed about certains acquisition settings before launching the acquisition
        """
        run = True
        
        #Shutter mode check
        if mmc.getProperty(DEVICE[0], 'ElectronicShutteringMode')== 'Rolling':
            choice = QMessageBox.question(self, 'Shutter Mode',
                                                "Running acquisition in Rolling mode ?",
                                                QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                print("Running in Rolling mode")
                run = True
            else:
                print('Change mode in the other panel')
                run = False
                
                
        #Trigger mode check
        if run and (self.ledTrigBox.currentText() == 'Labjack'):
            if (self.triggerModeCheck('External')):
                run = True
            else:
                run = False
        if run and (self.ledTrigBox.currentText() == 'Cyclops'):
            if(self.triggerModeCheck('Internal (Recommended for fast acquisitions)')):
                run = True
            else:
                run = False
        if run:
            self.saveImageSeq()
            
    def saveImageSeq(self):
        """
        Get all informations from the GUI needed for setting up an acquisition.
        Then instanciate an object from the SequenceAcquisition class, and this
        object will handle the actual sequence acquisition.
        """
        
        #Get experiment/acquisition settings from the GUI
        name = self.experimentName.text() #str
        duration = self.experimentDuration.value() # float (seconds)
        cycleTime = (self.testFramerate()) # int (seconds)
        rgbLedRatio = [self.rRatio.value(),self.gRatio.value(),self.bRatio.value()] #list of int
        maxFrames =  self.framePerFileBox.value() #int
        expRatio = self.expRatio.value() #int
        rbGreenRatio = self.gInterval.value() #int
        savingPath = self.savingPath.text() #str
        colorMode = self.rbColorBox.currentText() #str
        triggerStart = self.startTriggerBox.isChecked()
        triggerStop = self.stopTriggerBox.isChecked()
        
         
        #Creation of a SequenceAcquisition class instance
        self.sequencAcq = SequenceAcquisition(name, 
                                         duration,
                                         cycleTime,
                                         rgbLedRatio,
                                         rbGreenRatio,
                                         maxFrames,
                                         expRatio,
                                         savingPath,
                                         colorMode,
                                         self.mmc,
                                         self.labjack)
        print 'object initialized'
        self.sequencAcq.isFinished.connect(self.acquisitionDone)
        self.sequencAcq.nbFramesSig.connect(self.initProgressBar)
        self.sequencAcq.progressSig.connect(self.updateProgressBar)
        self.sequencAcq.acquMode = self.ledTrigBox.currentText() #TO DO : set all the parameters like this
        if self.rgbMode.isChecked():
            self.sequencAcq.seqMode = "rgbMode"
        elif self.rbMode.isChecked():
            self.sequencAcq.seqMode = "rbMode"
        
        
        # At this point we want to allow user to stop/terminate the thread
        # so we enable that button
        self.abortBtn.setEnabled(True)
        # And we connect the click of that button to the built in
        # terminate method that all QThread instances have
        self.abortBtn.clicked.connect(self.sequencAcq.abort)
        
        if triggerStop:
            #--> reading an while looping for the image acquisition
            # input and when the signal goes high
            interruptAIN = 1
            stopSignalState = False
            waitToCheckSignal = 0.5
            
            stopTriggerMsg = QMessageBox()
            stopTriggerMsg.setIcon(QMessageBox.Warning)
            stopTriggerMsg.setText("Low SYNC signal detected")
            stopTriggerMsg.setWindowTitle("Aborted acquisition")
            
            #Instanciate a SignalInterrupt object to listen to the labjack and detect interrupt
            self.stopInterrupt = SignalInterrupt(self.labjack, interruptAIN, waitToCheckSignal, stopSignalState)
            self.stopInterrupt.stateReachedInterrupt.connect(self.sequencAcq.abort)
            self.stopInterrupt.stateReachedInterrupt.connect(stopTriggerMsg.exec_)
            self.abortBtn.clicked.connect(self.sequencAcq.abort)
            self.sequencAcq.isFinished.connect(self.stopInterrupt.abort)
            self.abortBtn.clicked.connect(self.stopInterrupt.abort)
            self.stopInterrupt.start()
        
        # We don't want to enable user to start another thread while this one is
        # running so we disable the start button.
        self.runSaveBtn.setEnabled(False)
        if not triggerStart:
            # We have all the events we need connected we can start the thread 
            self.sequencAcq.start()
        else:
            interruptAIN = 1
            startSignalState = True
            waitToCheckSignal = 0.5
            
            startTriggerMsg = QMessageBox()
            startTriggerMsg.setIcon(QMessageBox.Warning)
            startTriggerMsg.setText("Labjack is ready to receive external signal")
            startTriggerMsg.setWindowTitle("Waiting for a SYNC signal")
            
            #Instanciate a SignalInterrupt object to listen to the labjack and detect interrupt
            self.startInterrupt = SignalInterrupt(self.labjack, interruptAIN, waitToCheckSignal, startSignalState)
            self.startInterrupt.stateReachedInterrupt.connect(self.sequencAcq.start)
            try:
                self.startInterrupt.stateReachedInterrupt.connect(startTriggerMsg.close)
            except:
                print ' no way to connect close fct'
            self.sequencAcq.isStarted.connect(self.startInterrupt.abort)
            self.startInterrupt.start() # start listening to the signal
            startTriggerMsg.exec_() #Pop window to prevent listenning to trigger
    
    ##### Methods in charge of communication with SequenceAcquisition class instance ####
    def initProgressBar(self,nbFrames):
        """
        Initialize the progress bar in function of the nb of frames of the acquisition.
        """
        self.progressBar.setMaximum(nbFrames)
        
    def updateProgressBar(self,imageCount):
        """
        Update progress bar in function of the acquisition progress.
        """
        self.progressBar.setValue(imageCount+1)
    
    def acquisitionDone(self):
        """
        Udpate the GUI when an acquisition is finished.
        """
        #Reset progressBar
        self.progressBar.reset()
        #Change button state
        self.abortBtn.setEnabled(False)
        self.runSaveBtn.setEnabled(True)
        
        
    #########################################
    #### Histogram using QThread section ####
    #########################################
    
    def launchHisto(self):
        try:
            self.liveHistogram = LiveHistogram(self.mmc, self.labjack)
            # Connections between LED settings button and histogram
            self.liveHistogram.modeChoice.connect(self.askHistoMode)
            self.liveHistogram.finished.connect(self.histoDone)
            
            self.liveHistogram.start()  
        except:
            print 'cannot instanciate the LiveHistogram class'
            
    def oldHisto(self):
        """
        Function that calculate and display a histogram.
        """
        triggerMode = 'Internal (Recommended for fast acquisitions)'
        if self.triggerModeCheck(triggerMode):
            (mask, h_h, h_w, pixMaxVal, bin_width, nbins) = histoInit(mmc)
            cv2.namedWindow('Histogram', cv2.CV_WINDOW_AUTOSIZE)
            cv2.namedWindow('Video')
            self.mmc.snapImage()
            g = self.mmc.getImage() #Initialize g
            self.mmc.startContinuousSequenceAcquisition(1)
            while True:
                    if self.mmc.getRemainingImageCount() > 0:
                        g = self.mmc.getLastImage()
                        rgb2 = cv2.cvtColor(g.astype("uint16"),cv2.COLOR_GRAY2RGB)
                        rgb2[g>(pixMaxVal-2)]=mask[g>(pixMaxVal-2)]*256 #It cannot be compared to pixMaxVal because it will never reach this value
                        cv2.imshow('Video', rgb2)
                            
                    else:
                        print('No frame')
                        
                    h = histoCalc(nbins, pixMaxVal, bin_width, h_h, h_w, g)
                    cv2.imshow('Histogram',h)
                    
                    if cv2.waitKey(33) == 27:
                        break
                    if cv2.getWindowProperty('Video', 1) == -1: #Condition verified when 'X' (close) button is pressed
                        break
                    elif cv2.getWindowProperty('Histogram', 1) == -1: #Condition verified when 'X' (close) button is pressed
                        break
    
            cv2.destroyAllWindows()
            self.mmc.stopSequenceAcquisition()
                
    ### Methods in charge of communication with LiveHisto class instance
    def askHistoMode(self):
        print 'popup window to ask mode'
        
        #Selection between blinking or continous mode histogram
        
        #Change in toggle boxes connection
        self.reconnect(self.Green.stateChanged, self.setBlinkingLED) #Disconnect green led from green function
        self.reconnect(self.Red.stateChanged, self.setBlinkingLED) #Disconnect green led from green function
        self.reconnect(self.Blue.stateChanged, self.setBlinkingLED) #Disconnect green led from green function
        
    
    def setBlinkingLED(self):
        print 'setBlinkingLED called'
        if self.Green.isChecked() and not self.Red.isChecked() and not self.Blue.isChecked():
            self.liveHistogram.led = 'g'
            print 'green LED blinking mode'
        elif self.Red.isChecked() and not self.Blue.isChecked() and not self.Green.isChecked():
            self.liveHistogram.led = 'r'
            print 'red LED blinking mode'
        elif self.Blue.isChecked() and not self.Red.isChecked() and not self.Green.isChecked():
            self.liveHistogram.led = 'b'
            print 'blue LED blinking mode'
        elif not self.Blue.isChecked() and not self.Red.isChecked() and not self.Green.isChecked():
            print 'black histogram'
        else:
            print 'Turn on only one LED before lauching histogram'
        #self.liveHistogram.blinkingLedMode()
        #launch blinking LED mode of the histogram
        self.liveHistogram.blinkingLedMode()
        
    def histoDone(self):
        print 'Histo done'
        #Change in toggle boxes connection
        self.reconnect(self.Green.stateChanged, self.green) #Disconnect green led from green function
        self.reconnect(self.Red.stateChanged, self.red) #Disconnect green led from green function
        self.reconnect(self.Blue.stateChanged, self.blue) #Disconnect green led from green function
        
    #######################    
    #### Analysis part ####
    #######################
        
    def loadFolder(self):
        """
        Load a folder containing experiments.
        """    
        folderName = str(QFileDialog.getExistingDirectory(self, "Select a valid experiment folder"))
        if path.isdir(folderName):
            self.folderName.setText(folderName)
            self.analysisPath = folderName
            subDirectories = get_immediate_subdirectories(self.analysisPath)
            self.subDirList.clear()
            self.subDirList.addItems(subDirectories)
        else:
            print('No folder selected')
        

    def processExperiment(self):
        """
        Get the experiment folder name from the gui and call the split fction.
        Called when split channels button is pressed.
        """
        experimentFolder = self.subDirList.currentItem() 
        if experimentFolder :
            print 'item well selected'
            experimentFolderName = experimentFolder.text()
            self.splitChannels(experimentFolderName)
        else:
            print 'Please, select a valid experiment folder' #TO DO : add window
    
    def processAllExperiments(self):
        """
        Get all the experiment names and call slit fct for each one
        """
        try:
            experimentsList = []
            for index in xrange(self.subDirList.count()):
                experimentsList.append(self.subDirList.item(index))
        except:
            print('cannot call this protected function')
        try:
            for experiment in experimentsList:
                experimentFolderName = experiment.text()
                self.splitChannels(experimentFolderName)
        except:
            print('Empty list of experiments')
    
    
    def splitChannels(self, experimentFolderName):
        """
        Concatenate all the .tif to segment them in blue, red and green channels.
        Create new .txt files for each channels containing the timestamps.
        """
        print'split channel fct'
        
        #If method called witout argument, trie
        print experimentFolderName
#        if not experimentFolderName : #experimentFolderName = False or None will enter the statement
#            experimentFolder = self.subDirList.currentItem() 
#            print 'item well selected'
#            experimentFolderName = experimentFolder.text()
#            print str(experimentFolderName)
        #if experimentFolderName : #experimentFolderName = something will enter this statement
        print self.analysisPath
        print str(experimentFolderName)
        experimentFolderPath = self.analysisPath+'/'+experimentFolderName
        print experimentFolderPath
        filePath =self.analysisPath+'/'+experimentFolderName+'/'+experimentFolderName
        print filePath
        txtFile=filePath+'.txt'
        try:
            txtArray = load2DArrayFromTxt(txtFile,"\t")
        except:
            print 'error to convert txt to array'
        try:
            tifsPathList = getTifLists(experimentFolderPath)
            print tifsPathList
        except:
            print 'error to convert txt to array'
        try:
            splitColorChannel(experimentFolderPath, txtArray, tifsPathList)
        except:
            print 'error to split channels'   
            
            
#        else:
#            print 'Please, select a valid experiment folder'

    
    
    #################################
    #### Common utility function ####
    #################################
    
    def reconnect(self, signal, newhandler=None, oldhandler=None):
        """
        Deconnect a signal and reconnect it to another handler function.
        Source : https://stackoverflow.com/questions/21586643/pyqt-widget-connect-and-disconnect
        """
        while True:
            try:
                if oldhandler is not None:
                    signal.disconnect(oldhandler)
                else:
                    signal.disconnect()
                print 'disconnection OK'
            except TypeError:
                break
        if newhandler is not None:
            signal.connect(newhandler)
            print 'new connection ok'
    
    def closeEvent(self, event):
        """
        Executed when close button of the main window is clicked.
        Ask for closing and close properly the program.
        """
        # Close all before closing the main window
        closingChoice = QMessageBox.question(self, 
                                             'Close Confirmation',
                                             "Exit ?",
                                             QMessageBox.Yes | QMessageBox.No)
        
        if closingChoice == QMessageBox.Yes: # UNLOAD DEVICES before closing the program
            try:
                self.sequencAcq.abort()
                time.sleep(2) #Ensure all is well closed
            except:
                print('No sequenceAcqu running or impossible to abort it')
            self.unloadDevices()
            event.accept() # let the window close
        else:
            event.ignore()


##Launching everything
if __name__ == '__main__':
    
    """MicroManager Init"""
    mmc = MMCorePy.CMMCore()
    
    """Camera Init"""
    DEVICE = camInit(mmc) # TO FIX, give DEVICE at some function only
    
    """Labjack init"""
    labjack = labjackInit()
    #Launch GUI
    app = QtWidgets.QApplication(sys.argv)
    window = isoiWindow(mmc, DEVICE, labjack)
    window.show()
    sys.exit(app.exec_())