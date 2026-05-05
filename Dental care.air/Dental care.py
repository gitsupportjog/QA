# -*- encoding=utf8 -*-
__author__ = "Remote"

from airtest.core.api import *

auto_setup(__file__)
game_package = "com.ferrero.applayduGP"
start_app(game_package)
sleep(15)
wait(Template(r"tpl1773798519177.png", record_pos=(-0.448, -0.176), resolution=(2340, 1080)))
touch((123, 740))
wait(Template(r"tpl1774852870604.png", record_pos=(0.101, -0.043), resolution=(2340, 1080)))
touch(Template(r"tpl1774852898003.png", record_pos=(0.101, -0.042), resolution=(2340, 1080)))
sleep(10.0)
wait(Template(r"tpl1774853922966.png", record_pos=(-0.004, 0.04), resolution=(2340, 1080)))
swipe((943, 592),(687, 592), duration=5)
wait(Template(r"tpl1774854115737.png", record_pos=(0.313, 0.126), resolution=(2340, 1080)))

left   = 1412
right  = 1022

top    = 675
middle = 775
bottom = 859

# fungsi sikat 1 garis
def brush_line(y):
    swipe((left, y), (right, y), duration=0.4)
    swipe((right, y), (left, y), duration=0.4)

# ulangi beberapa kali
for i in range(12):
    brush_line(top)
    brush_line(middle)
    brush_line(bottom)

print("Sikat seluruh area selesai")

wait(Template(r"tpl1774943625898.png", record_pos=(0.248, -0.157), resolution=(2340, 1080)))

# hold 10 detik (10000 ms)
swipe((1760,214), (1760,214), duration=4)
sleep(3.0)
wait(Template(r"tpl1774944086717.png", record_pos=(0.001, -0.129), resolution=(2340, 1080)))
touch(Template(r"tpl1774944096500.png", record_pos=(0.448, 0.173), resolution=(2340, 1080)))
sleep(2.0)
touch(Template(r"tpl1774944250420.png", record_pos=(0.451, 0.181), resolution=(2340, 1080)))

