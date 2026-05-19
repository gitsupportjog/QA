# -*- encoding=utf8 -*-
__author__ = "yorda"

from airtest.core.api import *
from airtest.core.settings import Settings as ST #Activate Settings
auto_setup(__file__)

ST.OPDELAY = 0 
ST.CVSTRATEGY = ["tpl", "sift"]

stop_app("com.ferrero.applayduGP")
clear_app("com.ferrero.applayduGP")
start_app("com.ferrero.applayduGP")

sleep(10) #Intro

wait(Template(r"tpl1769407892437.png", record_pos=(-0.001, -0.115), resolution=(2340, 1080)))
touch(Template(r"tpl1769407896917.png", record_pos=(0.406, 0.174), resolution=(2340, 1080)))
touch(Template(r"tpl1769407908053.png", record_pos=(-0.215, -0.049), resolution=(2340, 1080)))
touch(Template(r"tpl1769407918122.png", record_pos=(0.41, 0.175), resolution=(2340, 1080)))
touch(Template(r"tpl1769407926098.png", record_pos=(-0.388, 0.187), resolution=(2340, 1080)))
sleep(4)
touch(Template(r"tpl1769407943506.png", record_pos=(0.463, 0.194), resolution=(2340, 1080)))
touch((0.476, 0.884))
text("Labian")
touch(Template(r"tpl1769408056293.png", record_pos=(0.418, 0.174), resolution=(2340, 1080)))
wait(Template(r"tpl1769408088736.png", record_pos=(-0.082, -0.159), resolution=(2340, 1080)))
touch(Template(r"tpl1769408104031.png", record_pos=(-0.103, -0.044), resolution=(2340, 1080)))
sleep(1.0)
touch(Template(r"tpl1769408122394.png", record_pos=(0.094, 0.014), resolution=(2340, 1080)))
sleep(2.0)
swipe((0.547, 0.911), (0.547, 0.050))
swipe((0.547, 0.911), (0.547, 0.050))
sleep(6)
touch(Template(r"tpl1769393945385.png", record_pos=(-0.406, -0.174), resolution=(2340, 1080)))
touch(Template(r"tpl1769393961347.png", record_pos=(-0.054, 0.131), resolution=(2340, 1080)))
touch(Template(r"tpl1769398692607.png", record_pos=(-0.235, 0.132), resolution=(2340, 1080)))
sleep(4)
wait(Template(r"tpl1769408299362.png", record_pos=(-0.221, 0.001), resolution=(2340, 1080)))
touch(Template(r"tpl1769408315588.png", record_pos=(0.117, 0.035), resolution=(2340, 1080)))
sleep(1)
touch(Template(r"tpl1769409308589.png", record_pos=(-0.425, 0.005), resolution=(2340, 1080)))
sleep(3)
wait(Template(r"tpl1769399205522.png", record_pos=(-0.311, -0.113), resolution=(2340, 1080)))

ST.SAVE_IMAGE = False
#Fungsi Swipe Dino
horizontal_y = [0.217, 0.3, 0.378]
vertical_x = [0.285, 0.354, 0.429, 0.495, 0.571, 0.639, 0.711]

for i in range(9):
    if i >= 6:
        if exists(Template(r"tpl1769403064377.png")):
            break
    # horizontal swipes
    for y in horizontal_y:
        swipe((0.285, y), (0.711, y), duration=0.1)
        swipe((0.711, y), (0.285, y), duration=0.1)

    # vertical swipes
    for x in vertical_x:
        swipe((x, 0.248), (x, 0.989), duration=0.1)
        swipe((x, 0.989), (x, 0.248), duration=0.1)

ST.SAVE_IMAGE = True
wait(Template(r"tpl1769404229432.png", record_pos=(0.021, -0.131), resolution=(2340, 1080)))
touch(Template(r"tpl1769404237888.png", record_pos=(0.447, 0.175), resolution=(2340, 1080)))
wait(Template(r"tpl1769404266582.png", record_pos=(-0.329, -0.015), resolution=(2340, 1080)))
swipe((0.499, 0.867), (0.542, 0.556), duration=1)
sleep(3)
swipe((0.535, 0.867), (0.627, 0.426), duration=1)
sleep(3)
swipe((0.581, 0.884), (0.412, 0.499), duration=1)
sleep(3)
swipe((0.54, 0.875), (0.494, 0.443), duration=1)
sleep(3)
swipe((0.499, 0.887), (0.472, 0.583), duration=1)
sleep(4)
touch(Template(r"tpl1769416158120.png", record_pos=(0.458, 0.189), resolution=(2340, 1080)))
wait(Template(r"tpl1769416189682.png", record_pos=(-0.2, -0.083), resolution=(2340, 1080)))
touch(Template(r"tpl1769416201226.png", record_pos=(-0.409, -0.104), resolution=(2340, 1080)))
sleep(1)
touch(Template(r"tpl1769416248428.png", record_pos=(-0.406, -0.028), resolution=(2340, 1080)))
touch(Template(r"tpl1769416280775.png", record_pos=(0.318, -0.015), resolution=(2340, 1080)))
touch(Template(r"tpl1769416280775.png", record_pos=(0.318, -0.015), resolution=(2340, 1080)))
touch(Template(r"tpl1769416351519.png", record_pos=(-0.252, -0.013), resolution=(2340, 1080)))
touch(Template(r"tpl1769416359897.png", record_pos=(-0.414, 0.048), resolution=(2340, 1080)))
touch(Template(r"tpl1769416384491.png", record_pos=(0.096, 0.135), resolution=(2340, 1080)))
touch(Template(r"tpl1769416390872.png", record_pos=(0.029, 0.137), resolution=(2340, 1080)))
touch(Template(r"tpl1769416397852.png", record_pos=(-0.409, 0.124), resolution=(2340, 1080)))
touch(Template(r"tpl1769416430949.png", record_pos=(0.098, 0.136), resolution=(2340, 1080)))
touch(Template(r"tpl1769416436774.png", record_pos=(0.033, 0.139), resolution=(2340, 1080)))
touch(Template(r"tpl1769416448284.png", record_pos=(-0.416, -0.192), resolution=(2340, 1080)))
touch(Template(r"tpl1769416477301.png", record_pos=(-0.414, -0.192), resolution=(2340, 1080)))
wait(Template(r"tpl1769416501610.png", record_pos=(-0.215, -0.045), resolution=(2340, 1080)))
touch(Template(r"tpl1769416507478.png", record_pos=(-0.419, -0.003), resolution=(2340, 1080)))
touch(Template(r"tpl1769416588803.png", record_pos=(-0.411, 0.185), resolution=(2340, 1080)))
touch(Template(r"tpl1769416611730.png", record_pos=(0.447, 0.18), resolution=(2340, 1080)))
touch(Template(r"tpl1769416638660.png", record_pos=(0.231, 0.183), resolution=(2340, 1080)))
touch(Template(r"tpl1769416645678.png", record_pos=(0.455, 0.176), resolution=(2340, 1080)))
touch(Template(r"tpl1769416672481.png", record_pos=(0.122, 0.183), resolution=(2340, 1080)))
touch(Template(r"tpl1769416680215.png", record_pos=(0.455, 0.175), resolution=(2340, 1080)))
touch(Template(r"tpl1769416702571.png", record_pos=(0.122, 0.185), resolution=(2340, 1080)))
touch(Template(r"tpl1769416708769.png", record_pos=(0.454, 0.174), resolution=(2340, 1080)))
touch(Template(r"tpl1769416728450.png", record_pos=(0.455, 0.176), resolution=(2340, 1080)))
touch(Template(r"tpl1769416744619.png", record_pos=(0.443, 0.18), resolution=(2340, 1080)))
wait(Template(r"tpl1769416773837.png", record_pos=(-0.411, 0.07), resolution=(2340, 1080)))
touch(Template(r"tpl1769416783284.png", record_pos=(0.457, 0.167), resolution=(2340, 1080)))
touch((0.523, 0.858))
text("Bubura")
touch(Template(r"tpl1769416835749.png", record_pos=(0.444, 0.169), resolution=(2340, 1080)))
touch((0.457, 0.904))
sleep(1)
touch((0.523, 0.896))
touch(Template(r"tpl1769416947916.png", record_pos=(0.453, 0.187), resolution=(2340, 1080)))
sleep(1)
touch(Template(r"tpl1769416965822.png", record_pos=(0.449, 0.188), resolution=(2340, 1080)))
