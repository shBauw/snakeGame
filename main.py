# Import needed libraries
import pygame as pg
import sys

# Initiate pyGame
pg.init()

# Set default colours
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0

# Set window
size = width, height = 500, 500
screen = pg.display.set_mode(size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()