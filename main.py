
import getopt
from src.Game                  import *
from src.player import *

from src.player.Human        import *
from src.player.BuildAndRunBot import *
from src.player.MyBot import *


PARAMETERS_ERROR_RETURN_CODE = 1

def main():

    p = [Human(), MyBot()]

    game = Game(p, True)

    game.takeTurn(game.board.validPawnMoves())




main()
