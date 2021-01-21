from vpython import *
from threading import Timer

import random
import vlc

# Configuraciones de la musica
music = "./projects/game.mp3"
music1 = "./projects/gamePart2.mp3"
music2 = "./projects/gamePart3.mp3"
music3 = "./projects/gamePart4.mp3"
shot = "./projects/shot.mp3"
border = "./projects/borderSound.mp3"
win = "./projects/win.mp3"
# Iniciando con la primera cancion
p = vlc.MediaPlayer(music1)
p.play()
musicList = [music,music2, music3]

playAgain = False
# def twoArgs(arg1,arg2):
#     print (arg1)
#     pSecond = vlc.MediaPlayer(arg2)
#     pSecond.play()
#     p.stop()

# r = Timer(77.0,twoArgs,("ejecutando",music1))
# r.start()





#toda la documetación en glowscript

# topWall = box(pos = vector(0,3,))

# for animate an object you need a loop

#Configuration for the key events

# while True:
#     rate(30)
#     k = keysdown() # a list of keys that are down
#     # if 'left' in k: v.x -= dv
#     # if 'right' in k: v.x += dv
#     if 'down' in k: v.y -= dw
#     if 'up' in k: v.y += dw
#     wall2.pos += v*dz
scene.range = 4
my_sphere = sphere(pos = vector(0,0,0), radius = 0.25, texture=textures.earth, visible = False)
wall1 = box(pos = vector(4,0,0), size = vector(0.1,1,1), texture=textures.metal, visible = False)
wall2 = box(pos = vector(-4,0,0), size = vector(0.1,1,1), texture=textures.metal, visible = False)
score1 = 0
score2 = 0

dt = 0.091#Time step size
v = vec(0,0,0)
dw = 0.2
dz = 0.1
v1 = vec(0,0,0)
dw1 = 0.2
dz1 = 0.1
collided1 = False
collided2 = False
initialState = True
rebound = 0
valuesForRebound = [.01,-.01,0,.03,-.03,.05,-.05]
def printing():
    global tAbout, tLastNAme, tMove, tPlayer1, tPlayer2, tWin, T
    tAbout.visible = True
    tLastNAme.visible = True
    tMove.visible = False
    tPlayer1.visible = False
    tPlayer2.visible = False
    tWin.visible = False
    T.visible = False

def instructions():
    global tAbout, tLastNAme, tMove, tPlayer1, tPlayer2, tWin,T
    tAbout.visible = False
    tLastNAme.visible = False
    tMove.visible = True
    tPlayer1.visible = True
    tPlayer2.visible = True
    tWin.visible = False
    T.visible = False

def playGame():
    global tAbout, tLastNAme, tMove, tPlayer1, tPlayer2, T, scorePlayer1, scorePlayer2
    global bAbout, bInstructions, bPlay, scorePlayer1, scorePlayer2, T
    global my_sphere, wall1, wall2, tWin, p
    p.stop()
    p1 = vlc.MediaPlayer(random.choice(musicList))
    p1.play()
    resetValues()
    tWin.visible = False
    tAbout.visible = False
    tLastNAme.visible = False
    tMove.visible = False
    tPlayer1.visible = False
    tPlayer2.visible = False
    T.visible = True
    scorePlayer1.visible = True
    scorePlayer2.visible = True
    bAbout.disabled = True
    bInstructions.disabled = True 
    bPlay.disabled = True
    scorePlayer1.visible = True
    scorePlayer2.visible = True
    T.visible = True
    wall1.visible = True
    wall2.visible = True
    my_sphere.visible = True
    mainGame(p1)


tWin = text(text='You have won',pos=vector(-3.4,0,0), color=color.red, visible = False)
tMove = text(text = "Move with:", pos = vector(-3,3,-1),visible = False)
tPlayer1 = text(text = "Player 1: W  S",pos = vector(-3,1,-1), visible = False)
tPlayer2 = text(text = "Player 2: upKey \ndownKey", pos = vector(-6,-1,-1), visible = False)
tAbout = text(text = "Developed by:\nEduardo Domínguez", pos = vector(-4.4, 2, -1.8),visible = False)
tLastNAme = text(text = "Cordero", pos = vector(-4.4,-1,-1.8), visible = False)
backWall = box(pos = vector(0,0,-3),size = vector(19,12,1), texture=textures.wood)
T = text(text='Pong game',pos=vector(-2.9,2,0), color=color.red, visible = False)
scorePlayer1 = text(text=str(score1),pos=vector(-4.9,2,0), color=color.orange, visible = False)
scorePlayer2 = text(text=str(score2),pos=vector(4.9,2,0), color=color.purple, visible = False)
bAbout = button(text = "About",pos = scene.title_anchor, bind = printing)
bInstructions = button(text = "How to play",pos = scene.title_anchor, bind = instructions)
bPlay = button(text = "Play",pos = scene.title_anchor, bind = playGame)
time = 0 #Time in the simulation



def resetValues():
    global score1, score2, dt, v, v1, dw, dw1, dz1, dz, collided1, collided2
    global initialState, rebound, time
    score1 = 0
    score2 = 0
    dt = 0.091#Time step size
    v = vec(0,0,0)
    dw = 0.2
    dz = 0.1
    v1 = vec(0,0,0)
    dw1 = 0.2
    dz1 = 0.1
    collided1 = False
    collided2 = False
    initialState = True
    rebound = 0
    time = 0 #Time in the simulation

def constructorMainGame():
    global scorePlayer1, scorePlayer2, T
    # scorePlayer1.visible = False
    # scorePlayer2.visible = False
    # T.visible = False
    play = False
    bAbout.visible = True
    bInstructions.visible = True


def mainGame(gameMusic):
    global time, my_sphere, dt, v, dw, dw1, wall1, wall2, collided1, collided2, shot
    global rebound, initialState, score1, scorePlayer1, score2, scorePlayer2
    global bAbout, bInstructions, bPlay, tWin
    # rate control de fps
    while(time<=1000):
        rate(50)
        # if( my_sphere.pos.x>=2 ):
        #     dt = -dt

        # if( my_sphere.pos.x<=-2 ):
        #     dt = -dt
        # print(wall1.pos.y)
        my_sphere.pos.x = my_sphere.pos.x + dt
        if not initialState:
            my_sphere.pos.y+=rebound




        
        # my_sphere.pos.x = my_sphere.pos.x + dx
        time = time + dt
        

        rate(30)
        k = keysdown() # a list of keys that are down
        # if 'left' in  k: v1.y -= dw1
        # if 'right' in k: v1.y += dw1
        if 'down' in k: v.y -= dw
        if 'up' in k: v.y += dw
        if 's' in k: v1.y -= dw1
        if 'w' in k: v1.y += dw1

        wall2.pos += v*dz
        wall1.pos += v1*dz1
        distance_x1 = abs(wall2.pos.x-my_sphere.pos.x)
        distance_y1 = abs(wall2.pos.y-my_sphere.pos.y)
        collided1 = (distance_x1 < (wall2.size.x+my_sphere.size.x)/2 and distance_y1 < (wall2.size.y+my_sphere.size.y)/2)

        distance_x2 = abs(wall1.pos.x-my_sphere.pos.x)
        distance_y2 = abs(wall1.pos.y-my_sphere.pos.y)
        collided2 = (distance_x2 < (wall1.size.x+my_sphere.size.x)/2 and distance_y2 < (wall1.size.y+my_sphere.size.y)/2)
        
        if collided1:
            
            p1 = vlc.MediaPlayer(shot)
            p1.play()
            print('Collided ', ' x = ',wall1.pos.x,' y = ',wall1.pos.y)
            rebound = random.choice(valuesForRebound)
            print(rebound)
            dt = -dt
            initialState = False
            collided2 = False
        
        elif collided2:
            p1 = vlc.MediaPlayer(shot)
            p1.play()
            print('Collided2')
            dt = -dt
            collided1 = False
        elif my_sphere.pos.y>3:
            p2 = vlc.MediaPlayer(border)
            p2.play()
            print('dentro1')
            rebound = -rebound
        elif my_sphere.pos.y<-3:
            p2 = vlc.MediaPlayer(border)
            p2.play()
            rebound = -rebound
            print('dentro2')

        elif my_sphere.pos.x<-4.9:
            score1 +=1
            scorePlayer1.visible = False
            scorePlayer1 = text(text=str(score1),pos=vector(-4.9,2,0), color=color.orange)
            my_sphere.pos.x=0
        elif my_sphere.pos.x>4.9:
            score2 +=1
            scorePlayer2.visible = False
            scorePlayer2 = text(text=str(score2),pos=vector(4.9,2,0), color=color.purple)
            my_sphere.pos.x=0
        elif score1==3 or score2==3:
            gameMusic.stop()
            p.stop()
            p3 = vlc.MediaPlayer(win)
            p3.play()
            tWin.visible = True
            bAbout.disabled = False
            bInstructions.disabled = False 
            bPlay.disabled = False
            bPlay.text = "Play again"
            playAgain = True
            break
        elif wall1.pos.y<-2.9:
            wall1.pos.y = -2.7
        elif wall2.pos.y<-2.9:
            wall2.pos.y = -2.7
        elif wall1.pos.y>2.9:
            wall1.pos.y = 2.7
        elif wall2.pos.y>2.9:
            wall2.pos.y = 2.7
        else:
            dt = dt

mainGameVisible = False

def menuGame():
    tWelcome = Text()


constructorMainGame()
