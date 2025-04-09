#-------------------------------------------------------------------------------
# Name:        nomenclature
# Purpose:
#
# Author:      Louis-Ulysse Simonet
#
# Created:     05/04/2025
# Copyright:   (c) Louis-Ulysse Simonet 2025
# Licence:     MIT License
#-------------------------------------------------------------------------------

from math import *
from PIL import Image, ImageDraw, ImageFont
from random import *
from time import *
import os
import uuid

def generate_image():

    ######################################################

    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=20)

    #######################################################

    alcans=["méthan","éthan","propan","butan","pentan","hexan","heptan","octan"]

    #####################################################

    def drawmolecul(length,family,ethylpos,methylpos,alcoolpos):
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



      if alcoolpos==2 or alcoolpos==4 or alcoolpos==6 or alcoolpos==8:
        draw.line([100+(alcoolpos-1)*(40*cos(pi/6)), 150+sin(pi/6)*40,100+(alcoolpos-1)*(40*cos(pi/6)),150+sin(pi/6)*40+40], fill="black", width=2)
        draw.text((100+(alcoolpos-1)*(40*cos(pi/6))-10,150+sin(pi/6)*40+40+10), "OH", fill="black", font=font)

      if alcoolpos==1 or alcoolpos==3 or alcoolpos==5 or alcoolpos==7:
        draw.line([100+(alcoolpos-1)*(40*cos(pi/6)), 150,100+(alcoolpos-1)*(40*cos(pi/6)),150-40], fill="black", width=2)
        draw.text((100+(alcoolpos-1)*(40*cos(pi/6))-20,150-40-25), "OH", fill="black", font=font)

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

    #alcool_start
    isalcool=randint(0,1)
    if isalcool==1:
      alcoolposm=randint(1,l)
    else:
      alcoolposm=0
    #alcool_end

    #solve conflicts_start
    suppr=randint(0,1)
    if alcoolposm==ethylposm:
        if suppr==0:
            alcoolposm=0
        else:
            ethylposm=0
    if alcoolposm==methylposm:
        if suppr==0:
            alcoolposm=0
        else:
            methylposm=0
    if methylposm==ethylposm:
        if suppr==0:
            ethylposm=0
        else:
            methylposm=0
    #solve_conflicts_end


    if alcoolposm!=0:
        if methylposm!=0:
            invertedmethylpos=l+1-methylposm
        else:
            invertedmethylpos=0
        if ethylposm!=0:
            invertedethylpos=l+1-ethylposm
        else:
            invertedethylpos=0

        invertedalcoolpos=l+1-alcoolposm

        if invertedalcoolpos<alcoolposm:
            alcoolposm=invertedalcoolpos
            ethylposm=invertedethylpos
            methylposm=invertedmethylpos
        else:
            if ethylposm*methylposm!=0:
                postot=str(ethylposm)+str(methylposm)
                invertedpostot=str(invertedethylpos)+str(invertedmethylpos)
                if invertedpostot<postot:
                    ethylposm=invertedethylpos
                    methylposm=invertedmethylpos
            else:
                if invertedethylpos<ethylposm:
                    ethylposm=invertedethylpos
                elif invertedmethylpos<methylposm:
                    methylposm=invertedmethylpos
    else:
        if methylposm!=0:
            invertedmethylpos=l+1-methylposm
        else:
            invertedmethylpos=0
        if ethylposm!=0:
            invertedethylpos=l+1-ethylposm
        else:
            invertedethylpos=0

        if ethylposm*methylposm!=0:
            postot=str(ethylposm)+str(methylposm)
            invertedpostot=str(invertedethylpos)+str(invertedmethylpos)
            if invertedpostot<postot:
                ethylposm=invertedethylpos
                methylposm=invertedmethylpos
        else:
            if invertedethylpos<ethylposm:
                ethylposm=invertedethylpos
            elif invertedmethylpos<methylposm:
                methylposm=invertedmethylpos


    #############
    drawmolecul(l,0,ethylposm,methylposm,alcoolposm)
    #############





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

    #alcool_naming_start
    if alcoolposm==0:
        alcoolname=""
        end="e"
    else:
        alcoolname="-"+str(alcoolposm)+"-"
        end="ol"

    ######################################################

    name=str(ethylposm)+isboth+str(methylposm)+alcans[l-1]+alcoolname+end

    img.save(os.path.join('static', 'molecule.png'), 'PNG')

    with open(os.path.join('static', 'moleculename.txt'), 'w', encoding='utf-8') as f:
        f.write(name)


generate_image()
