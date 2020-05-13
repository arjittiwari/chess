from queen import *
from rook import *
from bishop import *
from pawn import *
from king import *
from knight import *
from player import *
from color import *

class Chess:
    __board = []

    def __init__(self,player1,player2):
        Chess.__initializeBoard(self)
        self.setDefaultPieces()

    def setDefaultPieces(self):
        King(self,"black","d8")
        King(self,"white","d1")
        Queen(self,"black","8e")
        Queen(self,"white","1e")
        for pos in ["2a","2b","2c","2d","2e","2f","2g","2h"]:
            Pawn(self,"white",pos)
        for pos in ["7a","7b","7c","7d","7e","7f","7g","7h"]:
            Pawn(self,"black",pos)
        Bishop(self,"black","c8")
        Bishop(self,"white","c1")
        Bishop(self,"black","f8")
        Bishop(self,"white","f1")
        Rook(self,"black","8a")
        Rook(self,"white","1a")
        Rook(self,"black","8h")
        Rook(self,"white","1h")
        Knight(self,"black","8b")
        Knight(self,"white","1b")
        Knight(self,"black","8g")
        Knight(self,"white","1g")
    def setPosition(self,piece):
        pos=list(piece.position)
        if pos[0].isdigit():
            x=int(pos[0])
            y=int(ord(pos[1]))-96
        else:
            y=int(ord(pos[0]))-96
            x=int(pos[1])
        Chess.__board[x][y]=piece

    def __initializeBoard(self):
        Chess.__board.append([".","a","b","c","d","e","f","g","h","."])
        Chess.__board.append(["1","-","-","-","-","-","-","-","-","1"])
        Chess.__board.append(["2","-","-","-","-","-","-","-","-","2"])
        Chess.__board.append(["3","-","-","-","-","-","-","-","-","3"])
        Chess.__board.append(["4","-","-","-","-","-","-","-","-","4"])
        Chess.__board.append(["5","-","-","-","-","-","-","-","-","5"])
        Chess.__board.append(["6","-","-","-","-","-","-","-","-","6"])
        Chess.__board.append(["7","-","-","-","-","-","-","-","-","7"])
        Chess.__board.append(["8","-","-","-","-","-","-","-","-","8"])
        Chess.__board.append([".","a","b","c","d","e","f","g","h","."])

    def printBoard(self):
        for row in self.__board:
            for column in row:
                if isinstance(column,str):
                    print(Color.GREEN + str(column) + Color.END,end="\t")
                else:
                    print(column.getColor() + column.getSymbol() + Color.END,end="\t")
            print("\n\n")
           
if __name__ == "__main__":
    p1 = Player("champ1")
    p2 = Player("champ2")
    #p3 = Player("champ3")
    c1 = Chess(p1,p2)
    c1.printBoard()

