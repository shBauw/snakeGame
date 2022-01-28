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
xPos = 250
yPos = 250
square = 15
xSnake = [xPos]
ySnake = [yPos]
snakeLength = 1

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
pauseGame = False

# Loop for game
while True:

    # Spawn new apple
    if apple == False or gameOver == True:
        randomx = round(random.randrange(square, width - square) / square) * square
        randomy = round(random.randrange(square, height - square) / square) * square

        # Check to make sure apple not spawned on snake
        if round(xPos / square) != round(randomx / square) and round(yPos / square) != round(randomy / square):
            apple = True
    
    # Check if apples are eaten
    if round(xPos / square) == round(randomx / square) and round(yPos / square) == round(randomy / square):
        apple = False
        score += 1
        speed = 15 + score

        xSnake.append(xPos - xChange)
        ySnake.append(yPos - yChange)
        snakeLength += 1

    # Event loop
    for event in pg.event.get():
        # Quit
        if event.type == pg.QUIT:
            sys.exit()
        
        # Change directions
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                xChange = 0
                yChange = -15
            elif event.key == pg.K_DOWN:
                xChange = 0
                yChange = 15
            elif event.key == pg.K_RIGHT:
                xChange = 15
                yChange = 0
            elif event.key == pg.K_LEFT:
                xChange = -15
                yChange = 0
            # Create pause menu
            elif event.key == pg.K_ESCAPE:
                pauseGame = True
                while pauseGame == True:
                    screen.fill(black)
                    screen.blit(pg.font.SysFont("None", 30).render("Score: " + str(score), True, green), [width / 10, height / 10])
                    screen.blit(pg.font.SysFont(None, 30).render("Q = Quit, C = Continue", True, green), [width / 4, height / 4])
                    pg.display.update()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            sys.exit()
                        elif event.type == pg.KEYDOWN:
                            if event.key == pg.K_q:
                                sys.exit()
                            elif event.key == pg.K_c:
                                pauseGame = False
        
        # Set border
        if xPos >= width or xPos < 0 or yPos >= height or yPos < 0:
            gameOver = True

        # Ending condition
        while gameOver == True:
            screen.fill(black)
            screen.blit(pg.font.SysFont(None, 30).render("Q = Quit, R = Retry", True, green), [width / 4, height / 4])
            pg.display.update()

            # Quit or restart
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        sys.exit()
                    if event.key == pg.K_r:
                        score = 0
                        xPos = 250
                        yPos = 250
                        xSnake = [xPos]
                        ySnake = [yPos]
                        snakeLength = 1
                        xChange = 0
                        yChange = 0
                        speed = 15
                        gameOver = False
    
    # Movement
    xPos += xChange
    yPos += yChange
    xSnake.append(xPos)
    ySnake.append(yPos)

    # Remove end of snake
    while len(xSnake) > snakeLength:
        del xSnake[0] 
        del ySnake[0]

    # Check for overlapping
    for x in range(snakeLength - 1):
        if (xSnake[0] == xSnake[x + 1] and ySnake[0] == ySnake[x + 1]):
            gameOver = True

    # Refresh screen
    screen.fill(black)
    for x in range(len(xSnake)):
        for y in range(len(ySnake)):
            pg.draw.rect(screen, green, [xSnake[x], ySnake[y], square, square])
    pg.draw.rect(screen, red, [randomx, randomy, square, square])
    screen.blit(pg.font.SysFont("None", 30).render("Score: " + str(score), True, green), [width / 10, height / 10])
    pg.display.update()

    pg.time.Clock().tick(speed)