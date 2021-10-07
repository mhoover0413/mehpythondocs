#Macarios Hoover
# Place a house with a button

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Use a module for requesting data online
import requests

#Use a module to control time
import time

#Setup for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        
def constructionTime():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+6, pos.y+5, pos.z+6, 5)
    mc.setBlocks(pos.x+2, pos.y+1, pos.z+2, pos.x+5, pos.y+4, pos.z+5, 0)
    mc.setBlocks(pos.x+3, pos.y+1, pos.z+1, pos.x+3, pos.y+2, pos.z+1, 0)
    mc.setBlocks(pos.x+6, pos.y+3, pos.z+3, pos.x+6, pos.y+2, pos.z+4, 102)
    mc.setBlocks(pos.x+1, pos.y+3, pos.z+3, pos.x+1, pos.y+2, pos.z+4, 102)

while True:
    #Wait for one second
    time.sleep(1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        constructionTime()
    #Check the second button
    elif GPIO.input(13) == GPIO.LOW:
        constructionTime()
    #Check the third button
    elif GPIO.input(19) == GPIO.LOW:
        constructionTime()
    #Check the fourth button
    elif GPIO.input(26) == GPIO.LOW:
        constructionTime()
