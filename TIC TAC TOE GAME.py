#==============================================================TIC TAC TOE==============================================================
from turtle import *
from freegames import line
bgcolor("light green")
color("red")
def grid():
#  This funtion is defied to draw grid for the game
# line(a,b,c,d) draws straight line from (a,b) to (c,d) 
    line(-50, 150, -50, -150)
    line(50, 150, 50, -150)
    line(-150, -50, 150, -50)
    line(-150, 50, 150, 50)

def draw_cross(x, y):
#  This function is defined to draw cross in the grid
    line(x, y, x + 85, y + 85)
    line(x, y + 85, x + 85, y)

def draw_zero(x, y):
#  This function is defined to draw zero in the grid
    up()       #turle's pen is up by  appling  this command
    goto(x + 45, y )    #turtle's point goes to the cordinates written as argument
    down()      #turtle's  pen is down by  appling  this command
    circle(45)    #turtle  draws cirle or radius written in argument


state = {'player': 0}
players = [draw_cross, draw_zero]

def tap(x, y):
# This function is defined to draw cross and zero at the tapped square
    if -50<x<50:

        x=-45
    if -150<=x<=-50:

        x=-145
    if 50<=x<=150:
        x=55
    
    if -50<y<50:

        y=-45
    if -150<=y<=-50:


        y=-145
    if 50<=y<=150:
        y=55

    player = state['player']
    draw = players[player]
    
    sum=0
    while sum<10:
    
        if player==0:
            state['player']=1
            sum+=1
        else:
            state['player']=0
            sum+=1
    draw(x,y)

setup(340, 340, 370, 0)           # This function decides the place of window where 
hideturtle()                      
tracer(True)                      

grid()

onscreenclick(tap)
done()

# All the command like bgcolor , color , setup , tracer , hideturtle and onscreenclick are from turtle libray 

#line(a,b,c,d) draws straight line from (a,b) to (c,d)