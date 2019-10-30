import pygame
import random
import math
from pygame import mixer

#initialize the pygame
pygame.init()
#create the screen
screen=pygame.display.set_mode((800,600))

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('l.png')
pygame.display.set_icon(icon)

#Player
playerImage = pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change = 0

#enemy
enemyImage = []
enemyX = []
enemyY = []
enemyX_change= []
enemyY_change= []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(10,150))
    enemyX_change.append(2)
    enemyY_change.append(3)

#bullet
#In ready state you cannot see the bullet
#in fire sate the bullet is currently moving
bulletImage = pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',25)

textX=10
textY=10

def show_score(x,y):
    score=font.render("SCORE:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y))


def player(x,y):
    screen.blit(playerImage,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImage,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27 :
        return True
    else:
        return False


#game loop

running = True

while running:

    #RGB - Red Green Blue (0-255) should be above all--
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


         #if the keystoke is pressed check its right or left
        if event.type == pygame.KEYDOWN: #pressing any key is keydown
            print("A keystroke is presssed")
            if event.key == pygame.K_LEFT:
                playerX_change = -4

            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change = 0

    

    #player function under while loop
    playerX +=playerX_change
    if playerX <=0:
        playerX =0
    if playerX >=736:
        playerX = 736

    #enemy function
    for i in range(num_of_enemies):
        enemyX[i] +=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i] =2
            enemyY[i] +=enemyY_change[i]
        if enemyX[i] >=736:
            enemyX_change[i] = -2
            enemyY[i] +=enemyY_change[i]

        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(10, 150)

        enemy(enemyX[i],enemyY[i],i)
    

        
        


    #bullet movement 
    if bulletY <=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change




    player( playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
