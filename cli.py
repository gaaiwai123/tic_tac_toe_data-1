# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import *

def main():
    
    if_input=input("Do you want to play with bot? (y/n)")
    if if_input=="y":
        
        what=input("Do you want to play X or O?")
        if what=="X":
            # player1,player2=player2,
            human=Human("X")
            bot=Bot("O")
        else:
            human=Human("O")
            bot=Bot("X")
        chose=input("Do you want to play first? (y/n)")
        if chose=="y":
            # player1,player2=player2,player1
        
            game=Game(human,bot,)
        else:
            game=Game(bot,human,)
        game.run()

    else:
        player1=Human("X")
        player2=Human("O")
        # prrint("Welcome to Tic Tac Toe!")
        who=input("Who want to play first? (X/O)")
        if who=="O":
            player1,player2=player2,player1


        # board=Board()

        game=Game(player1,player2)
        game.run()
if __name__=="__main__":
    main()
        

