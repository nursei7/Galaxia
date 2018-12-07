import os
path = os.getcwd()


#The main object class
class Object:
    def __init__(self, x, y, r, img, w, h):
        self.x = x
        self.y = y
        self.r = r
        self.img = loadImage(path+'/images/'+img)
        self.vx = 0
        self.vy = 0
    def update(self):
        self.x += vx
        self.x += vy
        
    def display(self):
        self.update()
        image(self.img, self.x-self.r, self.y- self.r)
    
    
        
#class for the spaceship
class Fighter(Object):
    def __init__(self, x, y, r, img, w, h):
        Object.__init__(self, x, y, r, img, w, h)
        self.keyHandler = {LEFT : False, RIGHT : False, UP : False, DOWN : False}
    
    def update(self):
        if self.keyHandler[LEFT]:
            self.x -= 10
        elif self.keyHandler[RIGHT]:
            self.x += 10
        if self.keyHandler[UP]:
            self.y -= 10
        elif self.keyHandler[DOWN]:
            self.y +=10
        
        if self.x - self.r < 0:
             self.x = self.r
        elif self.x + self.r > 680:
             self.x = 680 - self.r
        if self.y + self.r > 720:
            self.y = 720 - self.r
        elif self.y - self.r < 0:
            self.y = self.r
        
        


class Asteroids(Object):
    def __init__(self,x, y, r, img):
        Spaceship.__init(self, x, y, r)

        

class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.backgroundImg = loadImage(path + '/images/background.jpg')
        self.fighter = Fighter(self.w//2, self.h - 45, 45, 'fighter.png', 90,90)



    def display(self):
        image(self.backgroundImg,0,0)
        self.fighter.display()
        

g = Game(680, 720)

        
        
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
    elif keyCode == UP:
        g.fighter.keyHandler[UP] = True
    elif keyCode == DOWN:
        g.fighter.keyHandler[DOWN] = True
    
        
def keyReleased():
    if keyCode == LEFT:
        g.fighter.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.fighter.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.fighter.keyHandler[UP] = False
    elif keyCode == DOWN:
        g.fighter.keyHandler[DOWN] = False
        
    
    
