"""
new

Description:
"""

import time
import pygame.freetype
import pygame
import random

pygame.init()

screenwidth = 710
screenheight = 710
screen = pygame.display.set_mode([screenwidth, screenheight])


#game window
#def connect_4(score,First_player,placed,color,pc):

pygame.init()

Red1 = pygame.Rect(int(1/1), 10,int(170/2), 70)
Blue1 = pygame.Rect(int(1/1), 10,int(170/2), 70)
#borderslines===========================================
outline3 = pygame.Rect(int(1/1),1,int(10/2),100)
#===========================block
outline1 = pygame.Rect(int(-1/1),1,int(10/2),700)
#block==============================
outline2 = pygame.Rect(int(700/1),1,int(10/2),700)
#borderslines===========================================

#Game score keeper=================
Vert1 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert2 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert3 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert4 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert5 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert6 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
Vert7 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
#Game score keeper=================


intVert9 = [36, 37, 38, 39, 40, 41, 42]

intVert8 = [29, 30, 31, 32, 33, 34, 35]

intVert7 = [22, 23, 24, 25, 26, 27, 28]

intVert6 = [15, 16, 17, 18, 19, 20, 21]

intVert5 = [8, 9, 10, 11, 12, 13, 14]

intVert4 = [1, 2, 3, 4, 5, 6, 7]


Grid = [Vert1,Vert2,Vert3,Vert4,Vert5,Vert6,Vert7]
matches = []

#ylines===========================================
gridline1 = pygame.Rect(int(700/1),600,int(10/2),-500)
gridline2 = pygame.Rect(int(600/1),600,int(10/2),-500)
gridline3 = pygame.Rect(int(500/1),600,int(10/2),-500)
gridline4 = pygame.Rect(int(400/1),600,int(10/2),-500)
gridline5 = pygame.Rect(int(300/1),600,int(10/2),-500)
gridline6 = pygame.Rect(int(200/1),600,int(10/2),-500)
gridline7 = pygame.Rect(int(100/1),600,int(10/2),-500)
#ylines===========================================

starting_position = pygame.Rect(int(1/1), 10, int(170/2), 70)
starting_position2 = pygame.Rect(int(610/1), 10, int(170/2), 70)
Disappear = pygame.Rect(int(1/1), -1, int(170/2), 70)

#xlines===========================================
vertgridline1 = pygame.Rect(int(1/1),100,int(800/1),5)
vertgridline2 = pygame.Rect(int(1/1),200,int(800/1),5)
vertgridline3 = pygame.Rect(int(1/1),300,int(800/1),5)
vertgridline4 = pygame.Rect(int(1/1),400,int(800/1),5)
vertgridline5 = pygame.Rect(int(1/1),500,int(800/1),5)
vertgridline6 = pygame.Rect(int(1/1),600,int(800/1),5)
vertgridline7 = pygame.Rect(int(1/1),700,int(800/1),5)
#xlines===========================================



#max height is always at the bottom and max width is always to your far right

RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
psition = 100
position = 100
player = 0
BLACK = ((0,0,0))
GREEN = ((0,255,0))
score = ""
game_winner = ""
pc = WHITE
WINS = 0
Blue_Wins = 0
Red_Wins = 0
rainbow = ((200, 200, 55))
color = random.randint(0,5)
loading_screen = 100
round_winner = ""
round_winner_tie_breaker = 0
red_peice = 0
blue_peice = 0

placement = 0
color_list = [BLUE, RED, GREEN, WHITE,BLACK,rainbow]


#colors and mobility==================
#=======================restart game====================================

#==============peices activators
keys = pygame.key.get_pressed()

#verticlesections1 assign to blue and red==================
dropbox_0 = pygame.Rect(int(1/1), 610,int(85/1), 70)

Vert6sec1 = pygame.Rect(int(1/1), 510,int(85/1), 70)

Vert9sec1 = pygame.Rect(int(101/1), 510,int(170/2), 70)

Vert11sec1 = pygame.Rect(int(201/1), 510,int(170/2), 70)

Vert13sec1 = pygame.Rect(int(301/1), 510,int(170/2), 70)

Vert15sec1 = pygame.Rect(int(401/1), 510,int(170/2), 70)

Vert17sec1 = pygame.Rect(int(501/1), 510,int(170/2), 70)

Vert19sec1 = pygame.Rect(int(601/1), 510,int(170/2), 70)

Vert20sec1 = pygame.Rect(int(701/1), 510,int(170/2), 70)

#verticlesections2 assign to blue and red==================
dropbox_1 = pygame.Rect(int(101/1), 610,int(170/2), 70)

Vert6sec2 = pygame.Rect(int(1/1), 410,int(170/2), 70)

Vert9sec2 = pygame.Rect(int(101/1), 410,int(170/2), 70)

Vert11sec2 = pygame.Rect(int(201/1), 410,int(170/2), 70)

Vert13sec2 = pygame.Rect(int(301/1), 410,int(170/2), 70)

Vert15sec2 = pygame.Rect(int(401/1), 410,int(170/2), 70)

Vert17sec2 = pygame.Rect(int(501/1), 410,int(170/2), 70)

Vert19sec2 = pygame.Rect(int(601/1), 410,int(170/2), 70)

Vert20sec2 = pygame.Rect(int(701/1), 410,int(170/2), 70)


#verticlesections3 assign to blue and red==================
dropbox_2 = pygame.Rect(int(201/1), 610,int(170/2), 70)

Vert6sec3 = pygame.Rect(int(1/1), 310,int(170/2), 70)

Vert9sec3 = pygame.Rect(int(101/1), 310,int(170/2), 70)

Vert11sec3 = pygame.Rect(int(201/1), 310,int(170/2), 70)

Vert13sec3 = pygame.Rect(int(301/1), 310,int(170/2), 70)

Vert15sec3 = pygame.Rect(int(401/1), 310,int(170/2), 70)

Vert17sec3 = pygame.Rect(int(501/1), 310,int(170/2), 70)

Vert19sec3 = pygame.Rect(int(601/1), 310,int(170/2), 70)

Vert20sec3 = pygame.Rect(int(701/1), 310,int(170/2), 70)


#verticlesections4 assign to blue and red==================
dropbox_3 = pygame.Rect(int(301/1), 610,int(170/2), 70)

Vert6sec4 = pygame.Rect(int(1/1), 210,int(170/2), 70)

Vert9sec4 = pygame.Rect(int(101/1), 210,int(170/2), 70)

Vert11sec4 = pygame.Rect(int(201/1), 210,int(170/2), 70)

Vert13sec4 = pygame.Rect(int(301/1), 210,int(170/2), 70)

Vert15sec4 = pygame.Rect(int(401/1), 210,int(170/2), 70)

Vert17sec4 = pygame.Rect(int(501/1), 210,int(170/2), 70)

Vert19sec4 = pygame.Rect(int(601/1), 210,int(170/2), 70)

Vert20sec4 = pygame.Rect(int(701/1), 210,int(170/2), 70)


#verticlesections5 assign to blue and red==================
dropbox_4 = pygame.Rect(int(401/1), 610,int(170/2), 70)

Vert6sec5 = pygame.Rect(int(1/1), 110,int(170/2), 70)

Vert9sec5 = pygame.Rect(int(101/1), 110,int(170/2), 70)

Vert11sec5 = pygame.Rect(int(201/1), 110,int(170/2), 70)

Vert13sec5 = pygame.Rect(int(301/1), 110,int(170/2), 70)

Vert15sec5 = pygame.Rect(int(401/1), 110,int(170/2), 70)

Vert17sec5 = pygame.Rect(int(501/1), 110,int(170/2), 70)

Vert19sec5 = pygame.Rect(int(601/1), 110,int(170/2), 70)

Vert20sec5 = pygame.Rect(int(701/1), 110,int(170/2), 70)


#verticlesections6 assign to blue and red==================
dropbox_5 = pygame.Rect(int(501/1), 610,int(170/2), 70)

Vert6sec6 = pygame.Rect(int(1/1), 10,int(170/2), 70)

Vert9sec6 = pygame.Rect(int(101/1), 10,int(170/2), 70)

Vert11sec6 = pygame.Rect(int(201/1), 10,int(170/2), 70)

Vert13sec6 = pygame.Rect(int(301/1), 10,int(170/2), 70)

Vert15sec6 = pygame.Rect(int(401/1), 10,int(170/2), 70)

Vert17sec6 = pygame.Rect(int(501/1), 10,int(170/2), 70)

Vert19sec6 = pygame.Rect(int(601/1), 10,int(170/2), 70)

Vert20sec6 = pygame.Rect(int(701/1), 10,int(170/2), 70)
#=====================================================
dropbox_6 = pygame.Rect(int(601/1), 610,int(170/2), 70)

Vert6sec7 = pygame.Rect(int(1/1), 10,int(170/2), 70)

Vert9sec7 = pygame.Rect(int(101/1), 10,int(170/2), 70)

Vert11sec7 = pygame.Rect(int(201/1), 10,int(170/2), 70)

Vert13sec7 = pygame.Rect(int(301/1), 10,int(170/2), 70)

Vert15sec7 = pygame.Rect(int(401/1), 10,int(170/2), 70)

Vert17sec7 = pygame.Rect(int(501/1), 10,int(170/2), 70)

Vert19sec7 = pygame.Rect(int(601/1), 10,int(170/2), 70)

Vert20sec6 = pygame.Rect(int(701/1), 10,int(170/2), 70)


#SEC1=================================
SEC1square1_RED = 0
SEC1square2_RED = 0
SEC1square3_RED = 0
SEC1square4_RED = 0
SEC1square5_RED = 0
SEC1square6_RED = 0
SEC1square7_RED = 0
#SEC2=================================
SEC2square1_RED = 0
SEC2square2_RED = 0
SEC2square3_RED = 0
SEC2square4_RED = 0
SEC2square5_RED = 0
SEC2square6_RED = 0
SEC2square7_RED = 0
#SEC3=================================
SEC3square1_RED = False
SEC3square2_RED = False
SEC3square3_RED = False
SEC3square4_RED = False
SEC3square5_RED = False
SEC3square6_RED = False
SEC3square7_RED = False    

#SEC1=================================
SEC1square1_BLUE = 0
SEC1square2_BLUE = 0
SEC1square3_BLUE = 0
SEC1square4_BLUE = 0
SEC1square5_BLUE = 0
SEC1square6_BLUE = 0
SEC1square7_BLUE = 0
#SEC2=================================
SEC2square1_BLUE = 0
SEC2square2_BLUE = 0
SEC2square3_BLUE = 0
SEC2square4_BLUE = 0
SEC2square5_BLUE = 0
SEC2square6_BLUE = 0
SEC2square7_BLUE = 0
#SEC3=================================
SEC3square1_BLUE = False
SEC3square2_BLUE = False
SEC3square3_BLUE = False
SEC3square4_BLUE = False
SEC3square5_BLUE = False
SEC3square6_BLUE = False
SEC3square7_BLUE = False    



Bluerect = False
Redrect = False

First_player = "red"


#for every time that multiple of the same
#peices get placed in matches the list keeps adding on, but when a opposite piecfe
#gets placed in side the whole list gets deleted - list dosnt reset keeps previouse data
#----------------------------------------------------------------------------------------
#we make connect four a list with elements already in it and everytime the player places,
#the available element in connect4 list gets replaced by the players peice color,
#if a opposite peice gets placed in between and the dominant peice have no room to win,
#the whole list gets deleted.

game = 5

gameactivater = True
#game loop
for placement in range(5000):
    color = random.randint(0,5)
    placed = str(placement)
    if WINS < 8:
        score = str(WINS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameactivater = False
                pygame.display.flip()
        keys = pygame.key.get_pressed()



    #blue----------------------------------------------------
        if First_player == "red":
            Redrect = True
            pc = RED
            score = str(Red_Wins)

        if First_player == "blue":
            Bluerect = True
            pc = BLUE
            score = str(Blue_Wins)

        if not First_player == "blue":
            Bluerect = False
            Blue1.y = starting_position.y
            Blue1.x = starting_position.x

        else:
            Redrect = False
            Red1.y = starting_position.y
            Red1.x = starting_position.x


        if First_player == "red":
            Redrect = True

        if First_player == "red" and keys[pygame.K_SPACE]:
            time.sleep(0.2)
            Red1.y += 600
            First_player = "blue"


        if First_player == "red" and keys[pygame.K_RIGHT]:
            time.sleep(0.2)
            Red1.x += 100

        if First_player == "red" and keys[pygame.K_LEFT]:
            time.sleep(0.2)
            Red1.x -= 100

        if First_player == "blue":
            Bluerect = True

        if First_player == "blue" and keys[pygame.K_RETURN]:
            time.sleep(0.2)
            Blue1.y += 600
            First_player = "red"



        if First_player == "blue" and keys[pygame.K_RIGHT]:
            time.sleep(0.2)
            Blue1.x += 100

        if First_player == "blue" and keys[pygame.K_LEFT]:
            time.sleep(0.2)
            Blue1.x -= 100



        screen.fill((55, 5, 55))
        pygame.draw.rect(screen,(RED), gridline1)
        pygame.draw.rect(screen,(RED), gridline2)
        pygame.draw.rect(screen,(RED), gridline3)
        pygame.draw.rect(screen,(RED), gridline4)
        pygame.draw.rect(screen,(RED), gridline5)
        pygame.draw.rect(screen,(RED), gridline6)
        pygame.draw.rect(screen,(RED), gridline7)
                #=======================================
        pygame.draw.rect(screen,(BLUE), vertgridline1)
        pygame.draw.rect(screen,(BLUE), vertgridline2)
        pygame.draw.rect(screen,(BLUE), vertgridline3)    
        pygame.draw.rect(screen,(BLUE), vertgridline4)
        pygame.draw.rect(screen,(BLUE), vertgridline5)
        pygame.draw.rect(screen,(BLUE), vertgridline6)
        pygame.draw.rect(screen,(BLUE), vertgridline7)
                #============================================
        pygame.draw.rect(screen,(WHITE), outline1)
        pygame.draw.rect(screen,(WHITE), outline2)
        pygame.draw.rect(screen,(WHITE), outline3)
            #=================blue=======================
            #pygame.draw.rect(screen,RED,Vert8sec1)
        #game barriers#=================================
        if Red1.x < outline1.x:
            Red1.x = 601

        if Red1.x > outline2.x:
            Red1.x = 10

        if Blue1.x < outline1.x:
            Blue1.x = 601

        if Blue1.x > outline2.x:
            Blue1.x = 10

    #The if verts[0] == "red" or "blue": condition
    #The condition you're using doesn't correctly check if the 
    #first element of verts is either "red" or "blue". The expression verts[0] == 
    #"red" or "blue" will always evaluate to
    #True because "blue" is always truthy in Python.

        #game barriers#=================================

        #score keeper#================================
        if Blue_Wins == 3:
            game_winner = "BLUE"
            pc = BLUE
            First_player = "blue"

        if Blue_Wins > Red_Wins:
            round_winner = "BLUE"

        if round_winner_tie_breaker == 1:
            round_winner = "BLUE"

        if round_winner_tie_breaker == 2:
            round_winner = "RED"

        if Red_Wins > Blue_Wins:
            round_winner = "RED"

        if Red_Wins == 3:
            game_winner = "RED"
            pc = RED
            First_player = "red"




        #if blue in connect4 and vert 3 == SQ1 remove blue 

       #===================winning-pinning-blue-baby=============#
        if Vert7[0] == Vert7[1] == Vert7[2] == Vert7[3] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert7[1] == Vert7[2] == Vert7[3] == Vert7[4] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert7[2] == Vert7[3] == Vert7[4] == Vert7[5] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert7[3] == Vert7[4] == Vert7[5] == Vert7[6] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        #vert switch==============================================
        if Vert6[3] == Vert6[4] == Vert6[5] == Vert6[6] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert6[0] == Vert6[1] == Vert6[2] == Vert6[3] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert6[1] == Vert6[2] == Vert6[3] == Vert6[4] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert6[2] == Vert6[3] == Vert6[4] == Vert6[5] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        #========================sceond shelf====================--
        if Vert5[0] == Vert5[1] == Vert5[2] == Vert5[3] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert5[1] == Vert5[2] == Vert5[3] == Vert5[4] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert5[2] == Vert5[3] == Vert5[4] == Vert5[5] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert5[3] == Vert5[4] == Vert5[5] == Vert5[6] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
            #vert switch==============================================
        if Vert4[3] == Vert4[4] == Vert4[5] == Vert4[6] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert4[0] == Vert4[1] == Vert4[2] == Vert4[3] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert4[1] == Vert4[2] == Vert4[3] == Vert4[4] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert4[2] == Vert4[3] == Vert4[4] == Vert4[5] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        #========================Winsird shelf====================--
        if Vert3[0] == Vert3[1] == Vert3[2] == Vert3[3] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert3[1] == Vert3[2] == Vert3[3] == Vert3[4] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert3[2] == Vert3[3] == Vert3[4] == Vert3[5] == "blue":
            WINS += 1
            Blue_Wins += 1
            round_winner_tie_breaker = 1
        if Vert3[3] == Vert3[4] == Vert3[5] == Vert3[6] == "blue":
            Blue_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 1
        if Vert2[3] == Vert2[4] == Vert2[5] == Vert2[6] == "blue":
            Blue_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 1
        if Vert2[0] == Vert2[1] == Vert2[2] == Vert2[3] == "blue":
            Blue_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 1
        if Vert2[1] == Vert2[2] == Vert2[3] == Vert2[4] == "blue":
            Blue_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 1
        if Vert2[2] == Vert2[3] == Vert2[4] == Vert2[5] == "blue":
            Blue_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 1
        #========================fourth shelf====================--
        #===================winning-pinning-red-baby=============#
        if Vert7[0] == Vert7[1] == Vert7[2] == Vert7[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert7[1] == Vert7[2] == Vert7[3] == Vert7[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert7[2] == Vert7[3] == Vert7[4] == Vert7[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert7[3] == Vert7[4] == Vert7[5] == Vert7[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        #vert switch==============================================
        if Vert6[3] == Vert6[4] == Vert6[5] == Vert6[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert6[0] == Vert6[1] == Vert6[2] == Vert6[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert6[1] == Vert6[2] == Vert6[3] == Vert6[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert6[2] == Vert6[3] == Vert6[4] == Vert6[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        #========================sceond shelf====================--
        if Vert5[0] == Vert5[1] == Vert5[2] == Vert5[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert5[1] == Vert5[2] == Vert5[3] == Vert5[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert5[2] == Vert5[3] == Vert5[4] == Vert5[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert5[3] == Vert5[4] == Vert5[5] == Vert5[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        if Vert4[3] == Vert4[4] == Vert4[5] == Vert4[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2    
        elif Vert4[0] == Vert4[1] == Vert4[2] == Vert4[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert4[1] == Vert4[2] == Vert4[3] == Vert4[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert4[2] == Vert4[3] == Vert4[4] == Vert4[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        #========================ird shelf====================--
        if Vert3[0] == Vert3[1] == Vert3[2] == Vert3[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert3[1] == Vert3[2] == Vert3[3] == Vert3[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert3[2] == Vert3[3] == Vert3[4] == Vert3[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert3[3] == Vert3[4] == Vert3[5] == Vert3[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        if Vert2[3] == Vert2[4] == Vert2[5] == Vert2[6] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert2[0] == Vert2[1] == Vert2[2] == Vert2[3] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert2[1] == Vert2[2] == Vert2[3] == Vert2[4] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2
        elif Vert2[2] == Vert2[3] == Vert2[4] == Vert2[5] == "red":
            Red_Wins += 1
            WINS += 1
            round_winner_tie_breaker = 2



        #========================fifth shelf====================--




        #tehre shoukldnt be several instances for one peice drop
        #each row with boxes shoukld have itss own instance 
        #if blue drops iun the first row but red dropped first blud.collide push blue up
        #add outline barriers
        #add row limters
        #add score keeper
        #add winner decider#



        if Blue1.colliderect(dropbox_0):
            if Vert7[0] == "SQ1":
                Vert7[0] = "blue"

        if SEC1square1_RED > 10:
            SEC1square1_RED = 10

        if SEC1square1_BLUE > 10:
            SEC1square1_BLUE = 10

        if Blue1.colliderect(dropbox_0):
            SEC1square1_BLUE += 2

        if Red1.colliderect(dropbox_0):
            if Vert7[0] == "SQ1":
                Vert7[0] = "red" 

        if Red1.colliderect(dropbox_0):
            if Vert7[0] == "red":
                SEC1square1_RED += 2


        if SEC1square1_RED == 2:
            if Vert7[0] == "SQ1":
                Vert7[0] = "red"
        if SEC1square1_RED == 4:
            if Vert6[0] == "SQ1":
                Vert6[0] = "red"
        if SEC1square1_RED == 6:
            if Vert5[0] == "SQ1":
                Vert5[0] = "red"
        if SEC1square1_RED == 8:
            if Vert4[0] == "SQ1":
                Vert4[0] = "red"
        if SEC1square1_RED == 10:
            if Vert3[0] == "SQ1":
                Vert3[0] = "red"    

        if SEC1square1_BLUE == 2:
            if Vert7[0] == "SQ1":
                Vert7[0] = "blue"
        if SEC1square1_BLUE == 4:
            if Vert6[0] == "SQ1":
                Vert6[0] = "blue"
        if SEC1square1_BLUE == 6:
            if Vert5[0] == "SQ1":
                Vert5[0] = "blue"
        if SEC1square1_BLUE == 8:
            if Vert4[0] == "SQ1":
                Vert4[0] = "blue"
        if SEC1square1_BLUE == 10:
            if Vert3[0] == "SQ1":
                Vert3[0] = "blue"

        if Vert7[0] == "red" and SEC1square1_RED == 2:
            if not Vert7[0] == "blue":
                Vert7[0] = "red"
        if Vert7[0] == "red" and SEC1square1_RED == 4:
            if not Vert6[0] == "blue":
                Vert6[0] = "red"
        if Vert7[0] == "red" and SEC1square1_RED == 6:
            if not Vert5[0] == "blue":
                Vert5[0] = "red"
        if Vert7[0] == "red" and SEC1square1_RED == 8:
            if not Vert4[0] == "blue":
                Vert4[0] = "red"
        if Vert7[0] == "red" and SEC1square1_RED == 10:
            if not Vert3[0] == "blue":
                Vert3[0] = "red"

        if Vert7[0] == "blue" and SEC1square1_BLUE == 2:
            if not Vert7[0] == "red":
                Vert7[0] = "blue"
        if Vert7[0] == "blue" and SEC1square1_BLUE == 4:
            if not Vert6[0] == "red":
                Vert6[0] = "blue"
        if Vert7[0] == "blue" and SEC1square1_BLUE == 6:
            if not Vert6[0] == "red":
                Vert6[0] = "blue"
        if Vert7[0] == "blue" and SEC1square1_BLUE == 8:
            if not Vert6[0] == "red":
                Vert6[0] = "blue"
        if Vert7[0] == "blue" and SEC1square1_BLUE == 10:
            if not Vert6[0] == "red":
                Vert6[0] = "blue"


        if Vert7[0] == "red":
            pygame.draw.rect(screen,RED,Vert6sec1)
            if SEC1square1_BLUE == 0:
                SEC1square1_BLUE = 2
        if Vert6[0] == "red":
            pygame.draw.rect(screen,RED,Vert6sec2)
        if Vert5[0] == "red":
            pygame.draw.rect(screen,RED,Vert6sec3)
        if Vert4[0] == "red":
            pygame.draw.rect(screen,RED,Vert6sec4)
        if Vert3[0] == "red":
            pygame.draw.rect(screen,RED,Vert6sec5)


        if Vert7[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec1)
            if SEC1square1_RED == 0:
                SEC1square1_RED = 2
        if Vert6[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec2)
        if Vert5[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec3)
        if Vert4[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec4)
        if Vert3[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec5)
        if Vert2[0] == "blue":
            pygame.draw.rect(screen,BLUE,Vert6sec6)

        if Blue1.colliderect(dropbox_0):
            if Vert5[0] == "SQ1":
                if SEC1square1_RED == 4:
                    SEC1square1_BLUE = 6

          #new
        if Red1.colliderect(dropbox_0):
            if SEC1square1_RED == 6:
                if Vert5[0] == "blue":
                    if Vert7[0] == "red":
                        if Vert6[0] == "blue":
                            SEC1square1_RED += 2

             #new       
        if Red1.colliderect(dropbox_0):
            if SEC1square1_BLUE == 6:
                if Vert6[0] == "red":
                    if Vert7[0] == "blue":
                        SEC1square1_RED += 2

               #new         
        if Red1.colliderect(dropbox_0):
            if SEC1square1_RED == 6:
                if Vert7[0] == "red":
                    if Vert6[0] == "red":
                        if Vert5[0] == "blue":
                            SEC1square1_RED += 2

        #new
        if Red1.colliderect(dropbox_0):
            if SEC1square1_BLUE == 6:
                if Vert7[0] == "blue":
                    if Vert6[0] == "blue":
                        if Vert5[0] == "blue":
                            SEC1square1_RED += 4

        if Vert3[0] == "red":
            if Vert4[0] == "SQ1":
                SEC1square1_RED -= 2
                Vert3[0] = "SQ1"





            #new
        if Red1.colliderect(dropbox_0):
            if Vert7[0] == "red":
                if Vert6[0] == "blue":
                    if Vert5[0] == "blue":
                        SEC1square1_RED += 4


        if Blue1.colliderect(dropbox_0):
            if SEC1square1_BLUE == 4:
                if Vert5[0] == "red":
                    SEC1square1_BLUE += 4

        if Red1.colliderect(dropbox_0):
            if Vert4[0] == "SQ1":
                if SEC1square1_BLUE == 4:
                    if Vert6[0] == "blue":
                        SEC1square1_RED += 2

                    #new
        if Blue1.colliderect(dropbox_0):
            if Vert6[0] == "blue":
                if SEC1square1_RED == 6:
                    if Vert5[0] == "red":
                        SEC1square1_BLUE += 2

        if Red1.colliderect(dropbox_0):
            if SEC1square1_BLUE == 8:
                SEC1square1_RED = 10

        if Blue1.colliderect(dropbox_0):
            if SEC1square1_RED == 8:
                SEC1square1_BLUE = 10

        if Red1.colliderect(dropbox_0):
            if Vert7[0] == Vert6[0] == "blue":
                print("true")
                if SEC1square1_RED == 2:
                    SEC1square1_RED += 2

        if Red1.colliderect(dropbox_0) and Vert7[0] == "blue":
            SEC1square1_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert6sec2) and Vert6[0] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert6sec3) and Vert5[0] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert6sec4) and Vert4[0] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert6sec5) and Vert3[0] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_0) and Vert7[0] == "red":
            #if Vert6[0] == "SQ1":
                #SEC1square1_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert6sec2) and Vert6[0] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert6sec3) and Vert5[0] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert6sec4) and Vert4[0] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert6sec5) and Vert3[0] == "red":
            Blue1.y -= 100


    #============================square section one ==============
    #============================square section two ==============

        if Blue1.colliderect(dropbox_1):
            if Vert7[1] == "SQ1":
                Vert7[1] = "blue"

        if SEC1square2_RED > 10:
            SEC1square2_RED = 10

        if SEC1square2_BLUE > 10:
            SEC1square2_BLUE = 10

        if Blue1.colliderect(dropbox_1):
            SEC1square2_BLUE += 2

        if Red1.colliderect(dropbox_1):
            if Vert7[1] == "SQ1":
                Vert7[1] = "red" 

        if Red1.colliderect(dropbox_1):
            if Vert7[1] == "red":
                SEC1square2_RED += 2

        if SEC1square2_RED == 2:
            if Vert7[1] == "SQ1":
                Vert7[1] = "red"
        if SEC1square2_RED == 4:
            if Vert6[1] == "SQ1":
                Vert6[1] = "red"
        if SEC1square2_RED == 6:
            if Vert5[1] == "SQ1":
                Vert5[1] = "red"
        if SEC1square2_RED == 8:
            if Vert4[1] == "SQ1":
                Vert4[1] = "red"
        if SEC1square2_RED == 10:
            if Vert3[1] == "SQ1":
                Vert3[1] = "red"    

        if SEC1square2_BLUE == 2:
            if Vert7[1] == "SQ1":
                Vert7[1] = "blue"
        if SEC1square2_BLUE == 4:
            if Vert6[1] == "SQ1":
                Vert6[1] = "blue"
        if SEC1square2_BLUE == 6:
            if Vert5[1] == "SQ1":
                Vert5[1] = "blue"
        if SEC1square2_BLUE == 8:
            if Vert4[1] == "SQ1":
                Vert4[1] = "blue"
        if SEC1square2_BLUE == 10:
            if Vert3[1] == "SQ1":
                Vert3[1] = "blue"

        if Vert7[1] == "red" and SEC1square2_RED == 2:
            if not Vert7[1] == "blue":
                Vert7[1] = "red"
        if Vert7[1] == "red" and SEC1square2_RED == 4:
            if not Vert6[1] == "blue":
                Vert6[1] = "red"
        if Vert7[1] == "red" and SEC1square2_RED == 6:
            if not Vert5[1] == "blue":
                Vert5[1] = "red"
        if Vert7[1] == "red" and SEC1square2_RED == 8:
            if not Vert4[1] == "blue":
                Vert4[1] = "red"
        if Vert7[1] == "red" and SEC1square2_RED == 10:
            if not Vert3[1] == "blue":
                Vert3[1] = "red"

        if Vert7[1] == "blue" and SEC1square2_BLUE == 2:
            if not Vert7[1] == "red":
                Vert7[1] = "blue"
        if Vert7[1] == "blue" and SEC1square2_BLUE == 4:
            if not Vert6[1] == "red":
                Vert6[1] = "blue"
        if Vert7[1] == "blue" and SEC1square2_BLUE == 6:
            if not Vert5[1] == "red":
                Vert5[1] = "blue"
        if Vert7[1] == "blue" and SEC1square2_BLUE == 8:
            if not Vert4[1] == "red":
                Vert4[1] = "blue"
        if Vert7[1] == "blue" and SEC1square2_BLUE == 10:
            if not Vert3[1] == "red":
                Vert3[1] = "blue"


        if Vert7[1] == "red":
            pygame.draw.rect(screen,RED,Vert9sec1)
            if SEC1square2_BLUE == 0:
                SEC1square2_BLUE = 2
        if Vert6[1] == "red":
            pygame.draw.rect(screen,RED,Vert9sec2)
        if Vert5[1] == "red":
            pygame.draw.rect(screen,RED,Vert9sec3)
        if Vert4[1] == "red":
            pygame.draw.rect(screen,RED,Vert9sec4)
        if Vert3[1] == "red":
            pygame.draw.rect(screen,RED,Vert9sec5)


        if Vert7[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec1)
            if SEC1square2_RED == 0:
                SEC1square2_RED = 2
        if Vert6[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec2)
        if Vert5[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec3)
        if Vert4[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec4)
        if Vert3[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec5)
        if Vert2[1] == "blue":
            pygame.draw.rect(screen,BLUE,Vert9sec6)

        if Blue1.colliderect(dropbox_1):
            if Vert5[1] == "SQ1":
                if SEC1square2_RED == 4:
                    SEC1square2_BLUE = 6

        if Red1.colliderect(dropbox_1):
            if SEC1square2_RED == 6:
                if Vert5[1] == "blue":
                    if Vert7[1] == "red":
                        if Vert6[1] == "blue":
                            SEC1square2_RED += 2

             #new       
        if Red1.colliderect(dropbox_1):
            if SEC1square2_BLUE == 6:
                if Vert6[1] == "red":
                    if Vert7[1] == "blue":
                        SEC1square2_RED += 2

               #new         
        if Red1.colliderect(dropbox_1):
            if SEC1square2_RED == 6:
                if Vert7[1] == "red":
                    if Vert6[1] == "red":
                        if Vert5[1] == "blue":
                            SEC1square2_RED += 2

        #new
        if Red1.colliderect(dropbox_1):
            if SEC1square2_BLUE == 6:
                if Vert7[1] == "blue":
                    if Vert6[1] == "blue":
                        if Vert5[1] == "blue":
                            SEC1square2_RED += 4


        if Vert3[1] == "red":
            if Vert4[1] == "SQ1":
                SEC1square2_RED -= 2
                Vert3[1] = "SQ1"


            #new
        if Red1.colliderect(dropbox_1):
            if Vert7[1] == "red":
                if Vert6[1] == "blue":
                    if Vert5[1] == "blue":
                        SEC1square2_RED += 4

        if Blue1.colliderect(dropbox_1):
            if SEC1square2_BLUE == 4:
                if Vert5[1] == "red":
                    SEC1square2_BLUE += 4

        if Red1.colliderect(dropbox_1):
            if Vert4[1] == "SQ1":
                if SEC1square2_BLUE == 4:
                    if Vert6[1] == "blue":
                        SEC1square2_RED += 2

                    #new
        if Blue1.colliderect(dropbox_1):
            if Vert6[1] == "blue":
                if SEC1square2_RED == 6:
                    if Vert5[1] == "red":
                        SEC1square2_BLUE += 2

        if Red1.colliderect(dropbox_1):
            if SEC1square2_BLUE == 8:
                SEC1square2_RED = 10

        if Blue1.colliderect(dropbox_1):
            if SEC1square2_RED == 8:
                SEC1square2_BLUE = 10

        if Red1.colliderect(dropbox_1):
            if Vert7[1] == "blue" and Vert6[1] == "blue":
                if SEC1square2_RED == 2:
                    SEC1square2_RED += 2

        if Red1.colliderect(dropbox_1) and Vert7[1] == "blue":
            SEC1square2_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert9sec2) and Vert6[1] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert9sec3) and Vert5[1] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert9sec4) and Vert4[1] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert9sec5) and Vert3[1] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_1) and Vert7[1] == "red":
            #if Vert9[1] == "SQ1":
                #SEC1square2_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert9sec2) and Vert6[1] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert9sec3) and Vert5[1] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert9sec4) and Vert4[1] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert9sec5) and Vert3[1] == "red":
            Blue1.y -= 100

    #============================square section two ==============
    #============================square section three ==============
        if Blue1.colliderect(dropbox_2):
            if Vert7[2] == "SQ1":
                Vert7[2] = "blue"

        if SEC1square3_RED > 10:
            SEC1square3_RED = 10

        if SEC1square3_BLUE > 10:
            SEC1square3_BLUE = 10

        if Blue1.colliderect(dropbox_2):
            SEC1square3_BLUE += 2

        if Red1.colliderect(dropbox_2):
            if Vert7[2] == "SQ1":
                Vert7[2] = "red" 

        if Red1.colliderect(dropbox_2):
            if Vert7[2] == "red":
                SEC1square3_RED += 2

        if SEC1square3_RED == 2:
            if Vert7[2] == "SQ1":
                Vert7[2] = "red"
        if SEC1square3_RED == 4:
            if Vert6[2] == "SQ1":
                Vert6[2] = "red"
        if SEC1square3_RED == 6:
            if Vert5[2] == "SQ1":
                Vert5[2] = "red"
        if SEC1square3_RED == 8:
            if Vert4[2] == "SQ1":
                Vert4[2] = "red"
        if SEC1square3_RED == 10:
            if Vert3[2] == "SQ1":
                Vert3[2] = "red"    

        if SEC1square3_BLUE == 2:
            if Vert7[2] == "SQ1":
                Vert7[2] = "blue"
        if SEC1square3_BLUE == 4:
            if Vert6[2] == "SQ1":
                Vert6[2] = "blue"
        if SEC1square3_BLUE == 6:
            if Vert5[2] == "SQ1":
                Vert5[2] = "blue"
        if SEC1square3_BLUE == 8:
            if Vert4[2] == "SQ1":
                Vert4[2] = "blue"
        if SEC1square3_BLUE == 10:
            if Vert3[2] == "SQ1":
                Vert3[2] = "blue"

        if Vert7[2] == "red" and SEC1square3_RED == 2:
            if not Vert7[2] == "blue":
                Vert7[2] = "red"
        if Vert7[2] == "red" and SEC1square3_RED == 4:
            if not Vert6[2] == "blue":
                Vert6[2] = "red"
        if Vert7[2] == "red" and SEC1square3_RED == 6:
            if not Vert5[2] == "blue":
                Vert5[2] = "red"
        if Vert7[2] == "red" and SEC1square3_RED == 8:
            if not Vert4[2] == "blue":
                Vert4[2] = "red"
        if Vert7[2] == "red" and SEC1square3_RED == 10:
            if not Vert3[2] == "blue":
                Vert3[2] = "red"

        if Vert7[2] == "blue" and SEC1square3_BLUE == 2:
            if not Vert7[2] == "red":
                Vert7[2] = "blue"
        if Vert7[2] == "blue" and SEC1square3_BLUE == 4:
            if not Vert6[2] == "red":
                Vert6[2] = "blue"
        if Vert7[2] == "blue" and SEC1square3_BLUE == 6:
            if not Vert5[2] == "red":
                Vert5[2] = "blue"
        if Vert7[2] == "blue" and SEC1square3_BLUE == 8:
            if not Vert4[2] == "red":
                Vert4[2] = "blue"
        if Vert7[2] == "blue" and SEC1square3_BLUE == 10:
            if not Vert3[2] == "red":
                Vert3[2] = "blue"


        if Vert7[2] == "red":
            pygame.draw.rect(screen,RED,Vert11sec1)
            if SEC1square3_BLUE == 0:
                SEC1square3_BLUE = 2
        if Vert6[2] == "red":
            pygame.draw.rect(screen,RED,Vert11sec2)
        if Vert5[2] == "red":
            pygame.draw.rect(screen,RED,Vert11sec3)
        if Vert4[2] == "red":
            pygame.draw.rect(screen,RED,Vert11sec4)
        if Vert3[2] == "red":
            pygame.draw.rect(screen,RED,Vert11sec5)


        if Vert7[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec1)
            if SEC1square3_RED == 0:
                SEC1square3_RED = 2
        if Vert6[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec2)
        if Vert5[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec3)
        if Vert4[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec4)
        if Vert3[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec5)
        if Vert2[2] == "blue":
            pygame.draw.rect(screen,BLUE,Vert11sec6)

        if Blue1.colliderect(dropbox_2):
            if Vert5[2] == "SQ1":
                if SEC1square3_RED == 4:
                    SEC1square3_BLUE = 6

        if Red1.colliderect(dropbox_2):
            if SEC1square3_RED == 6:
                if Vert5[2] == "blue":
                    if Vert7[2] == "red":
                        if Vert6[2] == "blue":
                            SEC1square3_RED += 2

             #new       
        if Red1.colliderect(dropbox_2):
            if SEC1square3_BLUE == 6:
                if Vert6[2] == "red":
                    if Vert7[2] == "blue":
                        SEC1square3_RED += 2

               #new         
        if Red1.colliderect(dropbox_2):
            if SEC1square3_RED == 6:
                if Vert7[2] == "red":
                    if Vert6[2] == "red":
                        if Vert5[2] == "blue":
                            SEC1square3_RED += 2

        #new
        if Red1.colliderect(dropbox_2):
            if SEC1square3_BLUE == 6:
                if Vert7[2] == "blue":
                    if Vert6[2] == "blue":
                        if Vert5[2] == "blue":
                            SEC1square3_RED += 4

        if Vert3[2] == "red":
            if Vert4[2] == "SQ1":
                SEC1square3_RED -= 2
                Vert3[2] = "SQ1"


            #new
        if Red1.colliderect(dropbox_2):
            if Vert7[2] == "red":
                if Vert6[2] == "blue":
                    if Vert5[2] == "blue":
                        SEC1square3_RED += 4


        if Blue1.colliderect(dropbox_2):
            if SEC1square3_BLUE == 4:
                if Vert5[2] == "red":
                    SEC1square3_BLUE += 4

        if Red1.colliderect(dropbox_2):
            if Vert4[2] == "SQ1":
                if SEC1square3_BLUE == 4:
                    if Vert6[2] == "blue":
                        SEC1square3_RED += 2

                    #new
        if Blue1.colliderect(dropbox_2):
            if Vert6[2] == "blue":
                if SEC1square3_RED == 6:
                    if Vert5[2] == "red":
                        SEC1square3_BLUE += 2

        if Red1.colliderect(dropbox_2):
            if SEC1square3_BLUE == 8:
                SEC1square3_RED = 10

        if Blue1.colliderect(dropbox_2):
            if SEC1square3_RED == 8:
                SEC1square3_BLUE = 10

        if Red1.colliderect(dropbox_2):
            if Vert7[2] == "blue" and Vert6[2] == "blue":
                if SEC1square3_RED == 2:
                    SEC1square3_RED += 2

        if Red1.colliderect(dropbox_2) and Vert7[2] == "blue":
            SEC1square3_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert11sec2) and Vert6[2] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert11sec3) and Vert5[2] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert11sec4) and Vert4[2] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert11sec5) and Vert3[2] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_2) and Vert7[2] == "red":
            #if Vert11[2] == "SQ1":
                #SEC1square3_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert11sec2) and Vert6[2] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert11sec3) and Vert5[2] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert11sec4) and Vert4[2] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert11sec5) and Vert3[2] == "red":
            Blue1.y -= 100

    #============================square section three ==============
    #============================square section four ==============
        if Blue1.colliderect(dropbox_3):
            if Vert7[3] == "SQ1":
                Vert7[3] = "blue"

        if SEC1square4_RED > 10:
            SEC1square4_RED = 10

        if SEC1square4_BLUE > 10:
            SEC1square4_BLUE = 10

        if Blue1.colliderect(dropbox_3):
            SEC1square4_BLUE += 2

        if Red1.colliderect(dropbox_3):
            if Vert7[3] == "SQ1":
                Vert7[3] = "red" 

        if Red1.colliderect(dropbox_3):
            if Vert7[3] == "red":
                SEC1square4_RED += 2

        if SEC1square4_RED == 2:
            if Vert7[3] == "SQ1":
                Vert7[3] = "red"
        if SEC1square4_RED == 4:
            if Vert6[3] == "SQ1":
                Vert6[3] = "red"
        if SEC1square4_RED == 6:
            if Vert5[3] == "SQ1":
                Vert5[3] = "red"
        if SEC1square4_RED == 8:
            if Vert4[3] == "SQ1":
                Vert4[3] = "red"
        if SEC1square4_RED == 10:
            if Vert3[3] == "SQ1":
                Vert3[3] = "red"    

        if SEC1square4_BLUE == 2:
            if Vert7[3] == "SQ1":
                Vert7[3] = "blue"
        if SEC1square4_BLUE == 4:
            if Vert6[3] == "SQ1":
                Vert6[3] = "blue"
        if SEC1square4_BLUE == 6:
            if Vert5[3] == "SQ1":
                Vert5[3] = "blue"
        if SEC1square4_BLUE == 8:
            if Vert4[3] == "SQ1":
                Vert4[3] = "blue"
        if SEC1square4_BLUE == 10:
            if Vert3[3] == "SQ1":
                Vert3[3] = "blue"

        if Vert7[3] == "red" and SEC1square4_RED == 2:
            if not Vert7[3] == "blue":
                Vert7[3] = "red"
        if Vert7[3] == "red" and SEC1square4_RED == 4:
            if not Vert6[3] == "blue":
                Vert6[3] = "red"
        if Vert7[3] == "red" and SEC1square4_RED == 6:
            if not Vert5[3] == "blue":
                Vert5[3] = "red"
        if Vert7[3] == "red" and SEC1square4_RED == 8:
            if not Vert4[3] == "blue":
                Vert4[3] = "red"
        if Vert7[3] == "red" and SEC1square4_RED == 10:
            if not Vert3[3] == "blue":
                Vert3[3] = "red"

        if Vert7[3] == "blue" and SEC1square4_BLUE == 2:
            if not Vert7[3] == "red":
                Vert7[3] = "blue"
        if Vert7[3] == "blue" and SEC1square4_BLUE == 4:
            if not Vert6[3] == "red":
                Vert6[3] = "blue"
        if Vert7[3] == "blue" and SEC1square4_BLUE == 6:
            if not Vert5[3] == "red":
                Vert5[3] = "blue"
        if Vert7[3] == "blue" and SEC1square4_BLUE == 8:
            if not Vert4[3] == "red":
                Vert4[3] = "blue"
        if Vert7[3] == "blue" and SEC1square4_BLUE == 10:
            if not Vert3[3] == "red":
                Vert3[3] = "blue"


        if Vert7[3] == "red":
            pygame.draw.rect(screen,RED,Vert13sec1)
            if SEC1square4_BLUE == 0:
                SEC1square4_BLUE = 2
        if Vert6[3] == "red":
            pygame.draw.rect(screen,RED,Vert13sec2)
        if Vert5[3] == "red":
            pygame.draw.rect(screen,RED,Vert13sec3)
        if Vert4[3] == "red":
            pygame.draw.rect(screen,RED,Vert13sec4)
        if Vert3[3] == "red":
            pygame.draw.rect(screen,RED,Vert13sec5)


        if Vert7[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec1)
            if SEC1square4_RED == 0:
                SEC1square4_RED = 2
        if Vert6[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec2)
        if Vert5[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec3)
        if Vert4[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec4)
        if Vert3[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec5)
        if Vert2[3] == "blue":
            pygame.draw.rect(screen,BLUE,Vert13sec6)

        if Blue1.colliderect(dropbox_3):
            if Vert5[3] == "SQ1":
                if SEC1square4_RED == 4:
                    SEC1square4_BLUE = 6

        if Red1.colliderect(dropbox_3):
            if SEC1square4_RED == 6:
                if Vert5[3] == "blue":
                    if Vert7[3] == "red":
                        if Vert6[3] == "blue":
                            SEC1square4_RED += 2

             #new       
        if Red1.colliderect(dropbox_3):
            if SEC1square4_BLUE == 6:
                if Vert6[3] == "red":
                    if Vert7[3] == "blue":
                        SEC1square4_RED += 2

               #new         
        if Red1.colliderect(dropbox_3):
            if SEC1square4_RED == 6:
                if Vert7[3] == "red":
                    if Vert6[3] == "red":
                        if Vert5[3] == "blue":
                            SEC1square4_RED += 2

        #new
        if Red1.colliderect(dropbox_3):
            if SEC1square4_BLUE == 6:
                if Vert7[3] == "blue":
                    if Vert6[3] == "blue":
                        if Vert5[3] == "blue":
                            SEC1square4_RED += 4

        if Vert3[3] == "red":
            if Vert4[3] == "SQ1":
                SEC1square4_RED -= 2
                Vert3[3] = "SQ1"


            #new
        if Red1.colliderect(dropbox_3):
            if Vert7[3] == "red":
                if Vert6[3] == "blue":
                    if Vert5[3] == "blue":
                        SEC1square4_RED += 4


        if Blue1.colliderect(dropbox_3):
            if SEC1square4_BLUE == 4:
                if Vert5[3] == "red":
                    SEC1square4_BLUE += 4

        if Red1.colliderect(dropbox_3):
            if Vert4[3] == "SQ1":
                if SEC1square4_BLUE == 4:
                    if Vert6[3] == "blue":
                        SEC1square4_RED += 2

                    #new
        if Blue1.colliderect(dropbox_3):
            if Vert6[3] == "blue":
                if SEC1square4_RED == 6:
                    if Vert5[3] == "red":
                        SEC1square4_BLUE += 2

        if Red1.colliderect(dropbox_3):
            if SEC1square4_BLUE == 8:
                SEC1square4_RED = 10

        if Blue1.colliderect(dropbox_3):
            if SEC1square4_RED == 8:
                SEC1square4_BLUE = 10

        if Red1.colliderect(dropbox_3):
            if Vert7[3] == "blue" and Vert6[3] == "blue":
                if SEC1square4_RED == 2:
                    SEC1square4_RED += 2

        if Red1.colliderect(dropbox_3) and Vert7[3] == "blue":
            SEC1square4_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert13sec2) and Vert6[3] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert13sec3) and Vert5[3] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert13sec4) and Vert4[3] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert13sec5) and Vert3[3] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_3) and Vert7[3] == "red":
            #if Vert13[3] == "SQ1":
                #SEC1square4_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert13sec2) and Vert6[3] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert13sec3) and Vert5[3] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert13sec4) and Vert4[3] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert13sec5) and Vert3[3] == "red":
            Blue1.y -= 100

    #============================square section four ==============
    #============================square section six ==============
        if Blue1.colliderect(dropbox_4):
            if Vert7[4] == "SQ1":
                Vert7[4] = "blue"

        if SEC1square5_RED > 10:
            SEC1square5_RED = 10

        if SEC1square5_BLUE > 10:
            SEC1square5_BLUE = 10

        if Blue1.colliderect(dropbox_4):
            SEC1square5_BLUE += 2

        if Red1.colliderect(dropbox_4):
            if Vert7[4] == "SQ1":
                Vert7[4] = "red" 

        if Red1.colliderect(dropbox_4):
            if Vert7[4] == "red":
                SEC1square5_RED += 2

        if SEC1square5_RED == 2:
            if Vert7[4] == "SQ1":
                Vert7[4] = "red"
        if SEC1square5_RED == 4:
            if Vert6[4] == "SQ1":
                Vert6[4] = "red"
        if SEC1square5_RED == 6:
            if Vert5[4] == "SQ1":
                Vert5[4] = "red"
        if SEC1square5_RED == 8:
            if Vert4[4] == "SQ1":
                Vert4[4] = "red"
        if SEC1square5_RED == 10:
            if Vert3[4] == "SQ1":
                Vert3[4] = "red"    

        if SEC1square5_BLUE == 2:
            if Vert7[4] == "SQ1":
                Vert7[4] = "blue"
        if SEC1square5_BLUE == 4:
            if Vert6[4] == "SQ1":
                Vert6[4] = "blue"
        if SEC1square5_BLUE == 6:
            if Vert5[4] == "SQ1":
                Vert5[4] = "blue"
        if SEC1square5_BLUE == 8:
            if Vert4[4] == "SQ1":
                Vert4[4] = "blue"
        if SEC1square5_BLUE == 10:
            if Vert3[4] == "SQ1":
                Vert3[4] = "blue"

        if Vert7[4] == "red" and SEC1square5_RED == 2:
            if not Vert7[4] == "blue":
                Vert7[4] = "red"
        if Vert7[4] == "red" and SEC1square5_RED == 4:
            if not Vert6[4] == "blue":
                Vert6[4] = "red"
        if Vert7[4] == "red" and SEC1square5_RED == 6:
            if not Vert5[4] == "blue":
                Vert5[4] = "red"
        if Vert7[4] == "red" and SEC1square5_RED == 8:
            if not Vert4[4] == "blue":
                Vert4[4] = "red"
        if Vert7[4] == "red" and SEC1square5_RED == 10:
            if not Vert3[4] == "blue":
                Vert3[4] = "red"

        if Vert7[4] == "blue" and SEC1square5_BLUE == 2:
            if not Vert7[4] == "red":
                Vert7[4] = "blue"
        if Vert7[4] == "blue" and SEC1square5_BLUE == 4:
            if not Vert6[4] == "red":
                Vert6[4] = "blue"
        if Vert7[4] == "blue" and SEC1square5_BLUE == 6:
            if not Vert5[4] == "red":
                Vert5[4] = "blue"
        if Vert7[4] == "blue" and SEC1square5_BLUE == 8:
            if not Vert4[4] == "red":
                Vert4[4] = "blue"
        if Vert7[4] == "blue" and SEC1square5_BLUE == 10:
            if not Vert3[4] == "red":
                Vert3[4] = "blue"


        if Vert7[4] == "red":
            pygame.draw.rect(screen,RED,Vert15sec1)
            if SEC1square5_BLUE == 0:
                SEC1square5_BLUE = 2
        if Vert6[4] == "red":
            pygame.draw.rect(screen,RED,Vert15sec2)
        if Vert5[4] == "red":
            pygame.draw.rect(screen,RED,Vert15sec3)
        if Vert4[4] == "red":
            pygame.draw.rect(screen,RED,Vert15sec4)
        if Vert3[4] == "red":
            pygame.draw.rect(screen,RED,Vert15sec5)


        if Vert7[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec1)
            if SEC1square5_RED == 0:
                SEC1square5_RED = 2
        if Vert6[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec2)
        if Vert5[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec3)
        if Vert4[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec4)
        if Vert3[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec5)
        if Vert2[4] == "blue":
            pygame.draw.rect(screen,BLUE,Vert15sec6)

        if Blue1.colliderect(dropbox_4):
            if Vert5[4] == "SQ1":
                if SEC1square5_RED == 4:
                    SEC1square5_BLUE = 6

        if Red1.colliderect(dropbox_4):
            if SEC1square5_RED == 6:
                if Vert5[4] == "blue":
                    if Vert7[4] == "red":
                        if Vert6[4] == "blue":
                            SEC1square5_RED += 2

             #new       
        if Red1.colliderect(dropbox_4):
            if SEC1square5_BLUE == 6:
                if Vert6[4] == "red":
                    if Vert7[4] == "blue":
                        SEC1square5_RED += 2

               #new         
        if Red1.colliderect(dropbox_4):
            if SEC1square5_RED == 6:
                if Vert7[4] == "red":
                    if Vert6[4] == "red":
                        if Vert5[4] == "blue":
                            SEC1square5_RED += 2

        #new
        if Red1.colliderect(dropbox_4):
            if SEC1square5_BLUE == 6:
                if Vert7[4] == "blue":
                    if Vert6[4] == "blue":
                        if Vert5[4] == "blue":
                            SEC1square5_RED += 4

        if Vert3[4] == "red":
            if Vert4[4] == "SQ1":
                SEC1square5_RED -= 2
                Vert3[4] = "SQ1"


            #new
        if Red1.colliderect(dropbox_4):
            if Vert7[4] == "red":
                if Vert6[4] == "blue":
                    if Vert5[4] == "blue":
                        SEC1square5_RED += 4

        if Blue1.colliderect(dropbox_4):
            if SEC1square5_BLUE == 4:
                if Vert5[4] == "red":
                    SEC1square5_BLUE += 4

        if Red1.colliderect(dropbox_4):
            if Vert4[4] == "SQ1":
                if SEC1square5_BLUE == 4:
                    if Vert6[4] == "blue":
                        SEC1square5_RED += 2

                    #new
        if Blue1.colliderect(dropbox_4):
            if Vert6[4] == "blue":
                if SEC1square5_RED == 6:
                    if Vert5[4] == "red":
                        SEC1square5_BLUE += 2

        if Red1.colliderect(dropbox_4):
            if SEC1square5_BLUE == 8:
                SEC1square5_RED = 10

        if Blue1.colliderect(dropbox_4):
            if SEC1square5_RED == 8:
                SEC1square5_BLUE = 10

        if Red1.colliderect(dropbox_4):
            if Vert7[4] == "blue" and Vert6[4] == "blue":
                if SEC1square5_RED == 2:
                    SEC1square5_RED += 2

        if Red1.colliderect(dropbox_4) and Vert7[4] == "blue":
            SEC1square5_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert15sec2) and Vert6[4] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert15sec3) and Vert5[4] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert15sec4) and Vert4[4] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert15sec5) and Vert3[4] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_4) and Vert7[4] == "red":
            #if Vert15[4] == "SQ1":
                #SEC1square5_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert15sec2) and Vert6[4] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert15sec3) and Vert5[4] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert15sec4) and Vert4[4] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert15sec5) and Vert3[4] == "red":
            Blue1.y -= 100

    #============================square section six ==============
    #============================square section seven ==============
        if Blue1.colliderect(dropbox_5):
            if Vert7[5] == "SQ1":
                Vert7[5] = "blue"

        if SEC1square6_RED > 10:
            SEC1square6_RED = 10

        if SEC1square6_BLUE > 10:
            SEC1square6_BLUE = 10

        if Blue1.colliderect(dropbox_5):
            SEC1square6_BLUE += 2

        if Red1.colliderect(dropbox_5):
            if Vert7[5] == "SQ1":
                Vert7[5] = "red" 

        if Red1.colliderect(dropbox_5):
            if Vert7[5] == "red":
                SEC1square6_RED += 2

        if SEC1square6_RED == 2:
            if Vert7[5] == "SQ1":
                Vert7[5] = "red"
        if SEC1square6_RED == 4:
            if Vert6[5] == "SQ1":
                Vert6[5] = "red"
        if SEC1square6_RED == 6:
            if Vert5[5] == "SQ1":
                Vert5[5] = "red"
        if SEC1square6_RED == 8:
            if Vert4[5] == "SQ1":
                Vert4[5] = "red"
        if SEC1square6_RED == 10:
            if Vert3[5] == "SQ1":
                Vert3[5] = "red"    

        if SEC1square6_BLUE == 2:
            if Vert7[5] == "SQ1":
                Vert7[5] = "blue"
        if SEC1square6_BLUE == 4:
            if Vert6[5] == "SQ1":
                Vert6[5] = "blue"
        if SEC1square6_BLUE == 6:
            if Vert5[5] == "SQ1":
                Vert5[5] = "blue"
        if SEC1square6_BLUE == 8:
            if Vert4[5] == "SQ1":
                Vert4[5] = "blue"
        if SEC1square6_BLUE == 10:
            if Vert3[5] == "SQ1":
                Vert3[5] = "blue"

        if Vert7[5] == "red" and SEC1square6_RED == 2:
            if not Vert7[5] == "blue":
                Vert7[5] = "red"
        if Vert7[5] == "red" and SEC1square6_RED == 4:
            if not Vert6[5] == "blue":
                Vert6[5] = "red"
        if Vert7[5] == "red" and SEC1square6_RED == 6:
            if not Vert5[5] == "blue":
                Vert5[5] = "red"
        if Vert7[5] == "red" and SEC1square6_RED == 8:
            if not Vert4[5] == "blue":
                Vert4[5] = "red"
        if Vert7[5] == "red" and SEC1square6_RED == 10:
            if not Vert3[5] == "blue":
                Vert3[5] = "red"

        if Vert7[5] == "blue" and SEC1square6_BLUE == 2:
            if not Vert7[5] == "red":
                Vert7[5] = "blue"
        if Vert7[5] == "blue" and SEC1square6_BLUE == 4:
            if not Vert6[5] == "red":
                Vert6[5] = "blue"
        if Vert7[5] == "blue" and SEC1square6_BLUE == 6:
            if not Vert5[5] == "red":
                Vert5[5] = "blue"
        if Vert7[5] == "blue" and SEC1square6_BLUE == 8:
            if not Vert4[5] == "red":
                Vert4[5] = "blue"
        if Vert7[5] == "blue" and SEC1square6_BLUE == 10:
            if not Vert3[5] == "red":
                Vert3[5] = "blue"


        if Vert7[5] == "red":
            pygame.draw.rect(screen,RED,Vert17sec1)
            if SEC1square6_BLUE == 0:
                SEC1square6_BLUE = 2
        if Vert6[5] == "red":
            pygame.draw.rect(screen,RED,Vert17sec2)
        if Vert5[5] == "red":
            pygame.draw.rect(screen,RED,Vert17sec3)
        if Vert4[5] == "red":
            pygame.draw.rect(screen,RED,Vert17sec4)
        if Vert3[5] == "red":
            pygame.draw.rect(screen,RED,Vert17sec5)


        if Vert7[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec1)
            if SEC1square6_RED == 0:
                SEC1square6_RED = 2
        if Vert6[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec2)
        if Vert5[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec3)
        if Vert4[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec4)
        if Vert3[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec5)
        if Vert2[5] == "blue":
            pygame.draw.rect(screen,BLUE,Vert17sec6)

        if Blue1.colliderect(dropbox_5):
            if Vert5[5] == "SQ1":
                if SEC1square6_RED == 4:
                    SEC1square6_BLUE = 6

        if Red1.colliderect(dropbox_5):
            if SEC1square6_RED == 6:
                if Vert5[5] == "blue":
                    if Vert7[5] == "red":
                        if Vert6[5] == "blue":
                            SEC1square6_RED += 2

             #new       
        if Red1.colliderect(dropbox_5):
            if SEC1square6_BLUE == 6:
                if Vert6[5] == "red":
                    if Vert7[5] == "blue":
                        SEC1square6_RED += 2

               #new         
        if Red1.colliderect(dropbox_5):
            if SEC1square6_RED == 6:
                if Vert7[5] == "red":
                    if Vert6[5] == "red":
                        if Vert5[5] == "blue":
                            SEC1square6_RED += 2

        #new
        if Red1.colliderect(dropbox_5):
            if SEC1square6_BLUE == 6:
                if Vert7[5] == "blue":
                    if Vert6[5] == "blue":
                        if Vert5[5] == "blue":
                            SEC1square6_RED += 4

        if Vert3[5] == "red":
            if Vert4[5] == "SQ1":
                SEC1square6_RED -= 2
                Vert3[5] = "SQ1"
                print("your cooked",Vert3)

            #new
        if Red1.colliderect(dropbox_5):
            if Vert7[5] == "red":
                if Vert6[5] == "blue":
                    if Vert5[5] == "blue":
                        SEC1square6_RED += 4


        if Blue1.colliderect(dropbox_5):
            if SEC1square6_BLUE == 4:
                if Vert5[5] == "red":
                    SEC1square6_BLUE += 4

        if Red1.colliderect(dropbox_5):
            if Vert4[5] == "SQ1":
                if SEC1square6_BLUE == 4:
                    if Vert6[5] == "blue":
                        SEC1square6_RED += 2

                    #new
        if Blue1.colliderect(dropbox_5):
            if Vert6[5] == "blue":
                if SEC1square6_RED == 6:
                    if Vert5[5] == "red":
                        SEC1square6_BLUE += 2

        if Red1.colliderect(dropbox_5):
            if SEC1square6_BLUE == 8:
                SEC1square6_RED = 10

        if Blue1.colliderect(dropbox_5):
            if SEC1square6_RED == 8:
                SEC1square6_BLUE = 10

        if Red1.colliderect(dropbox_5):
            if Vert7[5] == "blue" and Vert6[5] == "blue":
                if SEC1square6_RED == 2:
                    SEC1square6_RED += 2

        if Red1.colliderect(dropbox_5) and Vert7[5] == "blue":
            SEC1square6_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert17sec2) and Vert6[5] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert17sec3) and Vert5[5] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert17sec4) and Vert4[5] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert17sec5) and Vert3[5] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_5) and Vert7[5] == "red":
            #if Vert17[5] == "SQ1":
                #SEC1square6_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert17sec2) and Vert6[5] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert17sec3) and Vert5[5] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert17sec4) and Vert4[5] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert17sec5) and Vert3[5] == "red":
            Blue1.y -= 100

    #============================square section seven ==============
    #============================square section eight ==============
        if Blue1.colliderect(dropbox_6):
            if Vert7[6] == "SQ1":
                Vert7[6] = "blue"

        if SEC1square7_RED > 10:
            SEC1square7_RED = 10

        if SEC1square7_BLUE > 10:
            SEC1square7_BLUE = 10

        if Blue1.colliderect(dropbox_6):
            SEC1square7_BLUE += 2

        if Red1.colliderect(dropbox_6):
            if Vert7[6] == "SQ1":
                Vert7[6] = "red" 

        if Red1.colliderect(dropbox_6):
            if Vert7[6] == "red":
                SEC1square7_RED += 2

        if SEC1square7_RED == 2:
            if Vert7[6] == "SQ1":
                Vert7[6] = "red"
        if SEC1square7_RED == 4:
            if Vert6[6] == "SQ1":
                Vert6[6] = "red"
        if SEC1square7_RED == 6:
            if Vert5[6] == "SQ1":
                Vert5[6] = "red"
        if SEC1square7_RED == 8:
            if Vert4[6] == "SQ1":
                Vert4[6] = "red"
        if SEC1square7_RED == 10:
            if Vert3[6] == "SQ1":
                Vert3[6] = "red"    

        if SEC1square7_BLUE == 2:
            if Vert7[6] == "SQ1":
                Vert7[6] = "blue"
        if SEC1square7_BLUE == 4:
            if Vert6[6] == "SQ1":
                Vert6[6] = "blue"
        if SEC1square7_BLUE == 6:
            if Vert5[6] == "SQ1":
                Vert5[6] = "blue"
        if SEC1square7_BLUE == 8:
            if Vert4[6] == "SQ1":
                Vert4[6] = "blue"
        if SEC1square7_BLUE == 10:
            if Vert3[6] == "SQ1":
                Vert3[6] = "blue"

        if Vert7[6] == "red" and SEC1square7_RED == 2:
            if not Vert7[6] == "blue":
                Vert7[6] = "red"
        if Vert7[6] == "red" and SEC1square7_RED == 4:
            if not Vert6[6] == "blue":
                Vert6[6] = "red"
        if Vert7[6] == "red" and SEC1square7_RED == 6:
            if not Vert5[6] == "blue":
                Vert5[6] = "red"
        if Vert7[6] == "red" and SEC1square7_RED == 8:
            if not Vert4[6] == "blue":
                Vert4[6] = "red"
        if Vert7[6] == "red" and SEC1square7_RED == 10:
            if not Vert3[6] == "blue":
                Vert3[6] = "red"

        if Vert7[6] == "blue" and SEC1square7_BLUE == 2:
            if not Vert7[6] == "red":
                Vert7[6] = "blue"
        if Vert7[6] == "blue" and SEC1square7_BLUE == 4:
            if not Vert6[6] == "red":
                Vert6[6] = "blue"
        if Vert7[6] == "blue" and SEC1square7_BLUE == 6:
            if not Vert5[6] == "red":
                Vert5[6] = "blue"
        if Vert7[6] == "blue" and SEC1square7_BLUE == 8:
            if not Vert4[6] == "red":
                Vert4[6] = "blue"
        if Vert7[6] == "blue" and SEC1square7_BLUE == 10:
            if not Vert3[6] == "red":
                Vert3[6] = "blue"


        if Vert7[6] == "red":
            pygame.draw.rect(screen,RED,Vert19sec1)
            if SEC1square7_BLUE == 0:
                SEC1square7_BLUE = 2
        if Vert6[6] == "red":
            pygame.draw.rect(screen,RED,Vert19sec2)
        if Vert5[6] == "red":
            pygame.draw.rect(screen,RED,Vert19sec3)
        if Vert4[6] == "red":
            pygame.draw.rect(screen,RED,Vert19sec4)
        if Vert3[6] == "red":
            pygame.draw.rect(screen,RED,Vert19sec5)


        if Vert7[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec1)
            if SEC1square7_RED == 0:
                SEC1square7_RED = 2
        if Vert6[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec2)
        if Vert5[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec3)
        if Vert4[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec4)
        if Vert3[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec5)
        if Vert2[6] == "blue":
            pygame.draw.rect(screen,BLUE,Vert19sec6)

        if Blue1.colliderect(dropbox_6):
            if Vert5[6] == "SQ1":
                if SEC1square7_RED == 4:
                    SEC1square7_BLUE = 6

        if Red1.colliderect(dropbox_6):
            if SEC1square7_RED == 6:
                if Vert5[6] == "blue":
                    if Vert7[6] == "red":
                        if Vert6[6] == "blue":
                            SEC1square7_RED += 2

             #new       
        if Red1.colliderect(dropbox_6):
            if SEC1square7_BLUE == 6:
                if Vert6[6] == "red":
                    if Vert7[6] == "blue":
                        SEC1square7_RED += 2

               #new         
        if Red1.colliderect(dropbox_6):
            if SEC1square7_RED == 6:
                if Vert7[6] == "red":
                    if Vert6[6] == "red":
                        if Vert5[6] == "blue":
                            SEC1square7_RED += 2

        #new
        if Red1.colliderect(dropbox_6):
            if SEC1square7_BLUE == 6:
                if Vert7[6] == "blue":
                    if Vert6[6] == "blue":
                        if Vert5[6] == "blue":
                            SEC1square7_RED += 4

        if Vert3[6] == "red":
            if Vert4[6] == "SQ1":
                SEC1square7_RED -= 2
                Vert3[6] = "SQ1"


            #new
        if Red1.colliderect(dropbox_6):
            if Vert7[6] == "red":
                if Vert6[6] == "blue":
                    if Vert5[6] == "blue":
                        SEC1square7_RED += 4


        if Blue1.colliderect(dropbox_6):
            if SEC1square7_BLUE == 4:
                if Vert5[6] == "red":
                    SEC1square7_BLUE += 4

        if Red1.colliderect(dropbox_6):
            if Vert4[6] == "SQ1":
                if SEC1square7_BLUE == 4:
                    if Vert6[6] == "blue":
                        SEC1square7_RED += 2

                    #new
        if Blue1.colliderect(dropbox_6):
            if Vert6[6] == "blue":
                if SEC1square7_RED == 6:
                    if Vert5[6] == "red":
                        SEC1square7_BLUE += 2

        if Red1.colliderect(dropbox_6):
            if SEC1square7_BLUE == 8:
                SEC1square7_RED = 10

        if Blue1.colliderect(dropbox_6):
            if SEC1square7_RED == 8:
                SEC1square7_BLUE = 10

        if Red1.colliderect(dropbox_6):
            if Vert7[6] == "blue" and Vert6[6] == "blue":
                if SEC1square7_RED == 2:
                    SEC1square7_RED += 2

        if Red1.colliderect(dropbox_6) and Vert7[6] == "blue":
            SEC1square7_RED += 2
            Red1.y -= 100
        if Red1.colliderect(Vert19sec2) and Vert6[6] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert19sec3) and Vert5[6] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert19sec4) and Vert4[6] == "blue":
            Red1.y -= 100
        if Red1.colliderect(Vert19sec5) and Vert3[6] == "blue":
            Red1.y -= 100


        #if Blue1.colliderect(dropbox_6) and Vert7[6] == "red":
            #if Vert19[6] == "SQ1":
                #SEC1square7_BLUE += 2
            #Blue1.y -= 100
        if Blue1.colliderect(Vert19sec2) and Vert6[6] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert19sec3) and Vert5[6] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert19sec4) and Vert4[6] == "red":
            Blue1.y -= 100
        if Blue1.colliderect(Vert19sec5) and Vert3[6] == "red":
            Blue1.y -= 100



        if Bluerect == True:
            pygame.draw.rect(screen,(BLUE),Blue1, 7)

        if Redrect == True:
            pygame.draw.rect(screen,(RED),Red1)

        resetTxT = pygame.freetype.Font("Asset-Regular.ttf")
        resetTxT_text = pygame.freetype.Font("Asset-Regular.ttf")

        dash_board1 = pygame.freetype.Font("Asset-Regular.ttf")
        dash_board1_text = pygame.freetype.Font("Asset-Regular.ttf")

        dash_board2 = pygame.freetype.Font("Asset-Regular.ttf")
        dash_board2_text = pygame.freetype.Font("Asset-Regular.ttf")

        dash_board3 = pygame.freetype.Font("Asset-Regular.ttf")
        dash_board3_text = pygame.freetype.Font("Asset-Regular.ttf")

        winner_decider = pygame.freetype.Font("Asset-Regular.ttf")
        winner_decider_text = pygame.freetype.Font("Asset-Regular.ttf")

        dash_board1.origin = True
        dash_board1.size = 16
        dash_board1_left = 246
        dash_board1_bottom = 690 
        dash_board1.fgcolor = (pc)
        d1 = dash_board1.get_rect("center me")
        dash_board1.render_to(screen, (dash_board1_left, dash_board1_bottom), score)
        dash_board1_text.size = 20
        dash_board1_text_left = 5
        dash_board1_text_bottom = 690
        dash_board1_text.fgcolor = color_list[color]
        t1 = dash_board1_text.get_rect("center me")
        dash_board1_text.origin = True

        dash_board1_text.render_to(screen, (dash_board1_text_left, dash_board1_text_bottom),"|𝕐=𝕆=𝕌==ℍ=𝔸=𝕍=𝔼|=|   |=/===𝕎=𝕀=ℕ=𝕊/!.!.!\====/",)

        dash_board2.origin = True
        dash_board2.size = 15
        dash_board2_left = 325
        dash_board2_bottom = 630 
        dash_board2.fgcolor = (pc)
        d2 = dash_board2.get_rect("center me")
        dash_board2.render_to(screen, (dash_board2_left, dash_board2_bottom), First_player)
        dash_board2_text.size = 22
        dash_board2_text_left = 400 
        dash_board2_text_bottom = 630 
        dash_board2_text.fgcolor = color_list[color]
        t2 = dash_board2_text.get_rect("center me")
        dash_board2_text.origin = True
        dash_board2_text.render_to(screen, (dash_board2_text_left,dash_board2_text_bottom),"<=𝕀𝕊==𝔽𝕀ℝ𝕊𝕋==ℙ𝕃𝔸𝕐𝔼ℝ=]",)


        dash_board3.origin = True
        dash_board3.size = 15
        dash_board3_left = 610
        dash_board3_bottom = 690 
        dash_board3.fgcolor = (pc)
        d3 = dash_board3.get_rect("center me")
        dash_board3.render_to(screen, (dash_board3_left, dash_board3_bottom), placed)
        dash_board3_text.size = 20
        dash_board3_text_left = 0 
        dash_board3_text_bottom = 630 
        dash_board3_text.fgcolor = color_list[color]
        t3 = dash_board3_text.get_rect("center me")
        dash_board3_text.origin = True
        dash_board3_text.render_to(screen, (dash_board3_text_left,dash_board3_text_bottom),"<==𝕕𝕒𝕥𝕖/ 𝟙 / 𝟙 / 𝟚𝟘𝟚𝟝 /==>",)




        if WINS == 1:
            resetTxT.origin = True
            resetTxT.size = 35
            resetTxT_left = 1
            resetTxT_bottom = 350
            resetTxT.fgcolor = color_list[3]
            d5 = resetTxT.get_rect("center me")
            resetTxT.render_to(screen, (resetTxT_left, resetTxT_bottom), "WINS ROUND ONE")
            resetTxT_text.origin = True
            resetTxT_text.size = 45
            resetTxT_text_left = 260
            resetTxT_text_bottom = 390
            resetTxT_text.fgcolor = color_list[color]
            t6 = resetTxT_text.get_rect("center me")
            resetTxT_text.render_to(screen, (resetTxT_text_left, resetTxT_text_bottom), round_winner)
            loading_screen_image = pygame.Rect(int(-40),10,int(790/1),700)
            pygame.draw.ellipse(screen,BLACK,loading_screen_image,loading_screen)
            loading_screen_image2 = pygame.Rect(int(-120),10,int(820/1),700)
            pygame.draw.rect(screen,color_list[color],loading_screen_image,loading_screen)
            Vert1 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert2 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert3 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert4 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert5 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert6 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert7 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
        #=======================restart game====================================        
            SEC1square1_RED = 0
            SEC1square2_RED = 0
            SEC1square3_RED = 0
            SEC1square4_RED = 0
            SEC1square5_RED = 0
            SEC1square6_RED = 0
            SEC1square7_RED = 0
        #=======================restart game====================================        
            SEC2square1_RED = 0
            SEC2square2_RED = 0
            SEC2square3_RED = 0
            SEC2square4_RED = 0
            SEC2square5_RED = 0
            SEC2square6_RED = 0
            SEC2square7_RED = 0
        #=======================restart game====================================        
            SEC3square1_RED = False
            SEC3square2_RED = False
            SEC3square3_RED = False
            SEC3square4_RED = False
            SEC3square5_RED = False
            SEC3square6_RED = False
            SEC3square7_RED = False    
        #=======================restart game====================================        
            SEC1square1_BLUE = 0
            SEC1square2_BLUE = 0
            SEC1square3_BLUE = 0
            SEC1square4_BLUE = 0
            SEC1square5_BLUE = 0
            SEC1square6_BLUE = 0
            SEC1square7_BLUE = 0
        #=======================restart game====================================        
            SEC2square1_BLUE = 0
            SEC2square2_BLUE = 0
            SEC2square3_BLUE = 0
            SEC2square4_BLUE = 0
            SEC2square5_BLUE = 0
            SEC2square6_BLUE = 0
            SEC2square7_BLUE = 0
        #=======================restart game====================================        
            SEC3square1_BLUE = False
            SEC3square2_BLUE = False
            SEC3square3_BLUE = False
            SEC3square4_BLUE = False
            SEC3square5_BLUE = False
            SEC3square6_BLUE = False
            SEC3square7_BLUE = False 
            #=======================restart game====================================
        if keys[pygame.K_1] and WINS == 1:
            loading_screen -= 100
            if loading_screen < 100:
                score = str(WINS - 1)
                WINS += 1
                loading_screen = 100




        if WINS == 3:
            resetTxT.origin = True
            resetTxT.size = 35
            resetTxT_left = 1
            resetTxT_bottom = 350
            resetTxT.fgcolor = color_list[3]
            d5 = resetTxT.get_rect("center me")
            resetTxT.render_to(screen, (resetTxT_left, resetTxT_bottom), "WINS ROUND TWO")
            resetTxT_text.origin = True
            resetTxT_text.size = 45
            resetTxT_text_left = 260
            resetTxT_text_bottom = 390
            resetTxT_text.fgcolor = color_list[color]
            t6 = resetTxT_text.get_rect("center me")
            resetTxT_text.render_to(screen, (resetTxT_text_left, resetTxT_text_bottom), round_winner)
            loading_screen_image = pygame.Rect(int(-40),10,int(790/1),700)
            pygame.draw.ellipse(screen,BLACK,loading_screen_image,loading_screen)
            loading_screen_image2 = pygame.Rect(int(-120),10,int(820/1),700)
            pygame.draw.rect(screen,color_list[color],loading_screen_image,loading_screen)
            Vert1 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert2 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert3 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert4 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert5 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert6 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert7 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
        #=======================restart game====================================        
            SEC1square1_RED = 0
            SEC1square2_RED = 0
            SEC1square3_RED = 0
            SEC1square4_RED = 0
            SEC1square5_RED = 0
            SEC1square6_RED = 0
            SEC1square7_RED = 0
        #=======================restart game====================================        
            SEC2square1_RED = 0
            SEC2square2_RED = 0
            SEC2square3_RED = 0
            SEC2square4_RED = 0
            SEC2square5_RED = 0
            SEC2square6_RED = 0
            SEC2square7_RED = 0
        #=======================restart game====================================        
            SEC3square1_RED = False
            SEC3square2_RED = False
            SEC3square3_RED = False
            SEC3square4_RED = False
            SEC3square5_RED = False
            SEC3square6_RED = False
            SEC3square7_RED = False    
        #=======================restart game====================================        
            SEC1square1_BLUE = 0
            SEC1square2_BLUE = 0
            SEC1square3_BLUE = 0
            SEC1square4_BLUE = 0
            SEC1square5_BLUE = 0
            SEC1square6_BLUE = 0
            SEC1square7_BLUE = 0
        #=======================restart game====================================        
            SEC2square1_BLUE = 0
            SEC2square2_BLUE = 0
            SEC2square3_BLUE = 0
            SEC2square4_BLUE = 0
            SEC2square5_BLUE = 0
            SEC2square6_BLUE = 0
            SEC2square7_BLUE = 0
        #=======================restart game====================================        
            SEC3square1_BLUE = False
            SEC3square2_BLUE = False
            SEC3square3_BLUE = False
            SEC3square4_BLUE = False
            SEC3square5_BLUE = False
            SEC3square6_BLUE = False
            SEC3square7_BLUE = False 
            #=======================restart game====================================()
        if keys[pygame.K_3] and WINS == 3:
            loading_screen -= 100
            if loading_screen < 100:
                score = str(WINS - 1)
                WINS += 1
                loading_screen = 100

        if WINS == 6:
            WINS += 1
            score = str(WINS - 1)
            Vert1 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert2 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert3 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert4 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert5 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert6 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
            Vert7 = ["SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1", "SQ1"]
        #=======================restart game====================================        
            SEC1square1_RED = 0
            SEC1square2_RED = 0
            SEC1square3_RED = 0
            SEC1square4_RED = 0
            SEC1square5_RED = 0
            SEC1square6_RED = 0
            SEC1square7_RED = 0
        #=======================restart game====================================        
            SEC2square1_RED = 0
            SEC2square2_RED = 0
            SEC2square3_RED = 0
            SEC2square4_RED = 0
            SEC2square5_RED = 0
            SEC2square6_RED = 0
            SEC2square7_RED = 0
        #=======================restart game====================================        
            SEC3square1_RED = False
            SEC3square2_RED = False
            SEC3square3_RED = False
            SEC3square4_RED = False
            SEC3square5_RED = False
            SEC3square6_RED = False
            SEC3square7_RED = False    
        #=======================restart game====================================        
            SEC1square1_BLUE = 0
            SEC1square2_BLUE = 0
            SEC1square3_BLUE = 0
            SEC1square4_BLUE = 0
            SEC1square5_BLUE = 0
            SEC1square6_BLUE = 0
            SEC1square7_BLUE = 0
        #=======================restart game====================================        
            SEC2square1_BLUE = 0
            SEC2square2_BLUE = 0
            SEC2square3_BLUE = 0
            SEC2square4_BLUE = 0
            SEC2square5_BLUE = 0
            SEC2square6_BLUE = 0
            SEC2square7_BLUE = 0
        #=======================restart game====================================        
            SEC3square1_BLUE = False
            SEC3square2_BLUE = False
            SEC3square3_BLUE = False
            SEC3square4_BLUE = False
            SEC3square5_BLUE = False
            SEC3square6_BLUE = False
            SEC3square7_BLUE = False 
            #=======================restart game====================================()

        def winner():
            winner_decider.origin = True
            winner_decider.size = 40
            winner_decider_left = 100
            winner_decider_bottom = 70
            winner_decider.fgcolor = (pc)
            d4 = winner_decider.get_rect("center me")
            winner_decider.render_to(screen, (winner_decider_left, winner_decider_bottom), game_winner)

            winner_decider_text.origin = True
            winner_decider_text.size = 40
            winner_decider_text_left = 300 
            winner_decider_text_bottom = 70 
            winner_decider_text.fgcolor = color_list[color]
            d4 = winner_decider_text.get_rect("center me")
            winner_decider.render_to(screen, (winner_decider_text_left, winner_decider_text_bottom), "WINNNS")



        if WINS == 7:
            winner()
            for i in range(100):
                if i == 99:
                    break


        #return First_player,score,WINS

       #consist of five arguements,the screen the rect will be on. rgb the colors, wich consist of red blue and green . and the rect itself 






        pygame.display.flip()

pygame.init()

