# Hmm bot code with speakers, and orientation sensor module
#
# Author: 12934713

import logging
import sys
import time
import pygame
import random
import os

#Array that  references sounds
hmm = ["./sounds/dunky_hmm.wav","./sounds/hmm.wav","./sounds/nootnoot.wav","./sounds/pewdipiehmmlaugh.wav","./sounds/siegmeyermmm.wav","./sounds/spongebobhmm.wav","./sounds/Yodahmm.wav"]


def choose_action(x):
    if x == "1":
        print("Okay 1")
        pygame.mixer.music.load(hmm[0])
        pygame.mixer.music.play()
    elif x == "2":
        print("Okay 2")
        pygame.mixer.music.load(hmm[1])
        pygame.mixer.music.play()
    else:
        print("Not Okay")

print('program currently yrunning')
pygame.mixer.init()
print("pygame has finished initializing")
pygame.mixer.music.load(random.choice(hmm))
print("pygame has loaded all the hmm")

while True:
    READ=raw_input("which input\n")
    print(READ)
    choose_action(READ)

