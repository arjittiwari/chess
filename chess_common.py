import enum

class PieceColor(enum.Enum):
    Black = 0
    White = 1




if __name__ == "__main__": 
    print (PieceColor.Black.name)
    print (PieceColor.White.name)
