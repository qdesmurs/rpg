#!/usr/bin/env python
#-- coding: UTF-8 --

class Board(object):
    def __init__(self, lig, col):
        self.grid = []
        for l in range(lig):
            truc = []
            for c in range(col):
                truc.append(Cell(l, c))
            self.grid.append(truc)

    def get_grid(self):
        return self.grid


    def get_cell(self, lig, col):
        return self.grid[lig][col]


    def get_height(self):
        return len(self.grid)


    def get_width(self):
        return len(self.grid[0])


class Cell(Board):
    def __init__(self, lig, col):
        self.items = []
        self.characters = []
        self.lig = lig
        self.col = col
