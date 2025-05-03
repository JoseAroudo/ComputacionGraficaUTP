import pygame
import sys
from game import Game  # Importa la clase de tu juego
from menu import Menu  # Importa la clase del menú

# Definir el tamaño de la pantalla
WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")

    # Pasar el tamaño de la pantalla al menú y al juego
    menu = Menu(screen, WIDTH, HEIGHT)
    game = Game(screen, WIDTH, HEIGHT)

    while True:
        action = menu.show_menu()

        if action == "play":
            game.run()  # Corre el juego si se elige jugar
        elif action == "exit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()