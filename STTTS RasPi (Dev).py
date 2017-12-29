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

pwd = os.path.dirname(os.path.abspath(__file__))

BrowTh = Thread(target=BrowSt)
BrowTh.start()
sleep(1)

krom = Chromote()
TabSTT = krom.tabs[0]
TabSTT.set_url("https://mandliksg.000webhostapp.com")
WelcTh.join()
os.system("aplay " + pwd + "/Beep.wav")

