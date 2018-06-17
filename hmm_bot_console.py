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
hmm = ["./sounds/frustration_hmm_purple.wav","./sounds/good_idea_green.wav","./sounds/good_idea_yellow.wav","./sounds/holding_bot_blue.wav","./sounds/negative_hmm_red.wav","./sounds/thinking_hmm_green.wav","./sounds/try_again_hmm_orange.wav"]

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
        pygame.mixer.music.load(hmm[2])
        pygame.mixer.music.play()
        yellowOn()
    elif x == "2":
        pygame.mixer.music.load(hmm[1])
        pygame.mixer.music.play()
        cyanOn()
    elif x == "3":
        pygame.mixer.music.load(hmm[4])
        pygame.mixer.music.play()
        redOn()
    elif x == "4":
        pygame.mixer.music.load(hmm[5])
        pygame.mixer.music.play()
        cyanOn()
    elif x == "5":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "6":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "7":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "8":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "9":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "10":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        blueOn()
    elif x == "11":
        pygame.mixer.music.load(hmm[2])
        pygame.mixer.music.play()
        yellowOn()
    elif x == "12":
        pygame.mixer.music.load(hmm[5])
        pygame.mixer.music.play()
        blueOn()
    elif x == "13":
        pygame.mixer.music.load(hmm[1])
        time.sleep(2)
        redOn()
        time.sleep(1)
        redOff()
        time.sleep(1)
        redOn()
        time.sleep(1)
        redOff()
        pygame.mixer.music.play()
    elif x == "14":
        pygame.mixer.music.load(hmm[1])
        redOn()
        time.sleep(0.5)
        redOff()
        time.sleep(0.5)
        redOn()
        time.sleep(0.5)
        redOff()
        time.sleep(0.5)
        pygame.mixer.music.play()
    elif x == "15":
        pygame.mixer.music.load(hmm[4])
        pygame.mixer.music.play()
        redOn()
    elif x == "16":
        pygame.mixer.music.load(hmm[1])
        pygame.mixer.music.play()
        greenOn()
    elif x == "17":
        pygame.mixer.music.load(hmm[6])
        pygame.mixer.music.play()
        number = 0
        while number < 4:
            redOn()
            time.sleep(1)
            greenOn()
            time.sleep(1)
            number += 1
    elif x == "18":
        pygame.mixer.music.load(hmm[4])
        pygame.mixer.music.play()
        number = 0
        while number < 4:
            redOn()
            time.sleep(1)
            magentaOn()
            time.sleep(1)
            number += 1
    else:
        blueOn()
        print("Not Okay")

print('program currently yrunning')
pygame.mixer.init()
print("pygame has finished initializing")

whiteOn()

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
    print("17. Merry Christmas")
    print("18. Happy Halloween")

    READ=raw_input("which input")
    print(READ)
    choose_action(READ)

