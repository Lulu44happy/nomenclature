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
import glob

def increment_counter():
    # Lire le fichier counter.txt pour obtenir le nombre actuel de molécules générées
    try:
        with open('static/counter.txt', 'r') as f:
            counter = int(f.read().strip())
    except FileNotFoundError:
        counter = 0  # Si le fichier n'existe pas, on commence à 0

    # Incrémente le compteur
    counter += 1

    # Sauvegarde le nouveau nombre dans counter.txt
    with open('static/counter.txt', 'w') as f:
        f.write(str(counter))



def clean_old_images(max_images=35):
    files = sorted(glob.glob("static/*.png"), key=os.path.getmtime)
    for f in files[:-max_images]:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Erreur lors de la suppression de {f} : {e}")

def generate_image():

    #####################################################
 
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
 
    font_path = os.path.join("fonts", "DejaVuSans.ttf")
    font = ImageFont.truetype(font_path, size=20)
 
     #######################################################

    alcans=["méth","éth","prop","but","pent","hex","hept","oct"]

    #####################################################

    def drawmolecul(length,family,ethylpos,methylpos,alcoolpos,doublelpos):
      x=100
      y=150
      angle=30

      for i in range(1, length):
        # Calculer la nouvelle position en fonction de l'angle et de la longueur
        x_new = x + 40 * cos(pi * angle / 180)  # Conversion de l'angle en radians
        y_new = y + 40 * sin(pi * angle / 180)

        # Dessiner la ligne de (x, y) à (x_new, y_new)
        draw.line([x, y, x_new, y_new], fill="black", width=2)
        if doublelpos==i:
            if i==1 or i==3 or i==5 or i==7:
                draw.line([x+4, y-4, x_new+5, y_new-3], fill="black", width=2)
                if doublelpos!=1:
                    draw.line([x+4, y-4, x, y-1], fill="black", width=2)
            else:
                draw.line([x-3, y-3, x_new-3, y_new-3], fill="black", width=2)
                if doublelpos!=1:
                    draw.line([x_new-3, y_new-3, x_new, y_new], fill="black", width=2)

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

    # Decide randomly: 0 = neither, 1 = alcohol, 2 = double bond
    feature_type = randint(0, 2)

    alcoolposm = 0
    doublelposm = 0

    if feature_type == 1:
        alcoolposm = randint(1, l)
    elif feature_type == 2:
        doublelposm = randint(1, l)


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
             if invertedethylpos<ethylposm:
                ethylposm=invertedethylpos
                methylposm=invertedmethylpos
             elif invertedethylpos==ethylposm and invertedmethylpos<methylposm:
                ethylposm=invertedethylpos
                methylposm=invertedmethylpos
             elif ethylposm==0 and invertedmethylpos<methylposm:
                methylposm=invertedmethylpos

    if alcoolposm==0:
        invertedmethylpos=l+1-methylposm
        invertedethylpos=l+1-ethylposm
        if invertedethylpos==(l+1):
            invertedethylpos=0
        if invertedmethylpos==(l+1):
            invertedmethylpos=0
        if invertedethylpos<ethylposm:
            ethylposm=invertedethylpos
            methylposm=invertedmethylpos
        elif invertedethylpos==ethylposm and invertedmethylpos<methylposm:
            ethylposm=invertedethylpos
            methylposm=invertedmethylpos
        elif ethylposm==0 and invertedmethylpos<methylposm:
            methylposm=invertedmethylpos



    if doublelposm!=0:
        inverteddoublelpos=l-doublelposm
        if inverteddoublelpos<doublelposm:
            if methylposm!=0:
                invertedmethylpos=l+1-methylposm
            else:
                invertedmethylpos=0
            if ethylposm!=0:
                invertedethylpos=l+1-ethylposm
            else:
                invertedethylpos=0

            ethylposm=invertedethylpos
            methylposm=invertedmethylpos
            doublelposm=inverteddoublelpos

    if doublelposm*alcoolposm*ethylposm==0:
        if invertedmethylpos<methylposm:
            methylposm=invertedmethylpos




    #############
    drawmolecul(l,0,ethylposm,methylposm,alcoolposm,doublelposm)
    #############

    if doublelposm==0 and alcoolposm==0 and ethylposm!=0 and methylposm!=0 and int(str(l+1-ethylposm)+str(l+1-methylposm))<int(str(ethylposm)+str(methylposm)):
        ethylposm=l+1-ethylposm
        methylposm=l+1-methylposm

    if doublelposm==0 and alcoolposm==0 and ethylposm==0 and methylposm!=0 and (l+1-methylposm)<methylposm:
        methylposm=l+1-methylposm

    if doublelposm==0 and alcoolposm==0 and ethylposm!=0 and methylposm==0 and (l+1-ethylposm)<ethylposm:
        ethylposm=l+1-ethylposm

    if ethylposm==methylposm:
        methylposm=0

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
    if alcoolposm!=0:
        alcoolalcenename="an-"+str(alcoolposm)+"-"
        end="ol"
    #alcool_naming_end

    #alcene_naming_start
    if doublelposm!=0:
        alcoolalcenename="-"+str(doublelposm)+"-"
        end="ène"

    if doublelposm==0 and alcoolposm==0:
        alcoolalcenename=""
        end="ane"


    ######################################################



    name=str(ethylposm)+isboth+str(methylposm)+alcans[l-1]+alcoolalcenename+end

    img.save(os.path.join('static', name+".png"), 'PNG')

    increment_counter()
    clean_old_images()
    return name


generate_image()
