#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:27:47 2017

@author: Nishad Mandlik
"""
from chromote import Chromote
import os
from time import sleep
from threading import Thread

def BrowSt () :
    os.system("chromium-browser -remote-debugging-port=9222")
    
def WelMes () :
    os.system('espeak "Please start your command after the beep"')


print ("Please Wait . . .")
WelcTh = Thread(target=WelMes)
WelcTh.start()

os.system("jack_control start")
os.system("sudo amixer cset numid=3 1")
pwd = os.path.dirname(os.path.abspath(__file__))

BrowTh = Thread(target=BrowSt)
BrowTh.start()
launchAttempts = 0
while (launchAttempts<20):
    try:        
        sleep(1)
        launchAttempts = launchAttempts + 1
        krom = Chromote()
    except :
        continue
    break

if (launchAttempts==20):
    WelcTh.join()
    ErrMes = "Maximum Attempts Reached. Your Browser Has Either Not Started Or Has Remote Debugging Disabled"
    print (ErrMes)
    os.system('espeak "' + ErrMes + '"')
    
TabSTT = krom.tabs[0]
TabSTT.set_url("https://mandliksg.000webhostapp.com")
WelcTh.join()
os.system("aplay " + pwd + "/Beep.wav")

