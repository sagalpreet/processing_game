slider_width=100
slider_height=20
ball_diameter=50
ball_radius=ball_diameter/2
x_speed=2
y_speed=-2
ball_xpos=random(0+ball_radius,740-ball_radius)
ball_ypos=random(0+ball_radius,180-ball_radius)
slider_xpos=random(0,740-slider_width)

def setup():
    size(740,360)
    
def draw():
    global slider_width
    global slider_height
    global ball_diameter
    global ball_radius
    global x_speed
    global y_speed
    global ball_xpos
    global ball_ypos
    global slider_xpos
    background(255,245,0)
    circle(ball_xpos,ball_ypos,ball_radius)
    rect(slider_xpos,height-slider_height,slider_width,slider_height)
    ball_xpos+=x_speed
    ball_ypos+=y_speed
    if ball_xpos>=width or ball_xpos<=0:
        x_speed*=-1
    if (ball_ypos>=height-ball_radius-slider_height and (ball_xpos-slider_xpos)*(ball_xpos-(slider_xpos+slider_width))<=0 ) or ball_ypos<=0:
        y_speed*=-1
    if ball_ypos>height:
        photo = loadImage("end.png")
        image(photo, 0, 0)
        
    f()

def f():
    global slider_xpos
    if key==CODED:
        if keyCode==RIGHT and slider_xpos<width-slider_width:
            slider_xpos+=4
        if keyCode==LEFT and slider_xpos>0:
            slider_xpos-=4
    return
