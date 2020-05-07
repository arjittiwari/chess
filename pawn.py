
##
## Have a package/module that can be common

from chess_common import *

class Pawn:

    #When creating the object of this pawn, define current position
    def __init__ (self,color,cur_pos):
        self.cur_pos = cur_pos

    def move(self,_from,_to):
        pass

    
