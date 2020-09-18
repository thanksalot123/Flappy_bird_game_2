import pygame, sys, random

brd_mov=200

game_active=True


def  cr_brd():
    random_brd_hgt = random.choice(brd_height)
    brd_evl = bg_brd_bd.get_rect(center = (900,random_brd_hgt))
    return brd_evl

def move_brd(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes    

def draw_brd(pipes):
    for pipe in pipes:
        flip_pipe = pygame.transform.flip(bg_brd_bd,True,False)
        screen.blit(flip_pipe,pipe)


#########################################################
#Bird collision and it was damn hard for me

def brd_coll(pipes,plumbs):
    for pipe in pipes:
        for plumb in plumbs:
            if pipe.colliderect(plumb):
                pipes.remove(pipe)
                plumbs.remove(plumb)



#########################################################

def draw_floor():
    screen.blit(bg_base,(pos_x,400))
    screen.blit(bg_base,(pos_x+376,400))

def  cr_brd_gd(pos):
    brd_evl = bg_brd_bd.get_rect(center = (60,pos))
    return brd_evl

def move_brd_gd(pipes):
    for pipe in pipes:
        pipe.centerx+=5
    return pipes    

def draw_brd_gd(pipes):
    for pipe in pipes:
        screen.blit(bg_brd_gd,pipe)
  
def check_coll(pipes):
    for pipe in pipes:
        if wall_rect.colliderect(pipe):
            return False
    return True


pygame.init()




screen = pygame.display.set_mode((876,500))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('F:/games_by_ME/assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(876,500))
bg_base = pygame.image.load('F:/games_by_ME/assets/sprites/base.png').convert()
bg_base = pygame.transform.scale(bg_base, (876,100))
pos_x=0

bg_brd_gd = pygame.image.load('F:/games_by_ME/assets/sprites/bluebird-midflap.png').convert()
bg_brd_gd = pygame.transform.scale(bg_brd_gd,(45,33))
bird_rect = bg_brd_gd.get_rect(center = (60,200))
fire_brd = []

game_ovr = pygame.image.load('F:/games_by_ME/assets/sprites/gameover.png').convert()
game_ovr = pygame.transform.scale(game_ovr,(270,100))


ref_wall = pygame.image.load('F:/games_by_ME/assets/sprites/pipe-green.png')
ref_wall = pygame.transform.scale(ref_wall,(5,900))
wall_rect = ref_wall.get_rect(midtop = (-2,0))

bg_brd_bd = pygame.image.load('F:/games_by_ME/assets/sprites/redbird-midflap.png').convert()
bg_brd_bd = pygame.transform.scale(bg_brd_bd,(45,33))
brd_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1100)
brd_height = [50,100,150,200,250,300,350,370]

while True:
    for event in pygame.event.get(): #event loop in pyhton it just knows all the event
        if event.type == pygame.QUIT: #to identify quit event
            pygame.quit() #quit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if brd_mov >= 50:
                    brd_mov-=50
            if event.key == pygame.K_DOWN:
                if brd_mov <= 300:
                    brd_mov+=50        
            if event.key == pygame.K_SPACE:
                fire_brd.append(cr_brd_gd(brd_mov))
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                brd_list.clear()
                fire_brd.clear()
                bird_rect.center = (60,200)
                brd_mov = 200


        if event.type == SPAWNPIPE:
            brd_list.append(cr_brd())


    screen.blit(bg_surface,(0,0))
    screen.blit(ref_wall,wall_rect)
    pos_x-=1
    if game_active:
        screen.blit(bg_brd_gd,bird_rect)
        bird_rect.centery = brd_mov
        fire_brd=move_brd_gd(fire_brd)
        draw_brd_gd(fire_brd) 
        brd_list=move_brd(brd_list)
        draw_brd(brd_list)
        brd_coll(fire_brd,brd_list)
        game_active = check_coll(brd_list)
    if game_active == False:
        screen.blit(game_ovr,(300,100))
    draw_floor()    
    if pos_x <= -376:
        pos_x=0
    pygame.display.update()
    clock.tick(90)