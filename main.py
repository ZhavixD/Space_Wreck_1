import pygame
import random
import constants

#=============================================================================
pygame.init()

# Display
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Space Wreck")

# Jugador
player = pygame.Rect(constants.WIDTH // 2 - constants.player_width // 2,
                    constants.HEIGHT - constants.player_height - 10,
                    constants.player_width, constants.player_height)

# Cargar imagenes
player_img = pygame.image.load("ship.png").convert_alpha()
meteor_img = pygame.image.load("meteor.png").convert_alpha()
background_img = pygame.image.load("space.png")

# Define las nuevas dimensiones
player_size = (90, 90) # Nuevo tamaño para la imgaen del jugador
meteor_size = (60, 60) # Nuevo tamaño para la imagen del meteorito

# Redimensiona las imagenes
player_img = pygame.transform.scale(player_img, player_size)
meteor_img = pygame.transform.scale(meteor_img, meteor_size)




# Meteoritos
meteors = []


# Puntuacion
score = 0
font  = pygame.font.Font(None, 36)

# Reloj para controlar FPS
clock = pygame.time.Clock()


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mover el jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < constants.WIDTH:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < constants.HEIGHT:
        player.y += 5
        

    # Generar meteoritos
    if len(meteors) < 7:
        meteor = pygame.Rect(random.randint(0, constants.WIDTH - constants.meteor_width),
                            0, constants.meteor_width, constants.meteor_height)
        meteors.append(meteor)
        
    # Mover los meteoritos
    for meteor in meteors:
        meteor.y += 5
        if meteor.top > constants.HEIGHT:
            meteors.remove(meteor) # Elimina los meteoritos que salen de la pantalla
            score += 1
            
            
    # Detectar colisiones
    for meteor in meteors:
        if player.colliderect(meteor):
            running = False
            print("Game Over!")
    
    screen.fill(constants.BLACK)
    
    screen.blit(background_img, (0, 0))
    
    # pygame.draw.rect(screen, constants.WHITE, player)
    
    screen.blit(player_img, player)
    for meteor in meteors:
        screen.blit(meteor_img, meteor)
        # pygame.draw.rect(screen, constants.RED, meteor)
        
        
    # Mostrar la puntuacion
    score_text = font.render(f"Puntuacion: {score}", True, constants.WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit() # Cierre de Pygame