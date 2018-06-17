# Hmm bot code with speakers, and orientation sensor module
#
# Author: 12934713

import logging
import sys
import time
import pygame
import random
import os
import RPi.GPIO as GPIO

#Array that  references sounds
hmm = ["./sounds/dunky_hmm.wav","./sounds/hmm.wav","./sounds/nootnoot.wav","./sounds/pewdipiehmmlaugh.wav","./sounds/siegmeyermmm.wav","./sounds/spongebobhmm.wav","./sounds/Yodahmm.wav"]

redPin = 15
greenPin = 13
bluePin = 11

def turnOn(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def redOn():
	turnOn(redPin)

def greenOn():
	turnOn(greenPin)

def blueOn():
	turnOn(bluePin)

def yellowOn():
	turnOn(redPin)
	turnOn(greenPin)

def cyanOn():
	turnOn(greenPin)
	turnOn(bluePin)

def magentaOn():
	turnOn(redPin)
	turnOn(bluePin)

def whiteOn():
	turnOn(redPin)
	turnOn(greenPin)
	turnOn(bluePin)

def redOff():
	turnOff(redPin)

def greenOff():
	turnOff(greenPin)

def blueOff():
	turnOff(bluePin)

def yellowOff():
	turnOff(redPin)
	turnOff(greenPin)

def cyanOff():
	turnOff(greenPin)
	turnOff(bluePin)

def magentaOff():
	turnOff(redPin)
	turnOff(bluePin)

def whiteOff():
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)

def choose_action(x):
    whiteOff()
    if x == "1":
        print("Okay 1")
        pygame.mixer.music.load(hmm[0])
        pygame.mixer.music.play()
        redOn()
    elif x == "2":
        print("Okay 2")
        pygame.mixer.music.load(hmm[1])
        pygame.mixer.music.play()
        greenOn()
    else:
        blueOn()
        print("Not Okay")

print('program currently yrunning')
pygame.mixer.init()
print("pygame has finished initializing")
pygame.mixer.music.load(random.choice(hmm))
print("pygame has loaded all the hmm")

while True:
    print("Choose which input for the example")
    print("1. Talking directly to the bot: While holding the bot")
    print("2. Talking directly to the bot: Resting on the table, with someone having a convo")
    print("3. Talking directly to the bot: Shouting at the bot")
    print("4. Talking directly to the bot: Whispering at the bot")
    print("5. Shaking the bot")
    print("6. Rotating the bot")
    print("7. Flipping the bot")
    print("8. Pushing or Sliding the bot")
    print("9. Shaking a table with the bot")
    print("10. Nudging the bot")
    print("11. Asking the bot for the weather")
    print("12. Asking the bot: Will I pass the assignemnt?")
    print("13. Asking the bot: Set an timer for 5 minutes")
    print("14. Asking the bot: Set an alarm for 7:30 am")
    print("15. Overwhelming negative response")
    print("16. Overwhelming positive response")

    READ=raw_input("which input")
    print(READ)
    choose_action(READ)

