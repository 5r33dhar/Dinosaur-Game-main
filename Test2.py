import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Font Test")

# Use a system font instead of external file
game_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")

    # Render some text
    text_surface = game_font.render("Hello, Dino!", True, "black")
    text_rect = text_surface.get_rect(center=(320, 240))
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)