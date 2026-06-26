import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0.0
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player_object.update(dt)
        screen.fill("black")
        player_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        log_state()
    
    

if __name__ == "__main__":
    main()
