import math,pygame
class Person():
    def __init__(self,x,y,size,person_color,view_color,ray_color,r,map,map_size,cell_size):
        self.x = x
        self.y = y
        self.dir = 1
        self.size = size
        self.color = person_color
        self.view_color = view_color
        self.ray_color = ray_color
        self.r = r
        self.map = map
        self.map_size = map_size
        self.cell_size = cell_size
        self.dalpha = 0.005     #turning speed
        self.dp = 0.2           #moving speed
    def draw_person(self, screen):
        pygame.draw.circle(screen,self.color,self.get_start(),20)
    def draw_direction(self, screen):
        pygame.draw.line(screen,self.view_color,self.get_start(),self.get_end(),2)
    def draw_ray(self, screen):
        dof = 0
        # looking down
        if self.dir < math.pi:
            iTan = -1/math.tan(self.dir)
            ry = int((self.y//self.cell_size)*self.cell_size)+self.cell_size
            rx = (self.y-ry)*iTan + self.x
            y0 = self.cell_size
            x0 = -y0*iTan
        # looking horizontally
        elif self.dir == 0 or self.dir == math.pi:
            rx = self.x
            ry = self.y
            dof = 8
        # looking up
        elif self.dir > math.pi:
            iTan = -1/math.tan(self.dir)
            ry = int((self.y//self.cell_size)*self.cell_size)-0.0001
            rx = (self.y-ry)*iTan + self.x
            y0 = -self.cell_size
            x0 = -y0*iTan
        while dof < self.map_size:
            x = int(rx//self.cell_size)
            y = int(ry//self.cell_size)
            if x >= 0 and y >= 0 and x < self.map_size and y < self.map_size and self.map[y][x] == 1:
                dof = self.map_size
            else:
                rx += x0
                ry += y0
                dof += 1
        x,y = rx,ry 
        # current ray

        dof = 0
        # looking left
        if self.dir > math.pi/2 and self.dir < math.pi*3/2:
            nTan = -math.tan(self.dir)
            rx = int((self.x//self.cell_size)*self.cell_size)+self.cell_size
            ry = (self.x-rx)*nTan + self.y
            x0 = self.cell_size
            y0 = -x0*nTan
        # looking vertically
        elif self.dir == math.pi/2 or self.dir == math.pi*3/2:
            rx = self.x
            ry = self.y
            dof = 8
        # looking right
        elif self.dir > math.pi*3/2 or self.dir < math.pi/2:
            nTan = -math.tan(self.dir)
            rx = int((self.x//self.cell_size)*self.cell_size)-0.0001
            ry = (self.x-rx)*nTan + self.y
            x0 = -self.cell_size
            y0 = -x0*nTan
        while dof < self.map_size:
            x = int(rx//self.cell_size)
            y = int(ry//self.cell_size)
            if x >= 0 and y >= 0 and x < self.map_size and y < self.map_size and self.map[y][x] == 1:
                dof = self.map_size
            else:
                rx += x0
                ry += y0
                dof += 1
        if self.dist(self.x,self.y,x,y) > self.dist(self.x,self.y,rx,ry):
            x,y = rx,ry
        pygame.draw.line(screen,self.ray_color,self.get_start(),(rx,ry))
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
    def dist(self,x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)