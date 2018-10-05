# https://techdevguide.withgoogle.com/resources/coding-question-minesweeper

from random import shuffle

class Minesweeper:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0]*cols for _ in range(rows)]

    def at(self,x,y):
        v = self.matrix[x][y]
        return str(v) if v <= 8 else "*"

    def resize(self,rows,cols):
        for i,_ in enumerate(self.matrix):  # each row
            self.matrix[i] = [self.matrix[i] + cols*[0]][:cols]
        new_rows = [[0]*cols for _ in range(rows)]
        self.matrix = (self.matrix + new_rows)[:rows]

    def generate_game(self, mines):
        positions = [(x,y) for x in range(self.rows) for y in range(self.cols)]
        shuffle(positions)
        for p in positions[:mines]:
            self.set_mine(p)
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.at(x,y),end='')
            print()

    def set_mine(self, pos):
        x,y = pos
        self.matrix[x][y] = 9
        adj = [(a,b) for a in range(x-1,x+2) for b in range(y-1,y+2) \
               if 0<=a<self.rows and 0<=b<self.cols]
        for a,b in adj:
            self.matrix[a][b] += 1

# generates expert mode minesweeper
m = Minesweeper(24,24)
m.generate_game(99)
