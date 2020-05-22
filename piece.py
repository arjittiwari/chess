class Piece:
    __limit1=(1,-1)
    __limit8=(8,1)
    __limit0=(0,0)
    
    def kill(self):
        print("Not override by derived class")
    def getPlayerName(self):
        print("Not override by derived class")
    def getPosition(self):
        print("Not override by derived class")
    def getPositionByCoordinate(self,x,y):
            return(str(x)+chr(96+y))
    def setPlayerName(self):
        print("Not override by derived class")
    def setPosition(self,position):
        print("Not override by derived class")
    def possibleMove(self,piece):
        moveList=[]
        flip = False
        if piece.player == "black":
            flip = True
        for func in piece.direction:
            moveList.append((func(self,position=piece.position,flip=flip)))
        return moveList

    def getCoordinate(self,position):
        pos=list(position)
        if pos[0].isdigit():
            x=int(pos[0])
            y=int(ord(pos[1].lower()))-96
        else:
            y=int(ord(pos[0].lower()))-96
            x=int(pos[1])
        return (x,y)

    def __createMovelist(self,position,
                        limitX,limitY):
        moveList=[]
        (x,y)=self.getCoordinate(position)
        while x != limitX[0] and y != limitY[0]:
            moveList.append("%d%c" %((x+limitX[1]), chr(96+(y+limitY[1]))))
            x = x + limitX[1]
            y = y + limitY[1] 
        return moveList

    def moveUpLeft(self,position,flip):
        limitX=Piece.__limit1 if flip else Piece.__limit8
        limitY=Piece.__limit8 if flip else Piece.__limit1
        return self.__createMovelist(position,
                            limitX,limitY)

    def moveUpRight(self,position,flip):
        limitX=Piece.__limit1 if flip else Piece.__limit8
        limitY=Piece.__limit1 if flip else Piece.__limit8
        return self.__createMovelist(position,
                            limitX,limitY)
         
    def moveDownLeft(self,position,flip):
        limitX=Piece.__limit8 if flip else Piece.__limit1
        limitY=Piece.__limit8 if flip else Piece.__limit1
        return self.__createMovelist(position,
                            limitX,limitY)
         
    def moveDownRight(self,position,flip):
        limitX=Piece.__limit8 if flip else Piece.__limit1
        limitY=Piece.__limit1 if flip else Piece.__limit8
        return self.__createMovelist(position,
                            limitX,limitY)

    def moveUp(self,position,flip):
        limitX=Piece.__limit1 if flip else Piece.__limit8
        limitY=Piece.__limit0 if flip else Piece.__limit0
        return self.__createMovelist(position,
                            limitX,limitY)
        
    def moveDown(self,position,flip):
        limitX=Piece.__limit8 if flip else Piece.__limit1
        limitY=Piece.__limit0 if flip else Piece.__limit0
        return self.__createMovelist(position,
                            limitX,limitY)
        
    def moveLeft(self,position,flip):
        limitX=Piece.__limit0 if flip else Piece.__limit0
        limitY=Piece.__limit8 if flip else Piece.__limit1
        return self.__createMovelist(position,
                            limitX,limitY)
         
    def moveRight(self,position,flip):
        limitX=Piece.__limit0 if flip else Piece.__limit0
        limitY=Piece.__limit1 if flip else Piece.__limit8
        return self.__createMovelist(position,
                            limitX,limitY)
 
if __name__ == "__main__":
    p1 = Piece()
    l1=p1.moveUp("8c",False)
    print(l1)
