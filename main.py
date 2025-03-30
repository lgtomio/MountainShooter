import pygame

print('Inicio do Programa')
pygame.init()
window = pygame.display.set_mode(size=(600, 600))
print('Fim do Programa')

print('Início do Loop')
while True:
    # Check for all avents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit() # end pygame