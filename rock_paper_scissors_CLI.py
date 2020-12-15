# my attempt at rock paper scissors
# finished 5/21/2020
import random, math, time, sys, os



# this prints the title of the game 
print('welcome to my rock paper scissers Game')

  

# this is the game function
def game():
    
    # while loop count
    count = 0
    comp_win = 0
    player_win = 0
    print()
    print('There will be three rounds, at the end we will declare a winner')
    print()
    # start of the while loop for the game 
    while count < 3:
        computer_choice = random.random()*3
        computer_choice = math.floor(computer_choice)
        if computer_choice == 0:
            computer_choice = 0 # rock
            
        elif computer_choice == 1:
                computer_choice = 1 # paper
        else:
            computer_choice = 2 # SCISSORS
            

        #asking the player for thier choice and converting it into caps
        player = input('Please select Rock, Paper or Scissors: ').upper()
        if player == 'ROCK':
            player = 0
            
        elif player == 'PAPER':
            player = 1
            
        elif player == 'SCISSORS':
            player = 2
                  
        # else statement telling the player 
        else:
            print('please make a proper choice!')
            
        
        # Checking to see who wins
        if player == computer_choice:
            print('Tied')
            count = count + 1
            
        # Computer winning
        if player == 0 and computer_choice == 1:
            print('Computer picked Paper and beat you')
            comp_win = comp_win + 1
            count = count + 1
            
        if player == 1 and computer_choice == 2:
            print('Computer picked Scissors and beat you')
            comp_win = comp_win + 1
            count = count + 1
            
        if player == 2 and computer_choice == 0:
            print('Computer picked Rock and beat you')
            comp_win = comp_win + 1
            count = count + 1
            
        # player winning
        if player == 1 and computer_choice == 0:
            print('Player covedred computers Rock You win')
            player_win = player_win + 1
            count = count + 1
            
        if player == 2 and computer_choice == 1:
            print('Player cut up computers paper')
            player_win = player_win + 1
            count = count + 1
           
        if player == 0 and computer_choice == 2:
            print('Player crushed computers Scissors')
            player_win = player_win + 1
            count = count + 1
            


        
        if count == 3:
            print()

            print('the computer has ' + str(comp_win) + ' wins and you had ' + str(player_win) + ' wins')
            print()
            print('Game will end in 5 Seconds')
            # this waits for 5 Seconds before closing the game
            time.sleep(5.0)

        

# closing function 
game()