import pygame
import random
import os
from pygame import mixer
x = pygame.init()

# mixer.init()
# mixer.music.load('background.mp3')
# mixer.music.play()
gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("Saanp aaya")
pygame.display.update()

DIR = os.path.dirname(os.path.realpath(__file__))
# bgimage = pygame.transform.scale( pygame.image.load(os.path.join(DIR,'background2.jpg')), (1200,500))
mixer.init()



# bgimage = pygame.transform.scale(bgimage,(1200,500)).convert_alpha()

#game title ,size

pygame.display.update()

#colors
white = (255,255,255)
black = (0,0,0)
rand1 = (231,24,5)



#game variables

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,(x,y))

def snakeprint(gamewindow,color,snakepos,snake_height):
    for i  in range(len(snakepos)):
         pygame.draw.rect(gamewindow,white,[snakepos[i][0],snakepos[i][1],snake_height,snake_height])




#events
def gameloop():
    mixer.music.load(os.path.join(DIR,'background.mp3'))
    mixer.music.play()
    snake_x = 50
    snake_y = 50
    snake_height = 25
    snake_length = 1
    fps = 10
    velocity_x = 0
    velocity_y = 0
    food_size = 25
    food_x = random.randint(0,1200//2)
    food_y = random.randint(20,500//2)
    score = 1
    snake_pos= []
    head = [snake_x,snake_y]
    snake_pos.append([snake_x,snake_y])
    exit_game = False
    game_over = False
    while not exit_game:
       
        if game_over:
            gamewindow.fill(white)
            if score*10  > 200:
             gamewindow.fill(black)   
             text_screen("Game over !!  Press space to restart",rand1,300,150)
             text_screen("    Score = "+str(score*10),rand1,470,200)
             text_screen(" Yeahhhh great",rand1,370,250)
            else:
                gamewindow.fill(black)
                text_screen("Game over !!  Press space to restart",rand1,300,150)
                text_screen("    Score = "+str(score*10),rand1,470,200)
                text_screen(" You should practice more ",rand1,400,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()    

        else:   
            speed = 0.5
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -speed
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = speed

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10: 
                snake_length = snake_length + 15
                score = score + 1
                speed = speed + score * 0.1
                food_x = random.randint(0,1200//2)
                food_y = random.randint(20,500//2)
            if [snake_x,snake_y] in snake_pos[:-1]:
                game_over = True 
                pygame.mixer.music.load(os.path.join(DIR,'gameover.mp3'))
                pygame.mixer.music.play()   
                
            snake_pos.append([snake_x,snake_y])   
            if len(snake_pos) > snake_length:
                snake_pos.pop(0)

            if snake_x < 0  or snake_y < 0 or snake_x > 1200 or snake_y > 500:
                game_over = True 
                pygame.mixer.music.load(os.path.join(DIR,'gameover.mp3'))
                pygame.mixer.music.play()    
             
        
            gamewindow.fill(white)
            gamewindow.fill((0,0,0))
            text_screen("Score" + str(score*10),rand1,5,5)
            pygame.draw.rect(gamewindow,rand1,[food_x,food_y,food_size,food_size])
            snakeprint(gamewindow,black,snake_pos,snake_height)  
        # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_width,snake_height])
        pygame.display.update()
    pygame.quit()
    quit()
gameloop()