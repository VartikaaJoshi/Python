#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
number = random.randint(1,100)
print(number)
level = int(input("Type 1 if you want to play easy level game and type 2 if you want to play hard level.: "))

        
if level == 1:
         for i in range(1,11):
           if i <11:
              user_input = int(input("Type your guess: "))
              difference= number - user_input
              if difference >0:
                  print("Too low")
              elif difference <0:
                  print("Too high")
              elif difference ==0:
                  print("You won")
                
             
                  
elif level == 2:
             for i in range(1,6):
               if i < 11:
                 user_input = int(input("Type your guess: "))
                 difference= number - user_input
                 if difference >0:
                  print("Too low")
                 elif difference <0:
              print("Too high")
             elif difference ==0:
              print("You won")
        
    


     




