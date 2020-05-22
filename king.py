from piece import *
from color import *
class King(Piece):
    __symbol = "K"
    __count = 1
    direction = [Piece.moveUp,Piece.moveUpRight,
                Piece.moveRight,Piece.moveDownRight,
                Piece.moveDown,Piece.moveDownLeft,
                Piece.moveLeft,Piece.moveUpLeft]
    def __init__(self,chess,player,newPosition):
        self.chess = chess
        self.player = player
        if player == "black":
            self.color = Color.RED
        else:
            self.color = Color.YELLOW
        self.position=newPosition
        self.setPosition(newPosition)
    def move(self,newPosition):
        moveList=self.possibleMove()
        if newPosition in moveList:
            (x,y)=self.getCoordinate(self.position)
            board=self.chess.getBoard()
            board[x][y]="-"
            self.setPosition(newPosition)
            return True
        else:
            print("Invalid move")
            return False
    def getColor(self):
        return self.color
    def getSymbol(self):
        return King.__symbol
    def getPlayerName(self):
        return self.player.name
    def getPosition(self):
        return self.position
    def setPlayerName(self,name):
        self.player.name = name
    def setPosition(self,newPosition):
        self.position=newPosition
        self.chess.setPosition(self)
    def possibleMove(self):
        finalList = []
        moveList=super().possibleMove(self)
        for direc in moveList:
            count = King.__count
            for pos in direc:
                if count > 0:
                    (x,y)=self.getCoordinate(pos)
                    board=self.chess.getBoard()
                    obj=board[x][y]
                    if isinstance(obj,str):
                        finalList.append(pos)
                        count -= 1
                    elif self.player != obj.player:
                        finalList.append(pos)
                        break
                    else:
                        break
        return finalList
if __name__ == "__main__":
    from chess import Chess,Player
    p1 = Player("champ1","black")
    p2 = Player("champ2","white")
    c1 = Chess(p1,p2)
    k1 = King(c1,"white","2d")
    print(k1.possibleMove())
    k1.move("3d")
    c1.printBoard()

