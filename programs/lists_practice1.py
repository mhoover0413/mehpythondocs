#M. Hoover
#Lists Practice 1

#A variable that hold more than one value is a list
#groceries = ["bread", "milk", "eggs", "cheese"]
#You can get items from a list by their index
#print(groceries[0])

#Start an empty list
#cart = []

#Fro every item in my grocier list: 
#    add that item to the cart
#for item in groceries:
    #cart.append(item)
#print(cart)

import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import random
funnyQoutes = ["hElP mE", "Wanna dance cowboy?", "Im sad", "run", "banana", "orange", "pizza pie", "train"]
x = random.randint(0, 7)
print(funnyQoutes[x])

while True:
    time.sleep(1)
    
    if GPIO.input(6) == GPIO.LOW:
        x = random.randint(0,7)
        print(funnyQoutes[x])

    
