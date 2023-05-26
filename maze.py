#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (0,255,0)

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

x=1
y=1
game_over = False

def check_wall(x,y,new_x,new_y):
   if maze[new_y][new_x] == b :
       return new_x, new_y
   else :
       return x,y

def move_marble(pitch,roll,x,y):
    new_x = x
    new_y = y
    if 4 < pitch < 176 and x > 0:
        new_x -= 1 
    if 184 < pitch < 356 and x < 7:
        new_x += 1
    if 184 < roll < 356 and y > 0:
        new_y -= 1 
    if 4 < roll < 176 and y < 7:
        new_y += 1

    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y



while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll  = o["roll"]
    x,y  = move_marble(pitch,roll,x,y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))
    sleep(0.1)
    maze[y][x] = b
    if x == 6 and y == 6:
        maze[6][6] = g
        sense.set_pixels(sum(maze,[]))
        game_over = True
 

