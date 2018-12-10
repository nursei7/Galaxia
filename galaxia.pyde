import os
from random import randint
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
        self.h = h
        self.w = w
    def update(self):
        self.x += vx
        self.x += vy
        
    def display(self):
        self.update()
        image(self.img, self.x-self.r, self.y - self.r)
    
    
        
#class for the spaceship
class Fighter(Object):
    def __init__(self, x, y, r, img, w, h):
        Object.__init__(self, x, y, r, img, w, h)
        self.health = 100
        self.keyHandler = {LEFT : False, RIGHT : False, UP : False, DOWN : False, SHIFT: False}
    
    def update(self):
        if self.keyHandler[LEFT]:
            self.x -= 7        #spaceship moves left
        elif self.keyHandler[RIGHT]:
            self.x += 7 #spaceship moves right
        if self.keyHandler[UP]:
            self.y -= 7 #spaceship goes up
        elif self.keyHandler[DOWN]:
            self.y +=7 #spaceship goes down
        
        if self.x - self.r < 0:
             self.x = self.r
        elif self.x + self.r > 680:
             self.x = 680 - self.r
        if self.y + self.r > 720:
            self.y = 720 - self.r
        elif self.y - self.r < 0:
            self.y = self.r
            
        
        


class Asteroid(Object):
    def __init__(self, x, y, r, img, w, h):
        Object.__init__(self, x, y, r, img, w, h)
        self.vy = randint(2, 14)
    def update(self):
       # g.asteroids.append(g.ast[randint(0,3)])
        self.y += self.vy
        if self.y - 2 * self.r > 720:
            self.y = 0 - randint(100,  350)
            self.x = randint(self.r, 680 - self.r)
  
   

       

class Game:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.frames = 0
        self.y = 0
        self.status = "menu"
        self.pause = False
        self.backgroundImg = loadImage(path + '/images/background.jpg')
        self.fighter = Fighter(self.w//2, self.h - 45, 45, 'fighter.png', 90,90)
        self.ast = []
        self.ast.append(Asteroid(randint(45, self.w - 45), 0 - 50-300, 42, 'ast1.png', 100, 100))
        self.ast.append(Asteroid(randint(95,self.w - 95), 0 - 109-300, 95, 'ast2.png', 250, 270))
        self.ast.append(Asteroid(randint(31, self.w - 31), 0 - 50-300, 31, 'ast3.png', 100, 100))
        self.ast.append(Asteroid(randint(44, self.w - 44), 0 - 44-300, 43, 'ast4.png', 150, 200))
        for i in range(6):
            self.ast.append(Asteroid(randint(44, self.w - 44), 0 - 44-randint(200, 700), 43, 'ast4.png', 150, 200))
            self.ast.append(Asteroid(randint(44, self.w - 44), 0 - 44-randint(200, 700), 42, 'ast1.png', 100, 100))
            self.ast.append(Asteroid(randint(31, self.w - 31), 0 - 50-randint(200, 700), 43, 'ast3.png', 100, 100))

       
        

        



    def display(self):
        
        image(self.backgroundImg, 0, 0 - (self.h - self.y))
        image(self.backgroundImg, 0, self.y+1)
        rect(10, 10, self.fighter.health, 15)
        fill(0, 250, 0)
        self.fighter.display()
        self.y += 4
        self.y %= self.h
        for i in self.ast:
            i.display()
        #update in 
        
        

g = Game(680, 720)

        
        
def setup():
    frameRate(60)
    size(g.w, g.h)
    background(0)
wp = loadImage(path+'/images/wp.png')
def draw():
    if g.status == 'menu':
        background(0)
        image(wp,0,0)
        textSize(34)
        fill(0)
        text('Press shift to start', g.w//4, g.h//3)
        text('Arrows to move. Space to fire', g.w//4-30, g.h//3+50)
    elif g.status == 'play':
        if not g.pause:
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
    if keyCode == SHIFT:
        g.fighter.keyHandler[SHIFT] = True
        g.status = 'play'
    
        
    
        
def keyReleased():
    if keyCode == LEFT:
        g.fighter.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.fighter.keyHandler[RIGHT] = False
    if keyCode == UP:
        g.fighter.keyHandler[UP] = False
    elif keyCode == DOWN:
        g.fighter.keyHandler[DOWN] = False
    if keyCode == SHIFT:
        g.fighter.keyHandler[SHIFT] = False
    
        
    
    
