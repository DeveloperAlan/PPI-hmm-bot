# Hmm bot code with speakers, and orientation sensor module
#
# Author: 12934713

import logging
import sys
import time
import random
import os

def choose_action(x):
    if x == "1":
        print("Okay 1")
    elif x == "2":
        print("Okay 2")
    else:
        print("Not Okay")

print('program currently yrunning')
#Array that  references sounds
hmm = ["./sounds/dunky_hmm.wav","./sounds/hmm.wav","./sounds/nootnoot.wav","./sounds/pewdipiehmmlaugh.wav","./sounds/siegmeyermmm.wav","./sounds/spongebobhmm.wav","./sounds/Yodahmm.wav"]

while True:
    READ=raw_input("which input\n")
    choose_action(READ)

