# Hmm bot code with speakers, and orientation sensor module
#
# Author: 12934713

import logging
import sys
import time
import pygame
import random

from Adafruit_BNO055 import BNO055

def keep_trying_bno():
    try:
        bno.begin()
        return
    except RuntimeError:
        keep_trying_bno()

pygame.mixer.init()
hmm = ["./sounds/dunky_hmm.wav","./sounds/hmm.wav","./sounds/nootnoot.wav","./sounds/pewdipiehmmlaugh.wav","./sounds/siegmeyermmm.wav","./sounds/spongebobhmm.wav","./sounds/Yodahmm.wav"]

pygame.mixer.music.load(random.choice(hmm))


# Raspberry Pi configuration with serial UART and RST connected to GPIO 23:
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=23)

# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Try before you die
keep_trying_bno()


# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

print('Reading BNO055 data, press Ctrl-C to quit...')
og_heading = 0
og_roll = 0
og_pitch = 0
while True:
    # Read the Euler angles for heading, roll, pitch (all in degrees).
    heading, roll, pitch = bno.read_euler()

    if og_heading == 0 and og_roll == 0 and og_pitch == 0:
        og_heading = heading
        og_roll = roll
        og_pitch = pitch
    else:
        if og_heading != heading or og_roll != roll or og_pitch != pitch:
            print("It's different")
            pygame.mixer.music.load(random.choice(hmm))
            pygame.mixer.music.play()
            og_heading = heading
            og_roll = roll
            og_pitch = pitch

    # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
    sys, gyro, accel, mag = bno.get_calibration_status()
    # Print everything out.
    print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
          heading, roll, pitch, sys, gyro, accel, mag))
    # Other values you can optionally read:
    # Orientation as a quaternion:
    #x,y,z,w = bno.read_quaterion()
    # Sensor temperature in degrees Celsius:
    #temp_c = bno.read_temp()
    # Magnetometer data (in micro-Teslas):
    #x,y,z = bno.read_magnetometer()
    # Gyroscope data (in degrees per second):
    #x,y,z = bno.read_gyroscope()
    # Accelerometer data (in meters per second squared):
    #x,y,z = bno.read_accelerometer()
    # Linear acceleration data (i.e. acceleration from movement, not gravity--
    # returned in meters per second squared):
    #x,y,z = bno.read_linear_acceleration()
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    #x,y,z = bno.read_gravity()
    # Sleep for a second until the next reading.
    time.sleep(5)
