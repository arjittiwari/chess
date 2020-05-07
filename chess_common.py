import enum

class PieceColor(enum.Enum):
    Black = 0
    White = 1


## Base class for all pieces
class ChessPiece():
    
    def __init__ (self,color=PieceColor.Black):
        self._color = color    
        print("Black color defaulted for ", self.__class__.__name__)



if __name__ == "__main__": 
    print (PieceColor.Black.name)
    print (PieceColor.White.name)
    objPiece = ChessPiece()

