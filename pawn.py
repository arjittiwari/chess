from chess_common import *
from chess_rules import *

class Pawn(ChessPiece):

    #When creating the object of this pawn, define current position
    def __init__ (self,name="pawn",color=PieceColor.Black,start_pos=0):
        super().__init__(name,color)
        self.start_pos = start_pos
        #self.color = color
        #ChessRules.check_start_pos(self,start_pos)
        print(self.__class__.__name__, self.name, self.color, self.start_pos)


    def move(self,_from,_to):
        self.check_move_position(_from,_to)
        self.check_move_rule(_from, _to)

    def check_move_position(self,_from,_to):
        pass

    def check_move_rule(self, _from, _to):
        pass


## ------------------------------------------
if (__name__ == "__main__"):
    pawn_black = Pawn("p1", PieceColor.Black, "h1")
    pawn_white = Pawn("p2", PieceColor.White, "k8")