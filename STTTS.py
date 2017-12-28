#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:27:47 2017

@author: Nishad Mandlik
"""

print ("Please Wait")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
import pyttsx

TTS = pyttsx.init()
pwd = os.path.dirname(__file__)

chrOpts = webdriver.ChromeOptions()
chrOpts.add_argument("--use-fake-ui-for-media-stream")

fireProf = webdriver.FirefoxProfile(pwd + "/Firefox Profile")

#driver = webdriver.Firefox(firefox_profile = fireProf, executable_path = pwd + '/geckodriver')
driver = webdriver.Chrome(executable_path = pwd + '/chromedriver', chrome_options = chrOpts)

driver.get("https://mandliksg.000webhostapp.com")

while (driver.title != "Recording") :
    sleep(1)

print ("Recording")
while (driver.title != "Done") :
    sleep(1)
    
print ("Done")
  
STT = driver.find_element_by_id("confm").text
driver.close()

TTS.say(STT)
TTS.runAndWait()




