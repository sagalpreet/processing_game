# Importing dependecies
import agent
import rl_agent
import environment

# Setup the window size
def setup():
    size(740,360)
    background(255)
    noStroke()
    fill(0)
    smooth(4)
    
# Initializing our agent and environment
height = 360
width = 740
#player = rl_agent.agent()
player = agent.agent()
slider = environment.slider(height, width)
ball = environment.ball(height, width)


# Code for what actually is going to be rendered on to the screen
def draw():
    global ball, slider, player, height, width
    background(255)
    boolVar = ball.move(slider)
    if boolVar:
        exit()
    y = player.get_action(ball, slider)
    if y:
        slider.moveRight()
    else:
        slider.moveLeft()
    circle(ball.xPos, ball.yPos, ball.radius)
    rect(slider.xPos, slider.yPos, slider.sizeX, slider.sizeY)
