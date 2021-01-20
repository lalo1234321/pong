from vpython import *
from threading import Timer

import random
import vlc

# Configuraciones de la musica
music = "/home/theowl/Documents/music/projects/game.mp3"
music1 = "/home/theowl/Documents/music/projects/gamePart2.mp3"
shot = "/home/theowl/Documents/music/projects/shot.mp3"
border = "/home/theowl/Documents/music/projects/borderSound.mp3"
win = "/home/theowl/Documents/music/projects/win.mp3"
# Iniciando con la primera cancion
p = vlc.MediaPlayer(music)
p.play()


playAgain = False
def twoArgs(arg1,arg2):
    print (arg1)
    pSecond = vlc.MediaPlayer(arg2)
    pSecond.play()
    p.stop()

r = Timer(77.0,twoArgs,("ejecutando",music1))
r.start()





#toda la documetación en glowscript
scene.range = 4
my_sphere = sphere(pos = vector(0,0,0), radius = 0.25, texture=textures.earth)
wall1 = box(pos = vector(4,0,0), size = vector(0.1,1,1), texture=textures.metal)
wall2 = box(pos = vector(-4,0,0), size = vector(0.1,1,1), texture=textures.metal)

backWall = box(pos = vector(0,0,-3),size = vector(19,12,1), texture=textures.wood)
# topWall = box(pos = vector(0,3,))

# for animate an object you need a loop
score1 = 0
score2 = 0
time = 0 #Time in the simulation
dt = 0.091#Time step size
T = text(text='Pong game',pos=vector(-2.9,2,0), color=color.red)
scorePlayer1 = text(text=str(score1),pos=vector(-4.9,2,0), color=color.orange)
scorePlayer2 = text(text=str(score2),pos=vector(4.9,2,0), color=color.purple)
#Configuration for the key events
v = vec(0,0,0)
dw = 0.2
dz = 0.1
v1 = vec(0,0,0)
dw1 = 0.2
dz1 = 0.1
# while True:
#     rate(30)
#     k = keysdown() # a list of keys that are down
#     # if 'left' in k: v.x -= dv
#     # if 'right' in k: v.x += dv
#     if 'down' in k: v.y -= dw
#     if 'up' in k: v.y += dw
#     wall2.pos += v*dz

collided1 = False
collided2 = False
initialState = True
rebound = 0
valuesForRebound = [.01,-.01,0,.03,-.03,.05,-.05]

def mainGame():
    global time, my_sphere, dt, v, dw, dw1, wall1, wall2, collided1, collided2, shot
    global rebound, initialState, score1, scorePlayer1, score2, scorePlayer2
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
            p.stop()
            p3 = vlc.MediaPlayer(win)
            p3.play()
            tWin = text(text='You have won',pos=vector(-3,0,0), color=color.red)
            score1 = 0
            score2 = 0
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


mainGame()