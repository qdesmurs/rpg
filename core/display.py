#!/usr/bin/env python

# -- coding: UTF-8 --

from board import Board, Cell
from character import Player

class BoardDisplayer(Board):
    def __init__(self, board, player):
        self.player = player
        self.board = board

    def display(self):
        pass

    def wait_move(self):
        pass

    def get_cell(self, lig, col):
        return self.board.get_cell(lig, col)

    def get_grid(self):
        return self.board.grid

    def get_height(self):
        return len(self.board.grid)

    def get_width(self):
        return len(self.board.grid[0])

class ConsoleBoard(BoardDisplayer):

    def display(self):
        res = ""
        lig = 0
        while lig <self.get_height():
            col = 0
            while col < self.get_width():
                cell = self.get_cell(lig, col)
                if self.player in cell.characters:
                    res += "X"
                else :
                    res += "#"
                col += 1
            res += "\n"
            lig += 1
        print res
