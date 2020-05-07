from chess_common import *
from chess_rules import *

class Pawn(ChessPiece):

    #When creating the object of this pawn, define current position
    def __init__ (self,name="pawn",color=PieceColor.Black,cur_pos=0):
        self.name = name
        self.cur_pos = cur_pos
        self.color = color
        #ChessRules.check_start_pos(self,cur_pos)
        print(self.__class__.__name__, self.name, self.color, self.cur_pos)


    def move(self,_from,_to):

        pass




## ------------------------------------------
if (__name__ == "__main__"):
    pawn_black = Pawn(PieceColor.Black, 0)
    pawn_white = Pawn(PieceColor.White, 1)
    print (pawn_black.color, pawn_white.color)