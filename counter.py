#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
sense.show_message("Press the Button to Start", text_colour=[255, 0, 0])
event = sense.stick.wait_for_event()

sleep(1)
sense.show_message("10", text_colour=[255, 255, 255])
for i in range (9,-1,-1):
    sense.show_letter( str(i) )
    sleep(1)
sense.clear()
sense.show_message("Bang!", text_colour=[255, 0, 0])
sleep(0.5)
sense.show_letter("*", text_colour=[175, 0, 175])





    
