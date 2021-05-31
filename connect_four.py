  
# Hello My Name is Clifton Abraham and this is my first Portfolio Project
# I chose connect four because i always played it in study hall
import random

class Player(object):
    def __init__(self, character):
        self.character = character

class Human(Player):
    def go(self, board):
        while True:
            column = int(input('Column: '))

            if board.insert(column, self.character):
               return True



class Ai(Player):
    def go(self, board):
        print('Thinking....')

        while True:
            if board.insert(random.randint(0, 6), self.character):
                return True



class Board(object):
    def __init__(self):
          self.board = [[] for i in range(0, 7)]
          for i in range(0, 7):
             self.board[i] = [' ' for j in range(0, 6)]

    def display(self):
       print([str(i) for i in range(0, len(self.board))])

       for i in range(len(self.board[0]) - 1, -1, -1):
            print([self.board[j][i] for j in range(0, len(self.board))])

    def insert(self, column, piece):
         # bounds check
        if column > 6 or column < 0:
            return False

        for i in range(0, 6):
            if ' ' == self.board[column][i]:
                self.board[column][i] = piece
                return True

        return False

    def filled(self):
        for i in range(0, len(self.board)):
            if any(map(lambda x: x == ' ', self.board[i])):
                return False

        return True 

    def won_by(self, piece):
        #match by column 
        if any(map(lambda x: self.match_four(x, piece), self.board)):
            return True

            #match by row
        for i in range(0, len(self.board[0])):
            row = [self.board[j][i] for j in range(0, len(self.board))]
            if self.match_four(row, piece):
                return True 

                #match by diaganal
        for i in range(0, len(self.board)): # for each column
            for j in range(0, len(self.board[i])): # for each continuit 
                # look north west
                if self.contains(i - 3, j - 3):
                    if self.match_four([self.board[i - k ][j - k] for k in range(0, 4)], piece):
                        return True

                # look north east
                if self.contains(i + 3, j - 3):
                    if self.match_four([self.board[i + k][j - k] for k in range(0, 4)], piece):
                        return True

                if self.contains(i - 3, j + 3):
                    if self.match_four([self.board[i - k][j + k] for k in range(0, 4)], piece):
                        return True

                if self.contains(i + 3, j + 3):
                    if self.match_four([self.board[i + k][j + k] for k in range(0, 4)], piece):
                        return True

    def contains(self, col, row):
        if col < 0 or col >= len(self.board):
            return False
        elif row < 0 or row >= len(self.board[0]):
            return False
        else:
            return True

    def match_four(self, arr, piece):
        num = 0
        for i in range(0, len(arr)):
            if piece == arr[i]:
                num += 1
                if 4 == num:
                    return True
            else:
                num = 0

        return num == 4


if __name__ == '__main__':
    players = [Human('G'), Ai('R')]
    board = Board()


    player_index = 0

    while not board.filled():
        board.display()

        current_player = players[player_index]

        current_player.go(board)

        if board.won_by(current_player.character):
            board.display()
            print("Player " + current_player.character + " Has won the Game!!!")
            exit()

        player_index = (player_index + 1) % 2
 
     



        