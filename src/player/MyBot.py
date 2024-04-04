#
# MyBot.py
#
# Brief description
# 
# @author    My Name
# @date      2000.00.00
# @version   0.1
#

from src.player.IBot    import *
from src.action.IAction import * 



class MyBot(IBot):

    def __init__(self, name = None, color = None):
        self.name   = name
        self.color  = color
        self.pawn   = None
        self.fences = []
        self.score  = 0
        self.startPosition = None
        self.endPositions = []

    def play(self, board) -> IAction:
        # TODO
        pass

