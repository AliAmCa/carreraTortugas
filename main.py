import turtle

class Circuito():
    corredores = []
    __posStartY=(-60,-20,20,60)
    __colorTurtle = ('red' , 'blue', 'green','orange')
    
    def __init__(self, width, height):
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine= -width/2 + (width*5/100)
        self.__finishLine= width/2 -(width*5/100)
        
        self.createRunners()
    
    def createRunners(self):
        
        for i in range (4):
            new_turtle= turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
        
      
        
        
        
        
if __name__ == '__main__':
    circuito= Circuito(640,480)