import math,pygame

ONE_DEGREE = 0.0174533
class Person():
    def __init__(self,x,y,size,person_color,view_color,ray_color,r,map,map_size_x,map_size_y,cell_size_x,cell_size_y):
        self.x = x
        self.y = y
        self.dir = 0
        self.size = size
        self.color = person_color
        self.view_color = view_color
        self.ray_color = ray_color
        self.r = r
        self.map = map
        self.map_size_x = map_size_x
        self.map_size_y = map_size_y
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.dalpha = 1.5*ONE_DEGREE        #turning speed
        self.dp = 5.0                     #moving speed
        self.cell_list = []
        for i in range(self.map_size_y):
            for j in range(self.map_size_x):
                if self.map[i][j]:
                    self.cell_list.append((cell_size_x*(j+0.5),cell_size_y*(i+0.5)))
    def draw_person(self, screen):
        pygame.draw.circle(screen,self.color,self.get_start(),self.size)
    def draw_direction(self, screen):
        pygame.draw.line(screen,self.view_color,self.get_start(),self.get_end(),2)
    def draw_ray(self, screen):
        RAYS = 360
        angle = self.dir - ONE_DEGREE*(RAYS/2)
        if angle < 0: angle += 2*math.pi
        if angle > 2*math.pi: angle -= 2*math.pi
        size = max(self.map_size_x,self.map_size_y)
        for i in range(RAYS):
            dof = 0
            # looking horizontally
            if angle == 0 or angle == math.pi:
                rx = self.x
                ry = self.y
                dof = 8
            # looking down
            elif angle < math.pi:
                iTan = -1/math.tan(angle)
                ry = int((self.y//self.cell_size_y)*self.cell_size_y)+self.cell_size_y
                rx = (self.y-ry)*iTan + self.x
                y0 = self.cell_size_y
                x0 = -y0*iTan
            # looking up
            elif angle > math.pi:
                iTan = -1/math.tan(angle)
                ry = int((self.y//self.cell_size_y)*self.cell_size_y)-0.0001
                rx = (self.y-ry)*iTan + self.x
                y0 = -self.cell_size_y
                x0 = -y0*iTan
            while dof < size:
                x = int(rx//self.cell_size_x)
                y = int(ry//self.cell_size_y)
                if x >= 0 and y >= 0 and x < self.map_size_x and y < self.map_size_y and self.map[y][x] == 1:
                    dof = size
                else:
                    rx += x0
                    ry += y0
                    dof += 1
            tx,ty = rx,ry   # temp value to compare later, display the shortest ray
            dof = 0
            # looking vertically
            if angle == math.pi/2 or angle == math.pi*3/2:
                rx = self.x
                ry = self.y
                dof = 8
            # looking left
            elif angle > math.pi*3/2 or angle < math.pi/2:
                nTan = -math.tan(angle)
                rx = int((self.x//self.cell_size_x)*self.cell_size_x)+self.cell_size_x
                ry = (self.x-rx)*nTan + self.y
                x0 = self.cell_size_x
                y0 = -x0*nTan
            # looking right
            elif angle > math.pi/2 and angle < math.pi*3/2:
                nTan = -math.tan(angle)
                rx = int((self.x//self.cell_size_x)*self.cell_size_x)-0.0001
                ry = (self.x-rx)*nTan + self.y
                x0 = -self.cell_size_x
                y0 = -x0*nTan
            while dof < size:
                x = int(rx//self.cell_size_x)
                y = int(ry//self.cell_size_y)
                if x >= 0 and y >= 0 and x < self.map_size_x and y < self.map_size_y and self.map[y][x] == 1:
                    dof = size
                else:
                    rx += x0
                    ry += y0
                    dof += 1
            d1 = self.dist(self.x,self.y,tx,ty)
            d2 = self.dist(self.x,self.y,rx,ry)
            if d1 < d2:
                rx,ry = tx,ty
            # pygame.draw.line(screen,(255,0,0),self.get_start(),(tx,ty),5)
            pygame.draw.line(screen,self.ray_color,self.get_start(),(rx,ry))
            angle += ONE_DEGREE
            if angle < 0: angle += 2*math.pi
            if angle > 2*math.pi: angle -= 2*math.pi
    def get_start(self):
        return (self.x,self.y)
    def get_end(self):
        x1,y1 = self.x,self.y
        dx = self.r*math.cos(self.dir)
        dy = self.r*math.sin(self.dir)
        x2,y2 = x1+dx,y1+dy
        return (x2,y2)
    def collide(self,x,y):
        check = False
        for rect in self.cell_list:
            circle_distance_x = abs(x - rect[0])
            circle_distance_y = abs(y - rect[1])
            if circle_distance_x >  (self.size + self.cell_size_x/2): continue
            if circle_distance_y >  (self.size + self.cell_size_y/2): continue
            if circle_distance_x <= (self.cell_size_x/2):
                check = True
                break
            if circle_distance_y <= (self.cell_size_y/2): 
                check = True
                break
            corner_distance = (circle_distance_x - self.cell_size_x/2)**2 + (circle_distance_y - self.cell_size_y/2)**2
            if corner_distance <= (self.size**2): 
                check = True
                break
        return check
    def move_forward(self):
        mx = self.dp*math.cos(self.dir)
        my = self.dp*math.sin(self.dir)
        if not self.collide(self.x+mx,self.y+my):
            self.x += mx
            self.y += my
        elif not self.collide(self.x+mx,self.y):
            self.x += mx
        elif not self.collide(self.x,self.y+my):
            self.y += my

    def move_backward(self):
        mx = -self.dp*math.cos(self.dir)
        my = -self.dp*math.sin(self.dir)
        if not self.collide(self.x+mx,self.y+my):
            self.x += mx
            self.y += my
        elif not self.collide(self.x+mx,self.y):
            self.x += mx
        elif not self.collide(self.x,self.y+my):
            self.y += my
            
    def turn_left(self):
        self.dir -= self.dalpha
        if self.dir <= 0: self.dir = 2*math.pi-self.dalpha
    def turn_right(self):
        self.dir += self.dalpha
        if self.dir >= 2*math.pi: self.dir = self.dalpha
    def dist(self,x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)