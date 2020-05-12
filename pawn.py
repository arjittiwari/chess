from color import *
from piece import *
class Pawn(Piece):
    __symbol = "P"
    def __init__(self,chess,player,position):
        self.chess = chess
        self.player = player
        if player == "black":
            self.color = Color.RED
        else:
            self.color = Color.YELLOW
        self.position = position
        self.setPosition(self.position)
    
    def move(self,position):
        pass
    def kill(self):
        pass
    def getColor(self):
        return self.color
    def getSymbol(self):
        return Pawn.__symbol
    def getPlayerName(self):
        return self.player.name
    def getPosition(self):
        return self.position
    def setPlayerName(self,name):
        self.player.name = name
    def setPosition(self,position):
        self.chess.setPosition(self)
    def possibleMove(self):
        pass
