# JanggiGame

## What is Janggi and how can I play it?

Janggi is a Korean game similar to chess. This implementation of Janggi can be played by two players through the command line. 


## What are the rules of Janggi?

The game consists of two opposing teams, which are red and blue, taking turns moving Janggi pieces around the game board and attemping to capture the pieces of their opponent. The game is won by placing the opposing General piece into check-mate. The blue player moves first. 

A complete explanation of the game, including the legal moves for each type of game piece, can be found at the following URL: https://en.wikipedia.org/wiki/Janggi


## How can I start playing?

Import the class named JanggiGame from the JanggiGame.py module. Creating an instance of the JanggiGame class will begin a new game. Calling the function make_move() will allow a player to make a move on the board. Two arguments must be passed to make_move(), the first is the current square location of a player's piece on the board, and the second is the square on the board where the selected piece will be moved. If a player attempts an illegal move, attemps to move an opponent's piece, or moves out of turn, then make_move() will return False because the move did not work. If a move is successful, True will be returned. Once the game is won, no further moves will be allowed. To determine if the game has been won, the function get_game_state() can be called with no arguments. 
