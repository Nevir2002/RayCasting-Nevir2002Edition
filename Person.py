import math,pygame
class Person():
    def __init__(self,y,x,size,r,map,map_size):
        self.y = y
        self.x = x
        self.dir = 0
        self.size = size
        self.r = r
        self.map = map
        self.map_size = map_size
        self.dalpha = 0.005     #turning speed
        self.dp = 0.1           #moving speed
    def get_rect(self):
        diff = (self.size-1)//2
        return pygame.Rect(self.x-diff,self.y-diff,self.size,self.size)
    def get_start(self):
        return (self.x,self.y)
    def get_end(self):
        x1,y1 = self.x,self.y
        dx = self.r*math.cos(self.dir)
        dy = self.r*math.sin(self.dir)
        x2,y2 = x1+dx,y1+dy
        return (x2,y2)
    def move_forward(self):
        dx = self.dp*math.cos(self.dir)
        dy = self.dp*math.sin(self.dir)
        self.x += dx
        self.y += dy
    def move_backward(self):
        dx = self.dp*math.cos(self.dir)
        dy = self.dp*math.sin(self.dir)
        self.x -= dx
        self.y -= dy
    def turn_left(self):
        self.dir -= self.dalpha
        if self.dir <= 0: self.dir = 2*math.pi-self.dalpha
    def turn_right(self):
        self.dir += self.dalpha
        if self.dir >= 2*math.pi: self.dir = self.dalpha