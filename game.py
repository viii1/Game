import pygame
import random
import math

#initialize the pygame
pygame.init()
#create the screen
screen=pygame.display.set_mode((800,600))

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
enemyImage = pygame.image.load('enemy.png')
enemyX=random.randint(0,736)
enemyY=random.randint(10,150)
enemyX_change = 2
enemyY_change = 30

#bullet
#In ready state you cannot see the bullet
#in fire sate the bullet is currently moving
bulletImage = pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

score=0
def enemy(x,y):
    screen.blit(enemyImage,(x,y))


def player(x,y):
    screen.blit(playerImage,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImage,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+(math.pow(enemyY-bulletY,2)))
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
    enemyX +=enemyX_change
    if enemyX <=0:
        enemyX_change =2
        enemyY +=enemyY_change
    if enemyX >=736:
        enemyX_change = -2
        enemyY +=enemyY_change


    #bullet movement 
    if bulletY <=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change

    #collision
    #collision=isCollision(enemyX,enemyY,bulletX,bulletY)
    #if collision:
    #    bulletY=480
    #   bullet_state="ready"
    #   score+=1

    enemy(enemyX,enemyY)
    player( playerX,playerY)

    pygame.display.update()
