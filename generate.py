from math import *
from turtle import *
from random import *
from time import *
from PIL import Image


def generate_image():

    #######################################################

    alcans=["méthan","éthan","propan","butan","pentan","hexan","heptan","octan"]

    #####################################################


    TurtleScreen._RUNNING = True
    screen = Screen()
    screen.setup(width=400, height=400)
    screen.bgcolor("white")

    t = Turtle()
    t.speed(0)
    t.pensize(2)

    #####################################################

    def drawmolecul(length,family,ethylpos,methylpos):
      penup()
      goto(-100,0)
      pendown()
      setheading(30)
      for i in range(1,length):
        forward(40)
        setheading(-heading())

      if methylpos==2 or methylpos==4 or methylpos==6 or methylpos==8:
          penup()
          goto(-100+(methylpos-1)*(40*cos(pi/6)),sin(pi/6)*40)
          setheading(90)
          pendown()
          forward(40)

      if methylpos==1 or methylpos==3 or methylpos==5 or methylpos==7:
          penup()
          goto(-100+(methylpos-1)*(40*cos(pi/6)),0)
          setheading(-90)
          pendown()
          forward(40)

      if ethylpos==2 or ethylpos==4 or ethylpos==6 or ethylpos==8:
          penup()
          goto(-100+(ethylpos-1)*(40*cos(pi/6)),sin(pi/6)*40)
          setheading(90)
          pendown()
          forward(40)
          setheading(30)
          forward(40)

      if ethylpos==1 or ethylpos==3 or ethylpos==5 or ethylpos==7:
          penup()
          goto(-100+(ethylpos-1)*(40*cos(pi/6)),0)
          setheading(-90)
          pendown()
          forward(40)
          setheading(-150)
          forward(40)

    ###########################################################

    hideturtle()
    speed(0)
    l=randint(5,8)


    #methyl_start
    ismethyl=randint(0,1)
    if ismethyl==1:
      methylposm=randint(2,l-1)
    else:
      methylposm=0
    #methyl_end

    #ethyl_start
    isethyl=randint(0,1)
    if l>4 and isethyl==1:
      ethylposm=randint(3,l-2)
    else:
      ethylposm=0
    #ethyl_end


    #############
    drawmolecul(l,0,ethylposm,methylposm)
    #############

    #reversingprocess_start
    invertedmethylpos=l+1-methylposm
    invertedethylpos=l+1-ethylposm

    if invertedethylpos<ethylposm:
        ethylposm=invertedethylpos
        methylposm=invertedmethylpos
    elif invertedmethylpos<methylposm and (ethylposm==0 or ethylposm==invertedethylpos):
        methylposm=invertedmethylpos
    #reversingprocess_end


    #ethyl-methyl naming_start
    if methylposm==0:
      methylposm=""
    else:
      methylposm=str(methylposm)+"-méthyl"

    if ethylposm==0:
      ethylposm=""
    else:
      ethylposm=str(ethylposm)+"-éthyl"

    if ismethyl*isethyl==1:
        isboth="-"
    else:
        isboth=""
    #ethyl-methyl naming_end

    ######################################################

    name=str(ethylposm)+isboth+str(methylposm)+alcans[l-1]+"e"
    penup()
    goto(0,-75)
    write(name)
    done()

generate_image()