import os
path = os.getcwd()


class Object:
    def __init__(self, x, y, r, img):
        self.x = x
        self.y = y
        self.r = r
        self.img = img
        self.vx = 0
        self.vy = 0
        
        
class Fighter(Object):
    def __init__(self, x, y, r, img):
        Object.__init__(self, x, y, r, img)
        self.keyHandler = {LEFT : False, RIGHT : False, UP : False, DOWN : False}
    
    def update(self):
        if self.keyHandler[LEFT]:
            self.vx = -5
        if self.keyHandler[RIGHT]:
            self.vx = 5
        else:
            self.vx = 0
        
        self.x += vx
        
        if self.x - self.r < 0:
             self.x = self.r
        elif self.x + self.r > 900:
             self.x = 900 - self.r
        


class Asteroids(Object):
    def __init__(self,x, y, r, img):
        Spaceship.__init(self, x, y, r)

        

class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.backgroundImg = loadImage(path + '/images/background.jpg')
        #self.fighter = Fighter(w//2, h, 



    def display(self):
        image(self.backgroundImg,0,0)

g = Game(700, 900)

        
        
def setup():
    size(g.w, g.h)
    background(0)
    
def draw():
    background(0)
    g.display()
    
    
def keyPressed():
    if keyCode == LEFT:
        g.fighter.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.fighter.keyHandler[RIGHT] = True
        
    
    
