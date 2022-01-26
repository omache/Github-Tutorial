# -*- coding: utf-8 -*-
"""Simple TicTacToe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/166GqBqW0uZArW9l3StI9iCGD4acb0FST

Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
"""

from IPython.display import clear_output # to help us clear the screen after a choice has been made

def display_board(board): # a board to print out the board
  print (board[9]+ "|" + board[8]+ "|" + board[7])
  print ("-----") # for the horizontal lines
  print (board[6]+ "|" + board[5]+ "|" + board[4])
  print("-----")
  print (board[1]+ "|" + board[2]+ "|" + board[3])
  #clear_output()

testboard = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
display_board(testboard)

"""Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer"""

def player_input():
  marker = " " #an empty string
  #We keep asking player1 to chose either X or O
  while marker != "X" and marker != "O":
    marker = input("Chose between O and X: ")

  #We now assign player 2 the opposite marker to that chosen by player1
  player1 = marker
  if marker == "O":
    player2 = "X"
  elif marker == "X":
    player2 = "O"
  return (player1, player2) #We'll need to call this as a tuple

player_input()

"""Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board."""

def place_marker():
  board = [" "," "," "," "," "," "," "," "," "," "]
  position = []

  marker = list(range(0,10))
  while marker not in position:
    inp = int(input("What is your choice: "))
    if inp < 10:
      if inp in position:
        print("This position has already been taken, try again")
        continue
      position.append(inp)
    if inp > 9:
      print("The value is greater than 10 please input a value from 1 to 9")
      continue
    if len(position) == 9:
      print("Game Over")
      break
    
    value = position[-1]
    board[value] = str(position[-1])
    marker.remove(inp)
    



    
    
# the odd length of the position represents the X choice and the O represents the even
    if len(position)%2 != 0:
      board[value] = "X"
    else:
      board[value] = "O"
      win_check(board)
    display_board(board)

place_marker()

"""Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won."""

def win_check(board):
  if board[1] == "X" and board[2] == "X" and board[3] == "X":
    print("The game has been won")
  elif board[1] == "O" and board[2] == "O" and board[3] == "O":
    print("The game has been won")
  elif board[4] == "X" and board[5] == "X" and board[6] == "X":
    print("The game has been won")
  elif board[4] == "O" and board[5] == "O" and board[6] == "O":
    print("The game has been won")
  elif board[7] == "X" and board[8] == "X" and board[9] == "X":
    print("The game has been won")
  elif board[7] == "O" and board[8] == "O" and board[9] == "O":
    print("The game has been won")
  elif board[3] == "X" and board[5] == "X" and board[9] == "X":
    print("The game has been won")
  elif board[3] == "O" and board[5] == "O" and board[9] == "O":
    print("The game has been won")
  elif board[1] == "X" and board[5] == "X" and board[7] == "X":
    print("The game has been won")
  elif board[1] == "O" and board[5] == "O" and board[7] == "O":
    print("The game has been won")

"""Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first."""

import random

def choose_first():
    randomize = random.randint(1,100)
    if randomize % 2 == 0:
      print("Player 1 goes first")
    else:
      print("Player 2 goes first")

choose_first()

"""Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available."""

def space_check(board, position):
  pass
## already done

"""Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again."""

def replay():
  inp = input("Do you want to replay the match?: ")
  if inp.lower == "yes":
    return True
  else:
    print("Thanks for playing")
  #break away from the loop and end the game

"""Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!"""

#while True:
    # Set the game up here
    #pass

    #while game_on:
        #Player 1 Turn
        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break