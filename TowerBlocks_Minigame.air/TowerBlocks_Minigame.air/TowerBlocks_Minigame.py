# -*- encoding=utf8 -*-
__author__ = "albam"

from airtest.core.api import *

auto_setup(__file__)
exists(Template(r"tpl1775458107838.png", record_pos=(0.19, -0.054), resolution=(1334, 750)))
touch(Template(r"tpl1775458107838.png", record_pos=(0.19, -0.054), resolution=(1334, 750)))
sleep(5.0)
while True:
    if exists(Template(r"tpl1775460867468.png", target_pos=8, record_pos=(-0.454, -0.13), resolution=(1334, 750))):
        touch(Template(r"tpl1775460867468.png", target_pos=8, record_pos=(-0.454, -0.13), resolution=(1334, 750)), duration=1)
        swipe(Template(r"tpl1775460867468.png", target_pos=8, record_pos=(-0.454, -0.13), resolution=(1334, 750)), vector=[0.4664, -0.1668], duration=1.5)
        sleep(0.5)
    else:
        break
exists(Template(r"tpl1775461071152.png", record_pos=(0.435, -0.004), resolution=(1334, 750)))
touch(Template(r"tpl1775461071152.png", record_pos=(0.435, -0.004), resolution=(1334, 750)))
while True:
    if exists(Template(r"tpl1775036028985.png", record_pos=(0.059, 0.072), resolution=(1334, 750)))
        touch(Template(r"tpl1775036028985.png", record_pos=(0.059, 0.072), resolution=(1334, 750)))
        sleep(1.0)
        touch(Template(r"tpl1775036028985.png", record_pos=(0.059, 0.072), resolution=(1334, 750)))
        sleep(1.0)
    else:
        break
touch(Template(r"tpl1775035986422.png", record_pos=(0.438, 0.212), resolution=(1334, 750)))