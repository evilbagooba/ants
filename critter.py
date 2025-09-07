white,black = 0,1

class LangAnt:
    # in the naming scheme for multiple colors, langtons ants are called RL
    def __init__ (self,x,y,orientation):
        self.x = x 
        self.y = y
        self.orientation = orientation
        self.orientations = [[0,-1],[1,0],[0,1],[-1,0]]
    

    def forward(self,environment):
        self.x = (self.x + self.orientations[self.orientation][0]) % environment.width
        self.y = (self.y + self.orientations[self.orientation][1]) % environment.height
        
    def move(self, environment):
        mySquare = environment.get_square(self.x, self.y)
        if mySquare == 0:
            self.orientation = (self.orientation + 1) % 4
            environment.colorSquare(black, self.x, self.y)
            self.forward(environment)
        elif mySquare == 1:
            self.orientation = (self.orientation - 1) % 4
            environment.colorSquare(white, self.x, self.y)
            self.forward(environment)

