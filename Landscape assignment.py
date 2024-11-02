import pygame


pygame.init()

WIDTH = 1280
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
forground = 200
background = 200
sun_xaxis = 100
sun_yaxis = 100
sun_radius = 70
moon_xaxis = 100
moon_yaxis = 100
moon_radius = 70
eye_radius = 3
triangle_width = 10
triangle_height = 10
flower_rows = [275, 370, 465] 
flower_count = 15
flower_spacing = WIDTH // (flower_count + 1)
flower_y = 275
petal_radius = 15
flower_center_radius = 10
stem_length = 50 
cloud_x = 200
cloud_x1 = cloud_x
cloud_x2 = cloud_x +200
cloud_x3 = cloud_x +350
cloud_x4 = cloud_x + 500
cloud_x5 = cloud_x + 615
ghost_moving_x = 10
cloud_positions = [(200, 100), (500, 150), (800, 120), (1000, 80)] 

Day_background = True
night_background = False
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    if sun_xaxis < WIDTH + sun_radius:
        sun_xaxis += 4
    if cloud_x1 < WIDTH + cloud_x:
        cloud_x1 += 2
        if cloud_x1  > WIDTH:
            cloud_x1 = 0
    if cloud_x2 < WIDTH + cloud_x:
        cloud_x2 += 2
        if cloud_x2  > WIDTH:
            cloud_x2 = 0
    if cloud_x3 < WIDTH + cloud_x:
        cloud_x3 += 2
        if cloud_x3  > WIDTH:
            cloud_x3 = 0

    if cloud_x4 < WIDTH + cloud_x:
        cloud_x4 += 2
        if cloud_x4  > WIDTH:
            cloud_x4 = 0

    if cloud_x5 < WIDTH + cloud_x:
        cloud_x5 += 2
        if cloud_x5  > WIDTH:
            cloud_x5 = 0
    
    if ghost_moving_x < WIDTH +ghost_moving_x:
        ghost_moving_x+=2 
        if ghost_moving_x > WIDTH:
            ghost_moving_x = 0 
    
    

    # DRAWING

    screen.fill((255, 255, 255))  # always the first drawing command




    if Day_background == True:
        background = pygame.draw.rect(screen, (173, 216, 230), (0,0,1280,250))
        forground = pygame.draw.rect(screen, (0,128,0), (0,250,1280, 350 ))
        sun = pygame.draw.circle(screen, (255, 255, 0), (sun_xaxis, sun_yaxis), sun_radius)
        # flowers
        for row in range(len(flower_rows)):
            flower_y = flower_rows[row] 
            for i in range(flower_count):
                flower_x = (i + 1) * flower_spacing
                flower_x = (i + 1) * flower_spacing
                pygame.draw.line(screen, ( 1,50,32), (flower_x, flower_y), (flower_x, flower_y + stem_length), 5) 
                pygame.draw.circle(screen, (255, 192, 203), (flower_x - petal_radius, flower_y), petal_radius)
                pygame.draw.circle(screen, (255, 192, 203), (flower_x + petal_radius, flower_y), petal_radius)
                pygame.draw.circle(screen, (255, 192, 203), (flower_x, flower_y - petal_radius), petal_radius)
                pygame.draw.circle(screen, (255, 192, 203), (flower_x, flower_y + petal_radius), petal_radius)
                pygame.draw.circle(screen, (255, 255, 0), (flower_x, flower_y), flower_center_radius)
    

        if sun_xaxis > WIDTH + sun_radius:
            background = pygame.draw.rect(screen, (0, 0, 0), (0,0,1280,250))
            forground = pygame.draw.rect(screen, (0,128,0), (0,250,1280, 350 ))
            moon = pygame.draw.circle(screen, (255, 255, 255), (moon_xaxis, moon_yaxis), moon_radius)
            dark_circle_covering_moon = moon_radius // 2 
            pygame.draw.circle(screen, (0, 0, 0), (moon_xaxis + dark_circle_covering_moon, moon_yaxis), moon_radius)
            night_background = True

    if night_background == True:
        
        # graves 
        for x in range(10,1280, 350):
            pygame.draw.rect(screen, (128,128,128), (x - 30,300,60, 75 ))
            pygame.draw.circle(screen,(128,128,128),(x,300),30)
            # ghost
            ghost_x = x + 80 
            pygame.draw.rect(screen, (225,225,225), (ghost_x, 315, 30, 30))
            pygame.draw.circle(screen, (225,225,225), (ghost_x + 15, 320), 15)
            pygame.draw.circle(screen, (0, 0, 0), (ghost_x + 10, 325), eye_radius)
            pygame.draw.circle(screen, (0, 0, 0), (ghost_x + 20, 325), eye_radius)
            for i in range(3):  # Create three triangles at the bottom of the ghost
                pygame.draw.polygon(screen, (225,225,225), [
                (ghost_x + i * triangle_width, 345),
                (ghost_x + i * triangle_width + triangle_width // 2, 345 + triangle_height),
                (ghost_x + (i + 1) * triangle_width, 345)])
        for x in range(100,1280, 350):
            pygame.draw.rect(screen, (128,128,128), (x - 30,500,60, 75 ))
            pygame.draw.circle(screen,(128,128,128),(x,500),30)
            # ghost
            ghost_x = x + 80 
            pygame.draw.rect(screen, (225, 225, 225), (ghost_x, 515, 30, 30))
            pygame.draw.circle(screen, (225, 225, 225), (ghost_x + 15, 520), 15)
            eye_radius = 3
            pygame.draw.circle(screen, (0, 0, 0), (ghost_x + 10, 525), eye_radius)
            pygame.draw.circle(screen, (0, 0, 0), (ghost_x + 20, 525), eye_radius)
            for i in range(3):  # Create three triangles at the bottom of the ghost
                pygame.draw.polygon(screen, (225, 225, 225), [
                    (ghost_x + i * triangle_width, 545),
                    (ghost_x + i * triangle_width + triangle_width // 2, 545 + triangle_height),
                    (ghost_x + (i + 1) * triangle_width, 545)
                ])

    # moving ghost
    pygame.draw.rect(screen, (225, 225, 225), (ghost_moving_x, 240, 30, 30))
    pygame.draw.circle(screen, (225, 225, 225), (ghost_moving_x + 15,240 - 5), 15)
    pygame.draw.circle(screen, (0, 0, 0), (ghost_moving_x + 10, 240 - 5), eye_radius)
    pygame.draw.circle(screen, (0, 0, 0), (ghost_moving_x + 20, 240 - 5), eye_radius)
    for i in range(3):  
        pygame.draw.polygon(screen, (225, 225, 225), [
            (ghost_moving_x + i * triangle_width, 240 + 30),
            (ghost_moving_x + i * triangle_width + triangle_width // 2, 240 + 30 + triangle_height),
            (ghost_moving_x + (i + 1) * triangle_width, 240 + 30)
        ])
    # clouds
    pygame.draw.rect(screen,(200,200,200), (cloud_x1, 100 + 20, 80, 30))
    pygame.draw.circle(screen, (200,200,200), (cloud_x1 + 10, 100 + 20), 20)
    pygame.draw.circle(screen, (200,200,200), (cloud_x1 + 30, 100), 25)
    pygame.draw.circle(screen, (200,200,200), (cloud_x1 + 50, 100 + 10), 30)
    pygame.draw.circle(screen, (200,200,200), (cloud_x1 + 70, 100 + 20), 20)

    pygame.draw.rect(screen,(200,200,200), (cloud_x2 , 170 + 20, 80, 30))
    pygame.draw.circle(screen, (200,200,200), (cloud_x2 + 10, 170 + 20), 20)
    pygame.draw.circle(screen, (200,200,200), (cloud_x2 +30, 170), 25)
    pygame.draw.circle(screen, (200,200,200), (cloud_x2 +50, 170 + 10), 30)
    pygame.draw.circle(screen, (200,200,200), (cloud_x2 +70, 170 + 20), 20)

    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x3 - 15, 70, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x3, 70, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x3 + 20, 70, 60, 40))         
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x3 + 50, 70 + 10, 40, 30))  

    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x4 - 15, 30, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x4, 30, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x4 + 20, 30, 60, 40))         
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x4 + 50, 30 + 10, 40, 30)) 
    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x5 - 15, 190, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x5, 190, 50, 40))    
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x5 + 20, 190, 60, 40))         
    pygame.draw.ellipse(screen, (200, 200, 200), (cloud_x5 + 50, 190 + 10, 40, 30)) 



    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()