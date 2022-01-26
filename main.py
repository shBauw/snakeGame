# Import needed libraries
from socketserver import BaseRequestHandler
import pygame as pg
import sys

# Initiate pyGame
pg.init()

# Set default colours
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Set window size
size = width, height = 501, 501
screen = pg.display.set_mode(size)

# Set initial position
xInit = 251
yInit = 251
clock = pg.time.Clock()

# Movement
xChange = 0
yChange = 0
speed = 20

# Loop for game
while True:

    # Event loop
    for event in pg.event.get():
        # Quit
        if event.type == pg.QUIT:
            sys.exit()
        
        # Change directions
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                xChange = 0
                yChange = -10
            elif event.key == pg.K_DOWN:
                xChange = 0
                yChange = 10
            elif event.key == pg.K_RIGHT:
                xChange = 10
                yChange = 0
            elif event.key == pg.K_LEFT:
                xChange = -10
                yChange = 0
    
    # Movement
    xInit += xChange
    yInit += yChange
    screen.fill(black)
    pg.draw.rect(screen, green, [xInit, yInit, 15, 15])
    pg.display.update()

    clock.tick(speed)