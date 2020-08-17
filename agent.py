import environment
import random

class agent:
    def __init__(self):
        pass
    
    def get_action(self, ball, slider):
        if random.random>0.1:
            if ball.xPos > slider.xPos + slider.sizeX:
                return 1
            else:
                return 0
        else:
            return random.choice([0,1])
