# -*- encoding=utf8 -*-
__author__ = "Remote"

from airtest.core.api import *
import random
import time

auto_setup(__file__)
game_package = "com.ferrero.applayduGP"
start_app(game_package)
sleep(15)
wait(Template(r"tpl1773798519177.png", record_pos=(-0.448, -0.176), resolution=(2340, 1080)))
touch((123, 740))
sleep(1.0)
touch(Template(r"tpl1775794383991.png", record_pos=(0.292, -0.041), resolution=(2340, 1080)))
sleep(3.0)

w, h = device().get_current_resolution()

left = int(w * 0.40)
right = int(w * 0.60)

face_top = int(h * 0.170)
face_bottom = int(h * 0.490)

body_top = int(h * 0.505)
body_bottom = int(h * 0.733)

leg_top = int(h * 0.745)
leg_bottom = int(h * 0.956)

# =========================
# BASIC SCRUB (1 PASS)
# =========================
def scrub_once(top, bottom):

    y = bottom  # mulai dari bawah area
    direction = random.choice([True, False])

    while y >= top:

        start_x = random.randint(left + 30, right - 30)
        offset = random.randint(-30, 30)

        if direction:
            end_x = right - random.randint(10, 30)
        else:
            end_x = left + random.randint(10, 30)

        y_rand = y + random.randint(-10, 10)

        swipe((start_x, y_rand), (end_x, y_rand + offset), duration=0.6)
        swipe((end_x, y_rand + offset), (start_x, y_rand - 20), duration=0.6)

        y -= random.randint(35, 60)
        direction = not direction


# =========================
# SCRUB AREA (2x PER AREA)
# =========================
def scrub_area(top, bottom):
    for i in range(1):  # 🔥 2x scrub
        scrub_once(top, bottom)
        sleep(0.2)


# =========================
# MAIN LOOP BERDASARKAN WAKTU
# =========================
def run_scrub(duration_seconds=1400):  # 🔥 tentukan waktu di sini

    start_time = time.time()

    while time.time() - start_time < duration_seconds:

        print("Scrub Legs")
        scrub_area(leg_top, leg_bottom)

        print("Scrub Body")
        scrub_area(body_top, body_bottom)

        print("Scrub Face")
        scrub_area(face_top, face_bottom)

    print("TIME UP - STOP")


# =========================
# EXECUTION
# =========================
print("START CYCLIC SCRUB")

run_scrub(duration_seconds=140)  # 🔥 ubah sesuai kebutuhan

print("DONE")
wait(Template(r"tpl1776066445071.png", record_pos=(0.448, 0.174), resolution=(2340, 1080)))
touch(Template(r"tpl1776066458756.png", record_pos=(0.448, 0.175), resolution=(2340, 1080)))
sleep(4.0)


def tap_anywhere():

    print("Touch screen")

    # koordinat tengah layar
    w, h = device().get_current_resolution()

    touch((w/2, h/2))
sleep(1.0)

def tap_anywhere():

    print("Touch screen")

    # koordinat tengah layar
    w, h = device().get_current_resolution()

    touch((w/2, h/2))
    wait(Template(r"tpl1776066590579.png", record_pos=(0.452, 0.181), resolution=(2340, 1080)))
touch(Template(r"tpl1776066597583.png", record_pos=(0.451, 0.18), resolution=(2340, 1080)))
