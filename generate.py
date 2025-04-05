#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      louis
#
# Created:     05/04/2025
# Copyright:   (c) louis 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import *
from PIL import Image, ImageDraw
from random import *
from time import *
import os


def generate_image():

    ######################################################

    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)

    #######################################################

    alcans=["méthan","éthan","propan","butan","pentan","hexan","heptan","octan"]

    #####################################################

    def drawmolecul(length,family,ethylpos,methylpos):
      x=100
      y=150
      angle=30

      for i in range(1, length):
        # Calculer la nouvelle position en fonction de l'angle et de la longueur
        x_new = x + 40 * cos(pi * angle / 180)  # Conversion de l'angle en radians
        y_new = y + 40 * sin(pi * angle / 180)

        # Dessiner la ligne de (x, y) à (x_new, y_new)
        draw.line([x, y, x_new, y_new], fill="black", width=2)

        # Mettre à jour la position actuelle
        x, y = x_new, y_new

        # Inverser l'angle (équivalent à setheading(-heading()))
        angle = -angle




      if methylpos==2 or methylpos==4 or methylpos==6 or methylpos==8:
        draw.line([100+(methylpos-1)*(40*cos(pi/6)), 150+sin(pi/6)*40,100+(methylpos-1)*(40*cos(pi/6)),150+sin(pi/6)*40+40], fill="black", width=2)

      if methylpos==1 or methylpos==3 or methylpos==5 or methylpos==7:
        draw.line([100+(methylpos-1)*(40*cos(pi/6)), 150,100+(methylpos-1)*(40*cos(pi/6)),150-40], fill="black", width=2)



      if ethylpos==2 or ethylpos==4 or ethylpos==6 or ethylpos==8:
        draw.line([100+(ethylpos-1)*(40*cos(pi/6)), 150+sin(pi/6)*40,100+(ethylpos-1)*(40*cos(pi/6)),150+sin(pi/6)*40+40], fill="black", width=2)
        draw.line([100+(ethylpos-1)*(40*cos(pi/6)),150+sin(pi/6)*40+40,(100+(ethylpos-1)*(40*cos(pi/6)))+40*cos(pi/6),150+sin(pi/6)*40+40+40*sin(pi/6)], fill="black", width=2)


      if ethylpos==1 or ethylpos==3 or ethylpos==5 or ethylpos==7:
        draw.line([100+(ethylpos-1)*(40*cos(pi/6)), 150,100+(ethylpos-1)*(40*cos(pi/6)),150-40], fill="black", width=2)
        draw.line([100+(ethylpos-1)*(40*cos(pi/6)),150-40,100+(ethylpos-1)*(40*cos(pi/6))-40*cos(pi/6),150-40-40*sin(pi/6)], fill="black", width=2)



    ###########################################################


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

    img.save(os.path.join('static', 'molecule.png'), 'PNG')

    with open(os.path.join('static', 'moleculename.txt'), 'w', encoding='utf-8') as f:
        f.write(name)


generate_image()
