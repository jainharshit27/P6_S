import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

bulb_state = "on"

clock = pygame.image.load("bulb.png")
clock = pygame.transform.scale(clock, (64, 90)).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if bulb_state == "on":
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        bulb_state = "off"
        if bulb_state == "off":
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bulb_state = "on"
                        
    if bulb_state == "on":
        screen.blit(clock, (50,50))
    else:
        screen.fill((0,0,0))   

    pygame.display.update()