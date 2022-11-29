# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import pandas as pd
import os
class Board():
    def __init__(self):
        self.board = self.make_empty_board()
        self.current_player = 'X'
        # print(self.print_board())
    def get_board(self):
        return self.board
    def print_board(self):
        print_str=""
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==None:
                    # print(i*3+j+1,end=" ")
                    print_str+=str(i*3+j+1)+" "
                else:
                    # print(board[i][j],end=" ")
                    print_str+=self.board[i][j]+" "
                if j<2:
                    # print("|",end=" ")
                    print_str+="|"+" "
            # print()
            print_str+="\n"
            if i<2:
                # print("---------")
                print_str+="---------"
                print_str+="\n"
        return print_str
    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    def get_winner(self):
      
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2] and self.board[i][0]!=None:
                return self.board[i][0]
            if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i]!=None:
                return self.board[0][i]
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=None:
            return self.board[0][0]
        if self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[0][2]!=None:
            return self.board[0][2]
        return None
    def check_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==None:
                    return False
        return True
    def make_move(self, player, position):
        
        position-=1

        if self.board[position//3][position%3]==None:
            self.board[position//3][position%3]=player
            return True
        else:
            return False
    def game_over(self):
        return self.get_winner() or self.check_full()

class  Human:
    def __init__(self,player):
        self.player=player
        self.type="Human"
    def get_move(self):
        return self.parse_move(input(f"Player {self.player},Enter your move: "))
    def parse_move(self,move):
        try:
            move=int(move)
            if move not in range(1,10):
                print("Invalid move.")
                return self.get_move()
            return move
        except:
            print("Invalid move.")
            return self.get_move()
    def get_player(self):

        return self.player
    def get_type(self):
        return self.type

class Bot:
    def __init__(self,player):
        self.player=player
        self.type="Bot"
    def get_move(self,board):
        # chioce= random.choice([i for i in range(0,9) if board[i//3][i%3]==None])
        valid_move=[]
        for i in range(9):
            if board[i//3][i%3]==None:
                valid_move.append(i)
        chioce=random.choice(valid_move)
        print("Bot move: "+str(chioce+1))
        return chioce+1
    def get_player(self):
        return self.player
    def get_type(self):
        return self.type
class Game:
    def __init__(self,player1,player2):
        print("Welcome to Tic Tac Toe!")
        self._board=Board()
        self._player1=player1
        self._player2=player2
        self._current_player=player1
        self._game_over=False
        self._winner=None
    def get_other_player(self,player):
        if player==self._player1:
            return self._player2
        else:
            return self._player1
    def run(self):
        save_columns=["game_id","player1","player2","winner","player1_type","player2_type"]
        if os.path.exists("result_database.csv"):
            result_database=pd.read_csv("result_database.csv")
            game_id=result_database.shape[0]+1
        else:
            result_database=pd.DataFrame(columns=save_columns)
            game_id=1
        result_row={}
        result_row["game_id"]=game_id
        while not self._game_over:
            print(self._board.print_board())
            
            if self._current_player.get_type() =="Human":

                flag=self._board.make_move(self._current_player.get_player(),self._current_player.get_move())
            else:
                flag=self._board.make_move(self._current_player.get_player(),self._current_player.get_move(self._board.get_board()))
            if not flag :
                print("Invalid move!")
                continue

            # self._game_over=self._board.game_over()
            # self._winner=self._board.get_winner()
            winner=self._board.get_winner()
            if winner:
                print(self._board.print_board())
                # print(winner,"wins!")
                winner=self._current_player if self._current_player.get_player()==winner else self.get_other_player(self._current_player)
                if winner.get_type()=="Bot":
                    print("Bot wins!")
                else:
                    print(f"Human {winner.get_player()}  wins!")
                self._game_over=True
              
                result_row["player1"]=self._player1.get_player()
                result_row["player2"]=self._player2.get_player()
                result_row["winner"]=winner.get_player()
                result_row["player1_type"]=self._player1.get_type()
                result_row["player2_type"]=self._player2.get_type()
                result_database=pd.concat([result_database,pd.DataFrame(result_row,index=[0])])
                result_database.to_csv("result_database.csv",index=False)

                break
            if self._board.check_full():
                print(self._board.print_board())
                print("Board is full!")
                self._game_over=True
               
                result_row["player1"]=self._player1.get_player()
                result_row["player2"]=self._player2.get_player()
                result_row["winner"]="Draw"
                result_row["player1_type"]=self._player1.get_type()
                result_row["player2_type"]=self._player2.get_type()
                result_database=pd.concat([result_database,pd.DataFrame(result_row,index=[0])])
                result_database.to_csv("result_database.csv",index=False)
            
                break
            if self._current_player==self._player1:
                self._current_player=self._player2
            else:
                self._current_player=self._player1
        print(result_database)


