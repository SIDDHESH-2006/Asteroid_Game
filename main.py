import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0.0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        log_state()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
