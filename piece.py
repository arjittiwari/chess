class Piece:
    limit1=(1,-1)
    limit8=(8,1)
    limit0=(0,0)
    def move(self,position):
        print("Not override by derived class")
    def kill(self):
        pass
    def getPlayerName(self):
        pass
    def getPosition(self):
        pass
    def setPlayerName(self):
        pass
    def setPosition(self):
        pass
    def possibleMove(self):
        pass
    def createMovelist(self,
                        x,y,
                        limitX,limitY,
                        moveList):
        while x != limitX[0] and y != limitY[0]:
            moveList.append("%d%c" %((x+limitX[1]), chr(96+(y+limitY[1]))))
            x = x + limitX[1]
            y = y + limitY[1]
    def moveUpLeft(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit1
            limitY=Piece.limit8
        else:#red Player
            limitX=Piece.limit8
            limitY=Piece.limit1
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)  
    def moveUpRight(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit1
            limitY=Piece.limit1
        else:#red Player
            limitX=Piece.limit8
            limitY=Piece.limit8
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
         
    def moveDownLeft(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit8
            limitY=Piece.limit8
        else:#red Player
            limitX=Piece.limit1
            limitY=Piece.limit1
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
         
    def moveDownRight(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit8
            limitY=Piece.limit1
        else:#red Player
            limitX=Piece.limit1
            limitY=Piece.limit8
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
        
    def moveUp(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit1
            limitY=Piece.limit0
        else:#red Player
            limitX=Piece.limit8
            limitY=Piece.limit0
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
        
    def moveDown(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit8
            limitY=Piece.limit0
        else:#red Player
            limitX=Piece.limit1
            limitY=Piece.limit0
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
        
    def moveLeft(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit0
            limitY=Piece.limit8
        else:#red Player
            limitX=Piece.limit0
            limitY=Piece.limit1
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
         
    def moveRight(self,x,y,moveList,flip):
        if flip :#Yellow Player
            limitX=Piece.limit0
            limitY=Piece.limit1
        else:#red Player
            limitX=Piece.limit0
            limitY=Piece.limit8
        self.createMovelist(x,y,
                            limitX,limitY,
                            moveList)
 
if _name_ == "__main__":
    p1 = Piece()
    l1 =[]
    p1.moveUpLeft(8,4,l1,True)
    print(l1)
