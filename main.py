# Import needed libraries
import random
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
size = width, height = 500, 500
screen = pg.display.set_mode(size)

# Set initial position
xInit = 250
yInit = 250
square = 20
clock = pg.time.Clock()

# Movement
xChange = 0
yChange = 0
speed = 15

# Set scopes for conditions
apple = False
gameOver = False
randomx = 0
randomy = 0
score = 0

# Loop for game
while True:

    # Spawn new apple
    if apple == False or gameOver == True:
        randomx = round(random.randrange(square, width - square) / square) * square
        randomy = round(random.randrange(square, height - square) / square) * square

        # Check to make sure apple not spawned on snake
        if round(xInit / square) != round(randomx / square) and round(yInit / square) != round(randomy / square):
            apple = True
    
    # Check if apples are eaten
    if round(xInit / square) == round(randomx / square) and round(yInit / square) == round(randomy / square):
        apple = False
        score += 1
        speed = 15 + score

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
        
        # Set border
        if xInit >= width or xInit < 0 or yInit >= height or yInit < 0:
            gameOver = True
        
        # Create condition for snake overlapping itself

        # Ending condition
        while gameOver == True:
            screen.fill(black)
            screen.blit(pg.font.SysFont(None, 30).render("Q = Quit, R = Retry", True, green), [width / 4, height / 4])
            pg.display.update()

            # Quit or restart
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        sys.exit()
                    if event.key == pg.K_r:
                        score = 0
                        xInit = 250
                        yInit = 250
                        gameOver = False
    
    # Movement and refresh screen
    xInit += xChange
    yInit += yChange
    screen.fill(black)
    pg.draw.rect(screen, green, [xInit, yInit, square, square])
    pg.draw.rect(screen, red, [randomx, randomy, square, square])
    screen.blit(pg.font.SysFont("None", 30).render("Score: " + str(score), True, green), [width / 10, height / 10])
    pg.display.update()

    clock.tick(speed)