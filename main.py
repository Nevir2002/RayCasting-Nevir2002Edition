import pygame,sys
import Person
import Map

def draw_background():
    SCREEN.fill(BACKGROUND_COLOR)
def draw_direction():
    pygame.draw.line(SCREEN,RAY_COLOR,p.get_start(),p.get_end())
def draw_person():
    pygame.draw.rect(SCREEN,PLAYER_COLOR,p.get_rect())
    draw_direction()
def draw_map():
    for i in range(SIZE):
        for j in range(SIZE):
            if MAP[i][j]:
                pygame.draw.rect(SCREEN,WALL_COLOR,pygame.Rect(j*CELL_SIZE+1,i*CELL_SIZE+1,CELL_SIZE-2,CELL_SIZE-2))

# initiate
CELL_SIZE = 100
SIZE = Map.SIZE
MAP = Map.MAP
BACKGROUND_COLOR = (100,100,100)
PLAYER_COLOR = (255,255,0)
RAY_COLOR = (255,0,0)
WALL_COLOR = (255,255,255)

pygame.init()
# SCREEN = pygame.display.set_mode((SIZE*CELL_SIZE,SIZE*CELL_SIZE))
SCREEN = pygame.display.set_mode((800,800))
pygame.display.set_caption("Ray-casting by Nevir2002")
p = Person.Person(250,250,51,100,MAP,SIZE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
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