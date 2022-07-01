import random
from itertools import product
from time import sleep
import click
from colorama import Fore,init

init(autoreset=True)

class TicTacToe():
    def __init__(self,n) -> None:
        self.board = []
        self.empty_loc = [*product(range(0,3),range(0,3))]
        self.n = n
        self.createBoard()
        print(Fore.RED+"Player X: X\nPlayer O: O\n\nPlayer X")
        self.printBoard()
    def createBoard(self):
        for _ in range(self.n):
            row = []
            for __ in range(self.n):
                row.append("-")
            self.board.append(row)    
    def run(self):
        while True:
           try: 
            x,y = map(lambda a: int(a)-1,input().replace(" ","").split(","))
            if not self.availability(y,x):
                print(f"{x+1},{y+1} is not available")
                continue
            self.board[y][x] = "X"
            if self.control():
                click.clear()
                print(Fore.RED+"Player X wins\n")
                self.printBoard()
                break
            click.clear()
            print(Fore.RED+"Player O")
            self.printBoard()    
            self.empty_loc.remove((y,x)) if (y,x) in self.empty_loc else None
            if (len(self.empty_loc)==0):
                break
            mc =random.choice(self.empty_loc)
            sleep(1)
            self.board[mc[0]][mc[1]] = "O"
            if self.control():
                click.clear()
                print(Fore.RED+"Player O wins\n")
                self.printBoard()
                break
            click.clear()
            print(Fore.RED+"Player X")
            self.printBoard()
            self.empty_loc.remove((mc[0],mc[1])) if (mc[0],mc[1]) in self.empty_loc else None
           except KeyboardInterrupt:
               break 
           except:
               continue    
                
    def printBoard(self):
        print(Fore.RED+"\n  1 2 3")
        for i,v in enumerate(self.board):
            print(Fore.RED+"{} ".format(i+1)+Fore.BLUE+" ".join(v))   
    def availability(self,y,x):
        if self.board[y][x] == "-":
            return True
        return False          
    def control(self):
        for i in self.board:
            if i == ["X"]*self.n or i == ["O"]*self.n:
                return True 
        for j in range(self.n):
           col =  [self.board[i][j] for i in range(self.n)]
           if col == ["X"]*self.n or col==["O"]*self.n:
               return True
        c = [self.board[i][i] for i in range(self.n)]   
        if c == ["X"]*self.n or c == ["O"]*self.n:
            return True         
        t = [self.board[self.n-1-i][self.n-1-i] for i in range(self.n)]
        if t == ["X"]*self.n or t == ["O"]*self.n:
            return True
        return False
if __name__ == "__main__":                  
   game = TicTacToe(3)
   game.run()