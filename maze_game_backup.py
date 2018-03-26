# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (6, 66, 163)

#font
MY_FONT = pygame.font.Font(None, 50)

# stages
START = 0
PLAYING = 1
END = 2
stage = START 

# Make a player
#player =  [725, 475, 25, 25]
vel = [0, 0]
player_speed = 5
score1 = 0
socre2 = 0 

# make walls
wall1 = [600, 100, 25, 25]

walls = [wall1] 

# Make coins 


 

'''def make_red_blocks():
    global red_blocks
    red_block = []
    for i in range (0):
        x = (random.randrange(300, 600)) 
        y = random.randrange(25, 250)
        red_block = [x, y, 30, 30, False]

        red_blocks.append(red_block)

make_red_blocks()''' 

def add_red_blocks(x, y, w, h): 
    global red_blocks 
    red_blocks = []
    for r in red_blocks:
        x = rx_loc 
        y = ry_loc
        red_block = [x, y, 30, 30, False]

        red_blocks.append(red_block)
        
    for ry_loc in range(y, y+h, 40):
        for rx_loc in range(x, x+w, 40):
            red_blocks.append([rx_loc, ry_loc, 30, 30, False])

def make_blue_blocks():
    global blocks, IS_BLUE, TOUCHED
    blocks = []
    for i in range (0):
        IS_BLUE = True
        TOUCHED = False
        x = random.randrange(30, 800)
        y = random.randrange(400, 600)
        block = [x, y, 30, 30, IS_BLUE, TOUCHED]
        b[4] = True
        b[5] = False 
        blocks.append(block)

make_blue_blocks()

def add_blocks(x, y, w, h): 
    global blocks, IS_BLUE, TOUCHED 
    IS_BLUE = True
    TOUCHED = False
    for y_loc in range(y, y+h, 40):
        for x_loc in range(x, x+w, 40):
            blocks.append([x_loc, y_loc, 30, 30, IS_BLUE, TOUCHED])


def setup():
    global stage, player, red_blocks, blocks, coins
    #blue blocks   
    add_blocks(75, 75, 100, 100)
    add_blocks(350, 200, 100, 100)
    add_blocks(715, 415, 25, 25)
    add_blocks(635, 490, 25, 25)
    add_blocks(500, 100, 200, 200)
    add_blocks(275, 400, 25, 25)
    add_blocks(275, 300, 25, 25)
    add_blocks(275, 200, 25, 25) 
               
    #red blocks
    add_red_blocks(0, 525, 800, 50)
    add_red_blocks(0, 0, 25,  300)
    add_red_blocks(0, 400, 2, 120)
    add_red_blocks(760, 0, 25,  310)
    add_red_blocks(760, 400, 25, 120)
    add_red_blocks(40, 0, 760, 25)
    add_red_blocks(675, 375, 25, 60)
    add_red_blocks(635, 455, 60, 25)
    add_red_blocks(315, 455, 300, 25)
    add_red_blocks(315, 130, 25, 300)
    add_red_blocks(230, 130, 25, 300)
    add_red_blocks(70, 455, 200, 25)

    #Coins
    coin1 = [710, 490, 25, 25]
    coin2 = [275, 200, 25, 25]
    coin3 = [275, 450, 25, 25]
    coin4 = [275, 350, 25, 25]
    coin5 = [275, 250, 25, 25]
    coin6 = [500, 150, 25, 25]
    for b in blocks:
        player =  [675, 300, 25, 25]
        stage = START

    coins = [coin1, coin2, coin3, coin4, coin5, coin6]




    
     

# Game loop
setup()
win = False
done = False
ticks = 20
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if stage == START:
            if event.key == pygame.K_SPACE:
                stage = PLAYING
                
    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        

        if left:
            vel[0] = -player_speed
        elif right:
            vel[0] = player_speed 
        else:
            vel[0] = 0
            
        if up:
            vel[1] = -player_speed
        elif down:
            vel[1] = player_speed
        else:
            vel[1] = 0
            
            
        # Game logic (Check for collisions, update points, etc.)
        ''' move the player in horizontal direction '''
        player[0] += vel[0] 

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if vel[0] > 0:
                    player[0] = w[0] - player[2]
                elif vel[0] < 0:
                    player[0] = w[0] + w[2]
     
        ''' move the player in vertical direction '''
        player[1] += vel[1] 
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if vel[1] > 0:
                    player[1] = w[1] - player[3]
                if vel[1]< 0:
                    player[1] = w[1] + w[3]
                    
        ''' here is where you should resolve player collisions with screen edges  ''' 




        '''get the coins''' 
        hit_list = []
        
        
        for c in coins:
            if intersects.rect_rect(player, c):
                hit_list.append(c)
           
             
        hit_list = [c for c in coins if intersects.rect_rect(player, c)]
        
        
        for hit in hit_list:
            coins.remove(hit)
            score1 += 1
            print("sound!")
       
        if len(coins) == 0:
            win = True
            
            
        # Drawing code (Describe the picture. It isn't actually drawn yet.)
        screen.fill(BLACK)
            
        for w in walls:
            pygame.draw.rect(screen, WHITE, w)

        for c in coins:
            pygame.draw.rect(screen, YELLOW, c)
            
        for b in blocks: 
            block = b[:5]
            IS_BLUE = True
            TOUCHED = False 

            if intersects.rect_rect(player, b):
                b[5] = False  
                
                     
                    
            
            if b[5] == False:
                color = BLUE
            else:
                color = RED
                if intersects.rect_rect(player,b) and color == RED:
                   stage = END
                    
                     
            rect = b[:4]
            pygame.draw.rect(screen, color, rect)
        
    for r in red_blocks:
        red_block = r[:4]
        r[4] = False
        if r[4] == False:
            color = RED
        if intersects.rect_rect(player,r):
            stage = END
            
        pygame.draw.rect(screen, color, red_block)

    pygame.draw.rect(screen, GREEN, player)

    if stage == START:
        text1 = MY_FONT.render("Press SPACE to Start.", True, WHITE)
        screen.blit(text1, [310, 150])
       
       

    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                setup() 

      
       
        
    
    if win and stage == PLAYING:
        font = pygame.font.Font(None, 48)
        if score1 == 3: 
            text = font.render("PERFECT", 1, WHITE)
            screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
