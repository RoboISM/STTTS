#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:27:47 2017

@author: Nishad Mandlik
"""

print ("Please Wait")
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import os
from time import sleep

pwd = os.path.dirname(os.path.abspath(__file__))

chrOpts = webdriver.ChromeOptions()
chrOpts.add_argument("--use-fake-ui-for-media-stream")

os.system("jack_control start")
os.system("sudo amixer cset numid=3 1")

os.system('espeak "Please start speaking after the beep"')

fireProf = webdriver.FirefoxProfile(pwd + "/Firefox Profile")

driver = webdriver.Chrome(executable_path = pwd + "/chromedriver", chrome_options = chrOpts)
#driver = webdriver.Firefox(firefox_profile = fireProf, firefox_binary = '/usr/bin/firefox', executable_path = pwd + '/geckodriver')

driver.get("https://mandliksg.000webhostapp.com")

while (driver.title != "Recording") :
    sleep(1)
    
os.system("aplay " + pwd + "/Beep.wav")

print ("Recording")
while (driver.title != "Done") :
    sleep(1)
    
print ("Done")
  
STT = driver.find_element_by_id("confm").text
print (STT)
driver.close()

os.system('espeak "' + STT + '"')


