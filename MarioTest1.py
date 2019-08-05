import pygame
import time
import random

pygame.init()

display_width=800
display_height=600
mario_width=30
mario_height=45

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SUPER MARIO")

black=(0,0,0)
white=(255,255,255)

img_mario=pygame.image.load("mario.png")
img_mario=pygame.transform.scale(img_mario,(mario_width,mario_height))
img_ground=pygame.image.load("ground.jpg")
img_ground=pygame.transform.scale(img_ground,(800,600))
img_sky=pygame.image.load("sky.png")
img_sky=pygame.transform.scale(img_sky,(800,600))

clock=pygame.time.Clock()

def mario(x,y):
    gameDisplay.blit(img_mario,(x,y))
def ground(a,b):
    gameDisplay.blit(img_ground,(a,b))
def sky(m,n):
    gameDisplay.blit(img_sky,(m,n))
    
a=(display_width*0)
b=(display_height*0.878)

m=(display_width*0)
n=(display_height*0)


mario_speed=0


def game_loop():
    
    gameExit=False
    x=(display_width*0.2)
    y=(display_height*0.8)
    x_change=0
    y_change=0

    

    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    x_change=5
                elif event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_UP:
                    y_change=-5
            
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT: 
                    x_change=0
                if event.key==pygame.K_UP:
                    y_change=5
                    
                    
        x+=x_change
        y+=y_change
    

        gameDisplay.fill(white)

        

        sky(m,n)
        ground(a,b)
        mario(x,y)

        if x<0.2:
            x_change=0
        if y>(display_height -mario_height)-80 or y<2:
            y_change=0

        
                        
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
