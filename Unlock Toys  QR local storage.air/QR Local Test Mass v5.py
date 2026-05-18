# -*- encoding=utf8 -*-
__author__ = "Remote"

from airtest.core.api import *
import os
import cv2
from pyzbar.pyzbar import decode

auto_setup(__file__)

# ==============================
# CONFIG
# ==============================

QR_FOLDER = r"D:\Applaydo\QR Local Test Mass v5.air\qr_images"

GAME_PACKAGE = "com.ferrero.applayduGP"

WAIT_GAME_LOAD = 15
WAIT_TOY_SCREEN = 6


# ==============================
# FUNCTION : READ QR
# ==============================

def read_qr(image_path):

    img = cv2.imread(image_path)
    decoded = decode(img)

    if decoded:
        return decoded[0].data.decode("utf-8")

    return None


# ==============================
# FUNCTION : LAUNCH DEEPLINK
# ==============================

def launch_deeplink(link):

    print("Launching:", link)

    device().shell(
        f'am start -a android.intent.action.VIEW -d "{link}"'
    )


# ==============================
# FUNCTION : TAP SCREEN
# ==============================

def tap_anywhere():

    print("Touch screen")

    # koordinat tengah layar
    w, h = device().get_current_resolution()

    touch((w/2, h/2))


# ==============================
# FUNCTION : CLOSE GAME
# ==============================

def close_game():

    print("Closing game")

    device().shell(
        f"am force-stop {GAME_PACKAGE}"
    )

    sleep(3)


# ==============================
# MAIN LOOP
# ==============================

qr_files = sorted(os.listdir(QR_FOLDER))

for file in qr_files:

    if file.lower().endswith((".png",".jpg",".jpeg")):

        qr_path = os.path.join(QR_FOLDER, file)

        print("=================================")
        print("Processing QR:", file)

        deeplink = read_qr(qr_path)

        if deeplink:

            print("QR content:", deeplink)

            # launch deeplink
            launch_deeplink(deeplink)

            # tunggu game load
            sleep(WAIT_GAME_LOAD)

            # tunggu screen toys
            sleep(WAIT_TOY_SCREEN)

            # touch screen
            tap_anywhere()

            sleep(10)

            # close game
            close_game()

        else:

            print("QR tidak terbaca:", file)