#Macarios Hoover
# Places a randomly colored wool block

'''
Set up program for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of blackdata numbers for different color wool
Define a function called placeNext
    - it takes one arguement called direction
    - it changes the counter by adding the direction arguement
    - place a wool block of the color from the list where
    the index matches the counter variable
    - If the counter is out of bounds of the index, reset it
In a forever loop:
    - if the first button was pressed, placeNext(1)
    - if the second button was pressed, placeNext(-1)
'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Use a module for requesting data online
import requests

#Use a module to control time
import time

pos = mc.player.getTilePos()
#Setup for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
woolColors = [6, 5, 10, 14, 15, 0]

def placeNext(direction):
    global counter
    counter += direction
    if counter > 2:
        counter = 0
    elif counter < 0:
        counter = 2
    mc.setBlock(pos.x + 2,pos.y,pos.z + 0, 35, woolColors[counter])
    
while True:
    #Wait for one second
    time.sleep(0.1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    #Check the second button
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)