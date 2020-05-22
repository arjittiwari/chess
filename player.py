class Player:
    __max_count = 2
    def __init__(self,name,team):
        if Player.__max_count > 0:
            self.name = name
            self.color=team
            Player.__max_count = Player.__max_count - 1
        else:
            print("More than two players are not allowed")
        
    