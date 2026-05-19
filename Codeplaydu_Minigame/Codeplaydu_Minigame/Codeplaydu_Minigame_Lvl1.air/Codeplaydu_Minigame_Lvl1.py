# -*- encoding=utf8 -*-
__author__ = "albam"

from airtest.core.api import *

auto_setup(__file__)
while True:
    if exists(Template(r"tpl1775529415334.png", record_pos=(-0.235, -0.051), resolution=(1334, 750))):
        touch(Template(r"tpl1775529415334.png", record_pos=(-0.235, -0.051), resolution=(1334, 750)))
        sleep(1.0)
    else:
        break
while True:
    if exists(Template(r"tpl1775529623551.png", record_pos=(-0.185, -0.196), resolution=(1334, 750))):
        touch(Template(r"tpl1775529634160.png", record_pos=(-0.241, -0.043), resolution=(1334, 750)))
        sleep(3.0)
    else:
        break
# STAGE LEVEL 1
exists(Template(r"tpl1775529672752.png", record_pos=(-0.124, 0.159), resolution=(1334, 750)))

touch(Template(r"tpl1775529672752.png", record_pos=(-0.124, 0.159), resolution=(1334, 750)))
wait(Template(r"tpl1775529723787.png", record_pos=(-0.001, 0.123), resolution=(1334, 750)))
touch(Template(r"tpl1775529723787.png", record_pos=(-0.001, 0.123), resolution=(1334, 750)))
touch(Template(r"tpl1775529828243.png", record_pos=(0.38, 0.201), resolution=(1334, 750)))
sleep(10.0)
while True:
    hand = exists(Template(r"tpl1775535603623.png", record_pos=(0.067, 0.078), resolution=(1334, 750)))
    if hand:
        touch(hand)
        sleep(5.0)
    else:
        break
sleep(3.0)
if wait(Template(r"tpl1775035986422.png", record_pos=(0.438, 0.212), resolution=(1334, 750)), timeout=5):
    touch(Template(r"tpl1775035986422.png", record_pos=(0.438, 0.212), resolution=(1334, 750)))