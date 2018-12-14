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
        self.keyHandler = {LEFT : False, RIGHT : False, UP : False, DOWN : False, SHIFT: False, ALT : False}
    
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
            

            
class Shoot(Object):
    def  __init__(self, x, y, r, img, w, h):
        Object.__init__(self, x, y, r, img, w, h)
    def update(self):
        self.y -= 15
        
class Explosion(Object):
    def __init__(self, x, y, r, img, w, h):
        Object.__init__(self, x, y, r, img, w, h)
        self.f = 0
    def update(self):
        if int(self.f) == 11:
            g.explosions.remove(self)
            del self
        self.f = (self.f+0.1)%10
  #  def display(self):
     #   image(img, self.x - self.r, self.y-self.r, self.w, self.h, int(self.f)*self.w, ((int(self.f))%3-1)*self.w, 
        
        
        
        
            
        
        


class Asteroid(Object):
    def __init__(self, x, y, r, img, w, h, health):
        Object.__init__(self, x, y, r, img, w, h)
        self.vy = randint(2, 10)
        self.health = health
    def update(self):
       # g.asteroids.append(g.ast[randint(0,3)])
        self.y += self.vy
        if self.y - 2 * self.r > 720:  #sending asteroid back
            self.y = 0 - randint(100,  350)
            self.x = randint(self.r, 680 - self.r)
            
        if self.distance(g.fighter) <= self.r +g.fighter.r:
             self.y = 0 - randint(100,  350)
             self.x = randint(self.r, 680 - self.r)
             if self.r == 64:
                 g.fighter.health -= 20
             else:
                g.fighter.health -=10
             if  g.fighter.health == 0:
                    g.status = 'gameover'
   
        for i in g.shoots:
            if self.distance(i) <=self.r + i.r:
                self.y = 0 - randint(100,  350)
                self.x = randint(self.r, 680 - self.r)
                g.shoots.remove(i)
          #      g.explotions.append(Explosion((self.x+i.x)*0.5, (self.y+i.y)*0.5, , 'expl.png', 120, 120))
            if i.y < -50:
                g.shoots.remove(i)
                
        
                
                
             
                

        
        
    
    
    def distance(self, f):
        return ((self.x - f.x)**2+(self.y - f.y)**2)**(0.500)
  
   

       

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
        self.shoots = []
        self.ast = []
        self.explosions = []
        self.ast.append(Asteroid(randint(27, self.w - 27), 0 - 50-300, 27, 'ast1.png', 70, 70, 1))
        self.ast.append(Asteroid(randint(64,self.w - 64), 0 - 109-300, 64, 'ast2.png', 170, 184, 3))
        self.ast.append(Asteroid(randint(31, self.w - 31), 0 - 50-300, 34, 'ast3.png', 100, 100, 1))
        self.ast.append(Asteroid(randint(24, self.w - 24), 0 - 44-300, 26, 'ast4.png', 90, 120, 1))
        for i in range(3):
            self.ast.append(Asteroid(randint(24, self.w - 24), 0 - 44-randint(300, 800), 26, 'ast4.png', 90, 120, 1))
            self.ast.append(Asteroid(randint(27, self.w - 27), 0 - 44-randint(300, 800), 27, 'ast1.png', 70, 70, 1))
            self.ast.append(Asteroid(randint(31, self.w - 31), 0 - 50-randint(300, 800), 31, 'ast3.png', 100, 100, 1))

       
        

        



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
        for i in self.shoots:
            i.display()
    #    for i in self.explosions:
     #       i.display()
        
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
        text('Arrows to move. Alt to fire', g.w//4-30, g.h//3+50)
    elif g.status == 'play':
        if not g.pause:
            background(0)
            g.display()
    elif g.status == 'gameover':
         background(0)
         textSize(34)
         text('GAME OVER', g.w//4, g.h//3)
         text('Press shift to restart', g.w//4-30, g.h//3+50)
         
         
        
        
        
    
    
        
    
    
    
    
    
    
def keyPressed():

    if keyCode == ALT:
        g.fighter.keyHandler[ALT] = True
        g.shoots.append(Shoot(g.fighter.x, g.fighter.y, 10, 'shoot.png', 20, 41))
     
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
        if g.status == 'menu':
            g.status = 'play'
        if g.status == 'gameover':
            g.__init__(680, 720)
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
    if keyCode == ALT:
        g.fighter.keyHandler[ALT] = False
    
        
    
    
