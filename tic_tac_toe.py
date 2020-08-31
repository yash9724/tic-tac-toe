"""
tic_tac_toe.py : A simple command line based tic tac toe
python version 3.8
"""

import os

__author__ = "Yash Gupta"

class Board:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = [[0]*boardSize for _ in range(boardSize)]
    
    def getSize(self):
        return self.boardSize

    def getCell(self, row, col):
        return self.board[row][col]

    def setCell(self, row, col, val):
        self.board[row][col] = val

    def printBoard(self):
        board = ''
        for row in range(self.boardSize):
            board += '---|'*(self.boardSize - 1) + '---\n'
            for col in range(self.boardSize):
                cell = self.getCell(row, col)
                val = ' ' if cell == 0 else cell
                board += f' {val} '
                if col != self.boardSize - 1:
                    board += '|'
            board += '\n'
        board += '---|'*(self.boardSize - 1) + '---\n'
        print(board)

#class User:
#    pass

class TicTacToe:
    def __init__(self, boardSize):
        self.board = Board(boardSize)
        self.user_1 = 1
        self.user_2 = -1
        self.winner = 0
        self.rowSum = [0]*self.board.getSize()
        self.colSum = [0]*self.board.getSize()
        self.diagSum = 0
        self.reverseDiagSum = 0
        
    def checkWinner(self, row, col, player):
        winner = 0
        boardSize = self.board.getSize()
        if player == self.user_1:
            if self.rowSum[row]== boardSize or \
               self.colSum[col] == boardSize or \
               self.diagSum == boardSize or \
               self.reverseDiagSum == boardSize:
                   winner = player
        else:
            if self.rowSum[row] == -boardSize or \
               self.colSum[col] == -boardSize or \
               self.diagSum == -boardSize or \
               self.reverseDiagSum == -boardSize:
                   winner = player
        return winner

    def clearScr(self):
        # windows                       
        if os.name == 'nt':
             _ = os.system('cls')
        
        # for linux/mac it is 'posix'
        else:
             _ = os.system('clear')

    def refresh(self):
        self.clearScr()
        print("user 1 is 1 and user 2 is -1");
        self.board.printBoard()

    def updateScore(self,row, col, player):
        self.rowSum[row] += player
        self.colSum[col] += player
        if row == col:
            self.diagSum += player
        if row + col == self.board.getSize():
            self.reverseDiagSum += player


    def start(self):
        self.refresh()
        player = self.user_1
        boardSize = self.board.getSize()
        no_of_entries = boardSize**2
        while self.winner == 0 and no_of_entries:
            while True:
                try:
                    index = int(input())
                    row = index // boardSize
                    col = index % boardSize
                    while index < 0 or index > (boardSize**2)-1 or self.board.getCell(row, col) != 0:
                        print(f'Invalid Entry. Index should be between 0 and {boardSize**2 - 1} and should be empty.\n')
                        index = int(input())
                        row = index // boardSize
                        col = index % boardSize
                    break
                except ValueError:
                    print("Index can be integer value only. Enter Again: ", end='')
            
            no_of_entries -= 1
            self.board.setCell(row, col, player)
            
            self.refresh()
            self.updateScore(row, col, player)
            self.winner = self.checkWinner(row, col, player)            
            player = self.user_1 if player == self.user_2 else self.user_2
        
        if self.winner == 0:
            print('Game Drawn')
        else:
            print(f"Winner is {self.winner}")
     
if __name__ == "__main__":
    size = 0
    while True:
        try:
            size = int(input("Enter size of board: "))
            break
        except ValueError:
            print("Size can be integer value only.")
    
    game = TicTacToe(size)
    game.start()
    del game
