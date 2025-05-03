from player import Player
from enemy import Enemy
from boss import Boss
import pygame
import random
import sys

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background = pygame.image.load('Assets\space.png')  # Asegúrate de usar la ruta correcta a tu imagen
        self.background = pygame.transform.scale(self.background, (self.width, self.height))  # Escalar la imagen para ajustarla a la pantalla
        player_image = pygame.image.load('Assets\spaceship_yellow.png')
        self.enemy_image=pygame.image.load('Assets\enemies_spaceships.png')
        self.boss_image = pygame.image.load('Assets\enemies_spaceships.png')
        player_image = pygame.transform.scale(player_image, (50, 40))  # Escalar la imagen del jugador
        self.laser_Allie_image = pygame.image.load('Assets\Allie_bullet.png')
        self.laser_Allie_image = pygame.transform.scale(self.laser_Allie_image, (10, 20))
        self.laser_Enemy_image = pygame.image.load('Assets\Enemy_bullet.png')
        self.laser_Enemy_image = pygame.transform.scale(self.laser_Enemy_image, (10, 20))
        self.laser_Boss_image = pygame.image.load('Assets\Boss_bullet.png')
        self.laser_Boss_image = pygame.transform.scale(self.laser_Boss_image, (10, 20))
        self.player = Player(player_image, (width // 2, height - 50), width, self.laser_Allie_image)
        self.enemies = []
        self.boss = None  # Jefe final del tercer nivel
        self.score = 0
        self.running = True
        self.level = 1  # Comenzamos en el nivel 1
        self.podium = pygame.image.load('Assets\podium.png')
        self.podium = pygame.transform.scale(self.podium, (self.width, self.height))

        self.music_tracks = {
            "menu": 'Assets\\Bubblaine - Super Mario Odyssey OST.mp3',
            1: 'Assets\\oye gelda escuchate esta (ultra mega saturado) (online-audio-converter.com).mp3',
            4: 'Assets\\Warriors - League of Legends.mp3',
        }
        
        # Cargar la música
        pygame.mixer.init()  # Inicializa el mezclador de audio
        self.current_music = None  # Para rastrear la música en reproducción
        self.play_music("menu")  # Música del menú

    def play_music(self, track_key):
        """Reproduce la música correspondiente al estado o nivel actual."""
        if track_key in self.music_tracks:
            track = self.music_tracks[track_key]
            if self.current_music != track:  # Cambiar solo si es diferente
                pygame.mixer.music.stop()  # Detener la música actual
                pygame.mixer.music.load(track)  # Cargar la nueva música
                pygame.mixer.music.play(-1)  # Reproducir en bucle
                self.current_music = track  # Actualizar la música actual


    def run(self):
        clock = pygame.time.Clock()

        
        # Inicializa el nivel, score, etc. cada vez que se corre el juego
        self.reset_game()  # Llamada para reiniciar el estado

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)

        # Si el juego termina, mostramos el mensaje de "Win" o "Game Over"
        if not self.running:
            self.game_over_screen()

    def reset_game(self):
        """Reinicia el estado del juego para una nueva partida."""
        self.score = 0
        self.level = 1
        self.running = True
        self.initialize_level(self.level)

    def game_over_screen(self):
        # Mensaje de Game Over o Win
        if self.level > 3:
            message = "You Win!"
        else:
            message = "Game Over!"
        
        self.play_music(4)
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.podium, (0, 0))

        # Mostrar el mensaje final y la puntuación
        font = pygame.font.Font(None, 74)
        score_font = pygame.font.Font(None, 50)
        message_text = font.render(message, True, (255, 255, 255))
        score_text = score_font.render(f"Your Score: {self.score}", True, (255, 255, 255))
        restart_text = score_font.render("Press ENTER to play again", True, (255, 255, 0))
        exit_text = score_font.render("Press ESC to exit", True, (255, 255, 0))

        self.screen.blit(message_text, (self.width // 2 - message_text.get_width() // 2, self.height // 4))
        self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, self.height // 2))
        self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, self.height // 2 + 60))
        self.screen.blit(exit_text, (self.width // 2 - exit_text.get_width() // 2, self.height // 2 + 120))

        pygame.display.flip()

        # Esperamos la acción del jugador para volver al menú o salir
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Si presiona ENTER, reiniciar el juego
                        waiting = False
                        return "menu"  # Volver al menú
                    elif event.key == pygame.K_ESCAPE:  # Si presiona ESC, salir del juego
                        pygame.quit()
                        sys.exit()


    def initialize_level(self, level):
        self.enemies = []
        self.boss = None
        self.play_music(level)  # Cambiar la música según el nivel

        if level == 1:
            self.enemies = [Enemy(random.randint(0, 750), random.randint(50, 200), speed=2, life=1, bullet_speed=5, image=self.enemy_image, laser_image=self.laser_Enemy_image) for _ in range(5)]
        elif level == 2:
            pygame.mixer.music.load('Assets\\oye gelda escuchate esta (ultra mega saturado) (online-audio-converter.com).mp3')  # Ruta a tu archivo de música
            pygame.mixer.music.set_volume(0.3)  # Volumen inicial
            pygame.mixer.music.play(-1)  # Reproducir en bucle
            self.enemies = [Enemy(random.randint(0, 750), random.randint(50, 200), speed=3, life=1, bullet_speed=6, image=self.enemy_image, laser_image=self.laser_Enemy_image) for _ in range(5)]
        elif level == 3:
            self.enemies = [Enemy(random.randint(0, 750), random.randint(50, 200), speed=4, life=1, bullet_speed=7, image=self.enemy_image, laser_image=self.laser_Enemy_image) for _ in range(3)]
            self.boss = Boss(350, 50, speed=2, life=10, bullet_speed=5, image=self.boss_image, screen_width=self.width, laser_image=self.laser_Boss_image)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(laser_sound=pygame.mixer.Sound("Assets\Shot.wav"),laser_image=self.laser_Allie_image)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update(self.height)

        if self.boss:
            self.boss.update(screen_height=600)

        # Colisiones entre los disparos del jugador y los enemigos
        for laser in self.player.lasers:
            for enemy in self.enemies:
                if laser.rect.colliderect(enemy.rect):
                    if enemy.take_damage():
                        self.enemies.remove(enemy)
                    self.player.lasers.remove(laser)
                    self.score += 10
                    break

            if self.boss and laser.rect.colliderect(self.boss.rect):
                if self.boss.take_damage():
                    self.boss = None
                    self.level += 1  # Subimos de nivel tras derrotar al jefe
                self.player.lasers.remove(laser)
                self.score += 50
                break

        # Colisiones entre los disparos de los enemigos/boss y el jugador
        for enemy in self.enemies:
            for laser in enemy.lasers:
                if laser.rect.colliderect(self.player.rect):
                    self.running = False  # Termina el juego si el jugador es golpeado

        if self.boss:
            for laser in self.boss.lasers:
                if laser.rect.colliderect(self.player.rect):
                    self.running = False

        # Si todos los enemigos han sido derrotados y no hay jefe, pasa al siguiente nivel
        if not self.enemies and not self.boss:
            self.level += 1
            if self.level <= 3:
                self.initialize_level(self.level)
            else:
                print("¡Ganaste!")  # Mensaje final
                self.running = False

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        if self.boss:
            self.boss.draw(self.screen)
        self.display_score()
        pygame.display.flip()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

