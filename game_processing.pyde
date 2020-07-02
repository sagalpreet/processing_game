slider_width=100
slider_height=20
ball_diameter=50
ball_radius=ball_diameter/2
x_speed=2
y_speed=-2
ball_xpos=random(0+ball_radius,740-ball_radius)
ball_ypos=random(0+ball_radius,180-ball_radius)
slider_xpos=random(0,740-slider_width)
score=0
marks=0
endnow=0

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
    global score
    global marks
    global endnow
    if endnow==0:
        background(255,245,0)
        circle(ball_xpos,ball_ypos,ball_radius)
        rect(slider_xpos,height-slider_height,slider_width,slider_height)
        textSize(32)
        text(score,width-50,50)
        ball_xpos+=x_speed
        ball_ypos+=y_speed
        if ball_xpos>=width or ball_xpos<=0:
            x_speed*=-1
        if (ball_ypos>=height-ball_radius-slider_height and (ball_xpos-slider_xpos)*(ball_xpos-(slider_xpos+slider_width))<=0 ) or ball_ypos<=0:
            y_speed*=-1
            score+=marks
            marks=1-marks
        if ball_ypos>height:
            photo = loadImage("end.png")
            image(photo, 0, 0)
            textSize(32)
            text("Your score is ",width//2-100,height//2)
            text(score,width//2+120,height//2)
            ball_ypos=2*height   
            endnow=1
        f()
    elif endnow==1:
        delay(1000)
        background(255,245,0)
        textSize(32)
        text("Press Enter to Restart",50,50)
        text("Press Esc to Exit",50,80)
        g() 
    

def f():
    global slider_xpos
    if key==CODED:
        if keyCode==RIGHT and slider_xpos<width-slider_width:
            slider_xpos+=4
        if keyCode==LEFT and slider_xpos>0:
            slider_xpos-=4
    return

def g():
    global score
    global endnow
    global ball_xpos, ball_ypos, y_speed, marks
    if key==CODED:
        if keyCode==ENTER or keyCode==RETURN:
            endnow=0
            score=0
            y_speed=-2
            ball_xpos=random(0+ball_radius,740-ball_radius)
            ball_ypos=random(0+ball_radius,180-ball_radius)
            marks=0
        elif keyCode==ESC:
            exit()
