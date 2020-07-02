import pygame
import time
import random
pygame.init()
blue = (0,0,255)
red=(255,0,0)
green=(0,255,0)
v=10
x1=400
y1=300
x1_changed=0
y1_changed=0
snake_width=10
snake_height=10
snake_length=1
food_width=10
food_height=10
food_x=200
food_y=300
dis=pygame.display.set_mode((800,600))
pygame.display.update()
font_obj=pygame.font.SysFont(None,50)
direction=''
snake_body=[]
def snakemove(snakebody,snake_width):
    for x in snake_body:
        pygame.draw.rect(dis,blue,[x[0],x[1],snake_width,snake_height])
def message(msg,color):
    #game_over=False
    msg_obj=font_obj.render(msg,True,red)
    dis.blit(msg_obj,[width_limit/2,height_limit/2])
def score(msg,color):
    msg_obj=font_obj.render("Your score"+str(msg),True,red)
    dis.blit(msg_obj,[5,5])
snake_list1=[]

width_limit=800
height_limit=600
pygame.display.set_caption("snake game")
game_over=True
clock=pygame.time.Clock()
pygame.display.update()
while game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction!='down':
                y1_changed=-v
                x1_changed=0
                direction='Up'
            elif event.key==pygame.K_DOWN and direction!='Up':
                y1_changed= v
                x1_changed = 0
                direction='down'
            elif event.key==pygame.K_LEFT and direction!='right':
                x1_changed=-v
                y1_changed=0
                direction='left'
            elif event.key==pygame.K_RIGHT and direction!='left':
                x1_changed=v
                y1_changed=0
                direction='right'
    if x1>=width_limit or x1<=0 or y1>=height_limit or y1<=0:
        message("you lost", red)
        game_over=False

    x1+=x1_changed
    y1+=y1_changed
    dis.fill((255,255,255))
    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)
    if len(snake_body)>snake_length:
        del snake_body[0]
    for x in snake_body[:-1]:
        if x==snake_head:
            message("you lost", red)
            game_over=False
    snakemove(snake_body,snake_width)


    if x1 == food_x and y1 == food_y:
        snake_length+=1
        food_x=random.randrange(0,750,10)
        food_y=random.randrange(0,600,10)

    #dis.fill((255,255,255))
    pygame.draw.rect(dis, green, [food_x,food_y, food_width, food_height])
    #pygame.draw.rect(dis, blue, [x1,y1,snake_width,snake_height])
    #dis.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(15)
score(snake_length-1,red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()