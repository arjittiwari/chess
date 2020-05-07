import enum

class PieceColor(enum.Enum):
    Black = 0
    White = 1


## Base class for all pieces
class ChessPiece():
    
    def __init__ (self,name,color=PieceColor.Black):
        self.name = name
        self.die_position = None
        self.last_position = None
        self.color = color    

    def kill(self):
        pass

    def die(self):
        self.die_position = self.last_position
        pass

    def check_move_position(self,_from,_to):
        pass

    def check_move_rule(self, _from, _to):
        pass

if __name__ == "__main__": 
    print (PieceColor.Black.name)
    print (PieceColor.White.name)
    objPiece = ChessPiece("dummy")

