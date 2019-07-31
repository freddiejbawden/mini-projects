
from __future__ import division
import pygame
import math
import random
height = 500
width = 500
numberOfNodes = 100
nodeJoinRadius = 50
maxLineWeight = 5
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def posToArr(self):
        return [int(self.x),int(self.y)]
class Circle:
    def __init__(self):
        self.position = Position(random.randint(0,width),random.randint(0,height))
        self.color = pygame.Color(0,0,0)
        self.target = Position(random.randint(0,width),random.randint(0,height))
        self.speed = random.randint(200,200)
        self.currentXSpeed = (self.target.x-self.position.x)/self.speed
        self.currentYSpeed = (self.target.y-self.position.y)/self.speed

        self.nearestNeighbour = []
    def drawCircle(self):
        pygame.draw.circle(screen, pygame.Color(0,0,0), self.position.posToArr(),3)
    def distance(self,otherCircle):
        deltaX = math.pow((self.position.x - otherCircle.position.x),2)
        deltaY = math.pow((self.position.y - otherCircle.position.y),2)
        return math.sqrt(deltaX+deltaY)
    def drawLine(self):
        posSelf = self.position.posToArr()
        for circ in self.nearestNeighbour:
            posOtherCircle = circ.position.posToArr()
            if int(self.distance(circ)) == 0:
                continue
            dist = (self.distance(circ)/nodeJoinRadius)
            w = (self.distance(circ)/maxLineWeight)

            pygame.draw.line(screen,pygame.Color(255-int(255*dist),int(255*dist),0),posSelf,posOtherCircle)

    def nearTarget(self,tolerance):
        distToTargetX =(self.target.x - self.position.x)
        distToTargetY = (self.target.y - self.position.y)
        if (distToTargetX <=tolerance and distToTargetY <=tolerance):
            return True
        else:
            return False


    def setNewTarget(self):
        self.target = Position(random.randint(0,width),random.randint(0,height))
        self.currentXSpeed = (self.target.x-self.position.x)/self.speed
        self.currentYSpeed = (self.target.y-self.position.y)/self.speed

    def move(self):
        if (self.nearTarget(3)):
            self.setNewTarget()
        self.position.x += self.currentXSpeed
        self.position.y += self.currentYSpeed

class CircleList:
    def __init__(self,count):
        self.circles = []
        for i in range(count):
            self.circles.append(Circle())
    def drawCircles(self):
        for c in self.circles:
            c.drawLine()
            c.drawCircle()
    def moveCircles(self):
        for c in self.circles:
            c.move()
    def findNearest(self):
        #minimum value

        for c in self.circles:
            c.nearestNeighbour = []
            circMin = None

            circs = self.circles[:]
            for n in self.circles:
                dist = c.distance(n)
                if (dist < nodeJoinRadius and n != c):
                    c.nearestNeighbour.append(n)




pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Lines")
background_colour = (255,255,255)
screen.fill(background_colour)
running = True
cList = CircleList(numberOfNodes)
cList.findNearest()
cList.drawCircles()

pygame.display.flip()
while running:
    screen.fill(pygame.Color(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cList.moveCircles()
    cList.findNearest()

    cList.drawCircles()
    pygame.display.flip()
