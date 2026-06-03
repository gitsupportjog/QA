# -*- encoding=utf8 -*-
__author__ = "yorda"

from airtest.core.api import *
from airtest.core.settings import Settings as ST #Activate Settings
auto_setup(__file__)

ST.OPDELAY = 0 
ST.CVSTRATEGY = ["tpl", "sift"]

wait(Template(r"tpl1780450476037.png", record_pos=(-0.002, -0.147), resolution=(2436, 1125)))
touch(Template(r"tpl1780450480408.png", record_pos=(0.436, 0.173), resolution=(2436, 1125)))
sleep(10)
wait(Template(r"tpl1780450533909.png", record_pos=(-0.014, -0.178), resolution=(2436, 1125)))
touch((0.465, 0.694))
sleep(0.5)
touch((0.618, 0.68))
sleep(0.5)
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(5)
touch(Template(r"tpl1780450640620.png", record_pos=(-0.209, 0.064), resolution=(2436, 1125)))
touch(Template(r"tpl1780450652515.png", record_pos=(0.333, 0.165), resolution=(2436, 1125)))
sleep(2)
touch(Template(r"tpl1780450675396.png", record_pos=(-0.224, 0.165), resolution=(2436, 1125)))
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(2)
touch(Template(r"tpl1780450707473.png", record_pos=(-0.229, 0.169), resolution=(2436, 1125)))
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(0.5)
touch(Template(r"tpl1780450740833.png", record_pos=(-0.105, 0.165), resolution=(2436, 1125)))
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(2)
touch(Template(r"tpl1780450768029.png", record_pos=(-0.231, 0.166), resolution=(2436, 1125)))
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(2)
touch(Template(r"tpl1780450789750.png", record_pos=(-0.227, 0.167), resolution=(2436, 1125)))
touch(Template(r"tpl1780450614594.png", record_pos=(0.356, 0.15), resolution=(2436, 1125)))
sleep(1)
touch(Template(r"tpl1780450816345.png", record_pos=(0.323, 0.172), resolution=(2436, 1125)))
sleep(10)
wait(Template(r"tpl1780450847795.png", record_pos=(0.208, -0.194), resolution=(2436, 1125)))
sleep(5)
ST.SAVE_IMAGE = False
touch(Template(r"tpl1780450861197.png", record_pos=(-0.397, -0.182), resolution=(2436, 1125)))
touch(Template(r"tpl1780450861197.png", record_pos=(-0.397, -0.182), resolution=(2436, 1125)))
ST.SAVE_IMAGE = True