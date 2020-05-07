from pawn import *
from chess_common import *
from chess_rules import *


class ChessBoard():

    def __init__(self):
        b_p_1 = Pawn("b_pawn_1",PieceColor.Black,1)
        b_p_2 = Pawn("b_pawn_2",PieceColor.Black,2)
        b_p_3 = Pawn("b_pawn_3",PieceColor.Black,3)
        b_p_4 = Pawn("b_pawn_4",PieceColor.Black,4)
        b_p_5 = Pawn("b_pawn_5",PieceColor.Black,5)
        b_p_6 = Pawn("b_pawn_6",PieceColor.Black,6)
        b_p_7 = Pawn("b_pawn_7",PieceColor.Black,7)
        b_p_8 = Pawn("b_pawn_8",PieceColor.Black,8)
        w_p_1 = Pawn("w_pawn_1",PieceColor.Black,1)
        w_p_2 = Pawn("w_pawn_2",PieceColor.Black,2)
        w_p_3 = Pawn("w_pawn_3",PieceColor.Black,3)
        w_p_4 = Pawn("w_pawn_4",PieceColor.Black,4)
        w_p_5 = Pawn("w_pawn_5",PieceColor.Black,5)
        w_p_6 = Pawn("w_pawn_6",PieceColor.Black,6)
        w_p_7 = Pawn("w_pawn_7",PieceColor.Black,7)
        w_p_8 = Pawn("w_pawn_8",PieceColor.Black,8)


    def create_board():
        pass
        

if __name__ == "__main__":
    my_c_b = ChessBoard()