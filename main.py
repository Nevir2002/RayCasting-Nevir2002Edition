import pygame,sys
import Person
import Map #contains MAP, SIZE_X, SIZE_Y

def draw_background():
    SCREEN.fill(BACKGROUND_COLOR)
def draw_direction():
    p.draw_direction(SCREEN)
def draw_ray():
    p.draw_ray(SCREEN)
def draw_person():
    draw_ray()
    p.draw_person(SCREEN)
    draw_direction()
def draw_map():
    for i in range(SIZE_Y):
        for j in range(SIZE_X):
            if MAP[i][j]:
                pygame.draw.rect(SCREEN,WALL_COLOR,pygame.Rect(j*CELL_X+1,i*CELL_Y+1,CELL_X-2,CELL_Y-2))

# initiate
SCREEN_X = 1600
SCREEN_Y = 900
SIZE_X = Map.SIZE_X
SIZE_Y = Map.SIZE_Y
CELL_X = SCREEN_X//SIZE_X
CELL_Y = SCREEN_Y//SIZE_Y
MAP = Map.MAP
BACKGROUND_COLOR = (100,100,100)
PLAYER_COLOR = (255,255,0)
VIEW_COLOR = (255,0,0)
RAY_COLOR = (30,200,200)
WALL_COLOR = (255,255,255)

# draw screen and set controller keys
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
pygame.display.set_caption("Ray-casting by Nevir2002")
p = Person.Person(x=250,y=250,size=20,person_color=PLAYER_COLOR,view_color=VIEW_COLOR,ray_color=RAY_COLOR,r=30,map=MAP,map_size_x=SIZE_X,map_size_y=SIZE_Y,cell_size_x=CELL_X,cell_size_y=CELL_Y)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_w]:
        p.move_forward()
    if keys[pygame.K_s]:
        p.move_backward()
    if keys[pygame.K_a]:
        p.turn_left()
    if keys[pygame.K_d]:
        p.turn_right()
    draw_background()
    draw_map()
    draw_person()
    pygame.display.update()