# -*- encoding=utf8 -*-
__author__ = "albam"

from airtest.core.api import *

auto_setup(__file__)
exists(Template(r"tpl1774852446070.png", record_pos=(-0.017, 0.189), resolution=(1334, 750)))
touch(Template(r"tpl1774852446070.png", record_pos=(-0.017, 0.189), resolution=(1334, 750)))
sleep(15.0)
exists(Template(r"tpl1774852579580.png", record_pos=(-0.001, 0.077), resolution=(1334, 750)))
touch(Template(r"tpl1774852594455.png", record_pos=(0.031, 0.004), resolution=(1334, 750)))
touch(Template(r"tpl1774852618025.png", record_pos=(-0.441, -0.001), resolution=(1334, 750)))
sleep(5.0)
exists(Template(r"tpl1774852755190.png", record_pos=(0.289, -0.213), resolution=(1334, 750)))

def click_sorted(template):
    positions = find_all(template)

    if positions:
        positions = sorted(positions, key=lambda p: (p["result"][0], p["result"][1]))

        for pos in positions:
            touch(pos["result"])
            sleep(0.1)

while True:

    # 1. Hijau dulu
    if exists(Template(r"tpl1774943758796.png", record_pos=(-0.174, 0.038), resolution=(1334, 750))):

        click_sorted(Template(r"tpl1774943758796.png", record_pos=(-0.174, 0.038), resolution=(1334, 750)))

    # 2. Batu setelah hijau habis
    elif exists(Template(r"tpl1774943501344.png", record_pos=(-0.082, 0.064), resolution=(1334, 750))):
        click_sorted(Template(r"tpl1774943501344.png", record_pos=(-0.082, 0.064), resolution=(1334, 750)))

    # 3. Orange terakhir
    elif exists(Template(r"tpl1774943539541.png", record_pos=(-0.088, 0.159), resolution=(1334, 750))):
        click_sorted(Template(r"tpl1774943539541.png", record_pos=(-0.088, 0.159), resolution=(1334, 750)))

    else:
        break
        
exists(Template(r"tpl1774944256787.png", record_pos=(0.001, -0.159), resolution=(1334, 750)))
touch(Template(r"tpl1774944264907.png", record_pos=(0.437, 0.217), resolution=(1334, 750)))
exists(Template(r"tpl1774944322566.png", record_pos=(-0.003, 0.21), resolution=(1334, 750)))
swipe(Template(r"tpl1774944561058.png", record_pos=(-0.001, 0.211), resolution=(1334, 750)), vector=[0.0831, -0.423])
sleep(1.0)
exists(Template(r"tpl1774944587784.png", record_pos=(-0.154, 0.209), resolution=(1334, 750)))
swipe(Template(r"tpl1774944587784.png", record_pos=(-0.154, 0.209), resolution=(1334, 750)), vector=[0.1578, -0.3688])
sleep(1.0)
exists(Template(r"tpl1774944732621.png", record_pos=(-0.104, 0.211), resolution=(1334, 750)))
swipe(Template(r"tpl1774944732621.png", record_pos=(-0.104, 0.211), resolution=(1334, 750)), vector=[0.1264, -0.5243])
sleep(1.0)
exists(Template(r"tpl1774944895653.png", record_pos=(-0.05, 0.211), resolution=(1334, 750)))
swipe(Template(r"tpl1774944895653.png", record_pos=(-0.05, 0.211), resolution=(1334, 750)), vector=[0.1995, -0.4451])
sleep(1.0)
exists(Template(r"tpl1774944973058.png", record_pos=(-0.001, 0.211), resolution=(1334, 750)))
swipe(Template(r"tpl1774944998771.png", record_pos=(-0.001, 0.212), resolution=(1334, 750)), vector=[-0.1248, -0.3859])
sleep(1.0)
exists(Template(r"tpl1774945031726.png", record_pos=(-0.033, 0.001), resolution=(1334, 750)))
touch(Template(r"tpl1774945043837.png", record_pos=(0.451, 0.229), resolution=(1334, 750)))
sleep(3.0)
touch(Template(r"tpl1774945069072.png", record_pos=(-0.441, -0.124), resolution=(1334, 750)))
exists(Template(r"tpl1774945126836.png", record_pos=(0.21, 0.006), resolution=(1334, 750)))
touch(Template(r"tpl1774945138142.png", record_pos=(-0.441, -0.032), resolution=(1334, 750)))
sleep(1.0)
touch(Template(r"tpl1774945164716.png", record_pos=(-0.443, 0.058), resolution=(1334, 750)))
sleep(1.0)
touch(Template(r"tpl1774945183931.png", record_pos=(-0.442, 0.154), resolution=(1334, 750)))
sleep(1.0)
touch(Template(r"tpl1774945207978.png", record_pos=(-0.444, -0.232), resolution=(1334, 750)))
touch(Template(r"tpl1774945207978.png", record_pos=(-0.444, -0.232), resolution=(1334, 750)))
touch(Template(r"tpl1774945251804.png", record_pos=(-0.448, -0.001), resolution=(1334, 750)))
touch(Template(r"tpl1774945278645.png", record_pos=(-0.442, 0.22), resolution=(1334, 750)))
touch(Template(r"tpl1774945303156.png", record_pos=(0.439, 0.216), resolution=(1334, 750)))
exists(Template(r"tpl1774945337850.png", record_pos=(-0.433, 0.222), resolution=(1334, 750)))
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774945375713.png", record_pos=(-0.432, 0.223), resolution=(1334, 750)))
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774945401946.png", record_pos=(-0.431, 0.223), resolution=(1334, 750)))
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774945428199.png", record_pos=(-0.431, 0.222), resolution=(1334, 750)))
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774945458802.png", record_pos=(-0.306, 0.223), resolution=(1334, 750)))
touch(Template(r"tpl1774945470755.png", record_pos=(0.437, 0.215), resolution=(1334, 750)))
sleep(3.0)
touch(Template(r"tpl1774945500419.png", record_pos=(0.448, 0.207), resolution=(1334, 750)))
exists(Template(r"tpl1774945587934.png", record_pos=(0.0, -0.22), resolution=(1334, 750)))
touch(Template(r"tpl1774946010865.png", record_pos=(-0.159, 0.199), resolution=(1334, 750)))
sleep(1.0)
text("whitesaurus")
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774946079889.png", record_pos=(-0.001, -0.235), resolution=(1334, 750)))
touch(Template(r"tpl1774946089537.png", record_pos=(0.127, 0.217), resolution=(1334, 750)))
touch(Template(r"tpl1774945351131.png", record_pos=(0.445, 0.219), resolution=(1334, 750)))
exists(Template(r"tpl1774946128637.png", record_pos=(-0.001, -0.235), resolution=(1334, 750)))
touch(Template(r"tpl1774946142765.png", record_pos=(0.077, 0.228), resolution=(1334, 750)))
touch(Template(r"tpl1774946164234.png", record_pos=(0.44, 0.229), resolution=(1334, 750)))

