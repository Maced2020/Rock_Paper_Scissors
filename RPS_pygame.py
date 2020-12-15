# my attempt at rock paper scissors with pygame
# started on 10/29/2020
# finished 11/6/2020

import random, math, time, sys, os, pygame


# initializing function
def initializing():
    pygame.init()
    pygame.font.init()

initializing()



# Global Varibles

TITLE_FONT = pygame.font.SysFont('comicsans', 80)
BACKGROUND_COLOR = (135,206,235) # light Blue
TEXT_COLOR = (73,2,94) # Some Kind of purple
HEIGHT, WIDTH = 1000, 1000 # The width is first even though it is listed Second
GAME_WINDOW = pygame.display.set_mode((HEIGHT, WIDTH))
GAME_WINDOW.fill(BACKGROUND_COLOR)
TOP_TEXT = TITLE_FONT.render('ROCK PAPER SCISSORS', 1, TEXT_COLOR)
GAME_WINDOW.blit(TOP_TEXT, (WIDTH/2 - TOP_TEXT.get_width()/2, 20))
pygame.display.flip()
pygame.display.set_caption('Rock Paper Scissors') # this is the top line 


# game outcome Messages 
def tied_message():
    pygame.display.update()
    GAME_WINDOW.fill(BACKGROUND_COLOR)
    tied = TITLE_FONT.render('You Tied!' , 1, TEXT_COLOR)
    GAME_WINDOW.blit(tied, (WIDTH//2 - TOP_TEXT.get_width()/2, 10))
    pygame.display.flip()
    pygame.display.update()

def lost_message():
    pygame.display.update()
    GAME_WINDOW.fill(BACKGROUND_COLOR)
    lost = TITLE_FONT.render('You Lost!' , 1, TEXT_COLOR)
    GAME_WINDOW.blit(lost, (WIDTH//2 - TOP_TEXT.get_width()/2, 10))
    pygame.display.flip()
    pygame.display.update()

def won_message():
    pygame.display.update()
    GAME_WINDOW.fill(BACKGROUND_COLOR)
    won = TITLE_FONT.render('You Won!' , 1, TEXT_COLOR)
    GAME_WINDOW.blit(won, (WIDTH//2 - TOP_TEXT.get_width()/2, 10))
    pygame.display.flip()
    pygame.display.update()

# loads images out of images file
def load_images():
    image_list = []
    for i in range(3):
        image = pygame.image.load('pictures\RPS' + str(i) + '.png')
        image_list.append(image)
    GAME_WINDOW.blit(image_list[0], (115, 208)) # rock picture
    GAME_WINDOW.blit(image_list[1], (415, 208)) # paper picture
    GAME_WINDOW.blit(image_list[2], (715, 208)) # scisors picture
    pygame.display.update()




# randomly selects the computer choice
def computer_choice():
    comp_choice = random.random() * 3
    comp_choice = math.floor(comp_choice)
    return comp_choice

# keeps the game running until you close it
# also collects the mouse clicks info

def play_game():
    true = True
    while true == True:
        # loads the game screen
        GAME_WINDOW.fill(BACKGROUND_COLOR)
        TOP_TEXT = TITLE_FONT.render('ROCK PAPER SCISSORS', 1, TEXT_COLOR)
        GAME_WINDOW.blit(TOP_TEXT, (WIDTH/2 - TOP_TEXT.get_width()/2, 20))
        load_images()
        # closes the game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # the following will collect the mouse clicks
                # and confirm which option you selected
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x > 115 and mouse_x < 250 and mouse_y > 210 and mouse_y < 299: # this is rock
                    comp_choice = computer_choice()
                    rock = True 
                    if rock == True and comp_choice == 0:
                        tied_message()
                        time.sleep(1.5)
                
                    elif rock == True and comp_choice == 1:
                        lost_message()
                        time.sleep(1.5)
                        

                    elif rock == True and comp_choice == 2:
                        won_message()
                        time.sleep(1.5)
                        

                elif mouse_x > 429 and mouse_x < 550 and mouse_y > 220 and mouse_y < 301: # this is paper
                    comp_choice = computer_choice()
                    paper = True
                    if paper == True and comp_choice == 1:
                        tied_message()
                        time.sleep(1.5)
                        
                    elif paper == True and comp_choice == 0:
                        won_message()
                        time.sleep(1.5)
                        
                    elif paper == True and comp_choice == 2:
                        lost_message()
                        time.sleep(1.5)
                        

                    
                elif mouse_x > 715 and mouse_x < 860 and mouse_y > 210 and mouse_y < 306: # scissors selected
                    comp_choice = computer_choice()
                    scissers = True
                    if scissers == True and comp_choice == 0:
                        lost_message()
                        time.sleep(1.5)
                        
                    elif scissers == True and comp_choice == 1:
                        won_message()
                        time.sleep(1.5)
                        
                    elif scissers == True and comp_choice == 2:
                        tied_message()
                        time.sleep(1.5)
                        
play_game()