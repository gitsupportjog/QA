# -*- encoding=utf8 -*-
__author__ = "yordan.ridhanto"

import random
from airtest.core.api import *
from airtest.core.settings import Settings as ST #Activate Settings
auto_setup(__file__)

stop_app("com.ferrero.applaydudev2")
start_app("com.ferrero.applaydudev2")

#Please remove if the app was not installed from TF
touch((0.849, 0.452)) 
sleep(1)
touch((0.847, 0.502))
#----

sleep(12) #For Intro
wait(Template(r"tpl1780371576791.png", record_pos=(0.249, -0.175), resolution=(2436, 1125)))
touch(Template(r"tpl1780371590878.png", record_pos=(0.104, 0.102), resolution=(2436, 1125)))
sleep(1)
touch((0.649, 0.392)) #add year
sleep(0.5)
for i in range(3): #add year on repeat 3 times
    touch((0.83, 0.715))
    sleep(0.1)
sleep(3)
touch((0.27, 0.88))
sleep(3)
touch((0.43, 0.88))
sleep(3)
touch((0.918, 0.88))
touch(Template(r"tpl1780371869293.png", record_pos=(0.25, 0.179), resolution=(2436, 1125)))
touch((0.73, 0.576))
text("Strawbelly Pancake")
touch(Template(r"tpl1780371966046.png", record_pos=(0.412, 0.174), resolution=(2436, 1125)))
touch(Template(r"tpl1780371986272.png", record_pos=(0.318, -0.014), resolution=(2436, 1125)))
sleep(1)
touch((0.505, 0.512))
sleep(4)
touch(Template(r"tpl1780372072041.png", record_pos=(-0.394, -0.192), resolution=(2436, 1125)))
sleep(3)
touch(Template(r"tpl1780372093539.png", record_pos=(0.082, 0.073), resolution=(2436, 1125)))
sleep(15)
touch(Template(r"tpl1780372160723.png", record_pos=(-0.395, -0.188), resolution=(2436, 1125)))
sleep(6)
touch(Template(r"tpl1780372192822.png", record_pos=(0.456, -0.192), resolution=(2436, 1125)))
for i in range(6): #Scrolling menu
    swipe((0.481, 0.89), (0.481, 0.212))
    sleep(2)
#Entering Dino FTUE
touch((0.516, 0.588))
touch(Template(r"tpl1780385374833.png", record_pos=(0.147, -0.103), resolution=(2436, 1125)))
sleep(5)
using("Dino_FTUE_Lite.air")
import Dino_FTUE_Lite
sleep(1)
swipe((0.481, 0.89), (0.481, 0.212))
touch((0.516, 0.588))
touch(Template(r"tpl1780389794189.png", record_pos=(0.141, -0.098), resolution=(2436, 1125)))
sleep(5)
using("LS_FTUE_Lite.air")
import LS_FTUE_Lite
sleep(2)