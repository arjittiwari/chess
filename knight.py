from color import *
from piece import *

class Knight(Piece):
    __symbol = "%"
    __count = 2
    direction = [Piece.moveUp,Piece.moveRight,
                Piece.moveDown,Piece.moveLeft]
    def __init__(self,chess,player,position):
        self.chess = chess
        self.player = player
        if player == "black":
            self.color = Color.RED
        else:
            self.color = Color.YELLOW
        self.position = position
        self.setPosition(position)
    
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
    def kill(self):
        pass
    def getColor(self):
        return self.color
    def getSymbol(self):
        return Knight.__symbol
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
            count = Knight.__count
            if len(direc) >=2 :
                for val in (1,-1):
                    if moveList.index(direc)%2 == 0:
                        (x,y)=self.getCoordinate(direc[count-1])
                        board=self.chess.getBoard()
                        obj=board[x][y+val]
                        if isinstance(obj,str) and obj == "-":
                            finalList.append(self.getPositionByCoordinate(x,y+val))
                        elif isinstance(obj,Piece) and self.player != obj.player:
                            finalList.append(self.getPositionByCoordinate(x,y+val))
                    else:
                        (x,y)=self.getCoordinate(direc[count-1])
                        board=self.chess.getBoard()
                        obj=board[x+val][y]
                        if isinstance(obj,str) and obj == "-":
                            finalList.append(self.getPositionByCoordinate(x+val,y))
                        elif isinstance(obj,Piece) and self.player != obj.player:
                            finalList.append(self.getPositionByCoordinate(x+val,y))
        return finalList
if __name__ == "__main__":
    from chess import Chess,Player
    p1 = Player("champ1","black")
    p2 = Player("champ2","white")
    c1 = Chess(p1,p2)
    k1 = Knight(c1,"black","8b")
    print(k1.possibleMove())
    k1.move("6c")
    c1.printBoard()