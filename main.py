# Mostly not my code
import random
from re import X
import pygame as pg
import sys

class cube(object):
    rows = 20
    width = 500
    def __init__(self, start, dirnx=1, dirny=0, colour=(0,255,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.colour = colour

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + dirnx, self.pos[1] + dirny)

    def draw(self, surface):
        display = self.width // self.rows
        x = self.pos[0]
        y = self.pos[1]

        pg.draw.rect(surface, self.colour, (x * display + 1, y * display + 1, display - 2, display - 2))

class snake(object):
    body = []
    turns = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.display.quit()
                    pg.quit()
                elif event.key == pg.K_UP:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pg.K_DOWN:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pg.K_RIGHT:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif event.key == pg.K_LEFT:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]         
        
        for count, index in enumerate(self.body):
            p = index.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                index.move(turn[0], turn[1])
                if count == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if index.dirnx == -1 and index.pos[0] <= 0: 
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif index.dirnx == 1 and index.pos[0] >= index.rows-1: 
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif index.dirny == 1 and index.pos[1] >= index.rows-1: 
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                elif index.dirny == -1 and index.pos[1] <= 0: 
                    print('Score: ', len(s.body))
                    s.reset((10,10))
                else: 
                    index.move(index.dirnx,index.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface)


def drawGrid(width, rows, surface):
    sizeBtwn = width // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pg.draw.line(surface, (255,255,255), (x,0),(x,width))
        pg.draw.line(surface, (255,255,255), (0,y),(width,y))
        

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pg.display.update()


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pg.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), colour=(255,0,0))
    flag = True

    clock = pg.time.Clock()
    
    while flag:
        pg.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), colour=(255,0,0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                s.reset((10,10))
                break

            
        redrawWindow(win)

main()