# -*- encoding=utf8 -*-
__author__ = "remote"

from airtest.core.api import *

auto_setup(__file__)
start_app("com.ferrero.applayduGP")
sleep(45.0)
touch((0.06, 0.676))
sleep(2.0)
touch(Template(r"tpl1769483781610.png", record_pos=(-0.101, -0.038), resolution=(2960, 1440)))
sleep(6)
for i in range(25):
    touch((0.422, 0.659))
    sleep(2)
    for i in range(3):
        swipe((0.22, 0.386), (0.4, 0.402), duration=1, steps=1)
        sleep(1)
    for i in range(3):
        swipe((0.4, 0.402),(0.22, 0.386), duration=1, steps=1)
        sleep(1)