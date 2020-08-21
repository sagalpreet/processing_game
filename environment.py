import random
import agent

def reward(ball, slider):
    if ball.yPos > ball.yBottomLimit:
        return -10000
    else:
        return 0.1

class slider:
    def __init__(self, screen_height, screen_width):
        self.sizeX = screen_width//7
        self.sizeY = screen_height//20
        self.xRightLimit = screen_width - self.sizeX
        self.xLeftLimit = 0
        self.xPos = random.randint(self.xLeftLimit, self.xRightLimit)
        self.yPos = screen_height - self.sizeY
        self.speed = 1
        
    def moveLeft(self):
        self.speed = -abs(self.speed)
        new_x= self.xPos + self.speed
        new_x -= 2 * (new_x - self.xLeftLimit)*(new_x - self.xLeftLimit < 0)
        self.xPos = new_x   
        
    def moveRight(self):
        self.speed = abs(self.speed)
        new_x= self.xPos + self.speed
        new_x -= 2 * (new_x - self.xRightLimit)*(new_x - self.xRightLimit > 0)
        self.xPos = new_x
        
class ball:
    def __init__(self, screen_height, screen_width):
        self.radius = screen_height//50
        self.yBottomLimit = screen_height - screen_height//20 - self.radius
        self.yTopLimit = self.radius
        self.xLeftLimit = self.radius
        self.xRightLimit = screen_width - self.radius
        self.xPos = random.randint(self.xLeftLimit, self.xRightLimit)
        self.yPos = random.randint(self.yTopLimit, self.yBottomLimit//3+1)
        self.xSpeed = 1
        self.ySpeed = 1.1
        
    def move(self, slider):
        new_x = self.xPos + self.xSpeed
        new_y = self.yPos + self.ySpeed
        if new_x - self.xLeftLimit < 0 or new_x - self.xRightLimit > 0:
            self.xSpeed *= -1
        if (new_y - self.yBottomLimit > 0 and (new_x-slider.xPos-1)*(new_x-slider.xPos-slider.sizeX-3) <= 0) or new_y - self.yTopLimit < 0:
            self.ySpeed *= -1
        if (new_y - self.yBottomLimit > 0 and (new_x-slider.xPos-1)*(new_x-slider.xPos-slider.sizeX-3) > 0):
            self.yPos = new_y
            self.xPos = new_x
            return 1
        new_x -= 2 * (new_x - self.xRightLimit) * ((new_x - self.xRightLimit) > 0) + 2 * (new_x - self.xLeftLimit) * ((new_x - self.xLeftLimit) < 0)
        new_y -= 2 * (new_y - self.yBottomLimit) * ((new_y - self.yBottomLimit) > 0) + 2 * (new_y - self.yTopLimit) * ((new_y - self.yTopLimit) < 0)
        self.xPos = new_x
        self.yPos = new_y
        return 0
