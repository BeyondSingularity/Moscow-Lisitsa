import pygame

pygame.init()
width, height = map(int, input().split())
size = (width, height)
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("black"))

pygame.draw.line(screen, pygame.Color("white"), (0, 0), (width, height), 5)
pygame.draw.line(screen, pygame.Color("white"), (width, 0), (0, height), 5)

pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
