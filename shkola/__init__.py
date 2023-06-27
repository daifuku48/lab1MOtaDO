import pygame
import random

from pygame import Rect

# Ініціалізація Pygame
pygame.init()

# Кольори
WHITE = (0, 0, 0)
RED = (255, 0, 0)

# Розміри вікна
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Розміри іподрому та перешкод
TRACK_WIDTH = 800
TRACK_HEIGHT = 400
OBSTACLE_WIDTH = 10
OBSTACLE_HEIGHT = 10

# Розміри фінішної прямої
FINISH_LINE_WIDTH = 10
FINISH_LINE_HEIGHT = TRACK_HEIGHT

# Швидкість та сила кіней
HORSE_SPEED = 2
HORSE_STRENGTH = 100

# Ймовірність перестрибнути перешкоду (у відсотках)
JUMP_PROBABILITY = 50


# Клас коня
class NewHorse:
    def __init__(self, x, y, width, height, collidersX, collidersY):
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
        self.width = width
        self.height = height
        self.vel = 5  # скорость передвижения
        self.is_jump = False
        self.jump_count = 10
        self.walk_count = 0
        self.left = False
        self.right = False
        self.standing = True
        self.jump_height = 20
        self.is_throw = False
        self.jump_vel = 40
        self.walk_right = pygame.image.load("images\horse1.png")
        self.stand = pygame.image.load("images\horse1.png")
        self.image = self.stand
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.orientation = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.win = False
        self.collidersX = collidersX
        self.collidersY = collidersY

    def move_right(self):
        self.x += self.vel

    def jump(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 10
        if self.jump_vel < -40:
            self.is_jump = False
            self.jump_vel = 40

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_win(self):
        self.win = True
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        self.x += self.vel
        if self.x == self.collidersX and self.collidersY == self.y + 20:
            if random.randint(1, 100) <= JUMP_PROBABILITY:
                self.is_jump = True
            else:
                self.vel = random.randint(1, 3)

    def is_win(self):
        self.win = True
        pygame.event.post(pygame.event.Event(pygame.QUIT))


class Player:
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
        self.width = width
        self.height = height
        self.vel = 10  # скорость передвижения
        self.is_jump = False
        self.jump_count = 10
        self.walk_count = 0
        self.left = False
        self.right = False
        self.standing = True
        self.jump_height = 20
        self.is_throw = False
        self.jump_vel = 40
        self.walk_right = pygame.image.load("images\horse1.png")
        self.stand = pygame.image.load("images\horse1.png")
        self.image = self.stand
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.orientation = True
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.win = False

    def move_right(self):
        self.x += self.vel

    def jump(self):
        self.is_jump = True

    def jump_move(self):
        self.y -= self.jump_vel
        self.jump_vel -= 10
        if self.jump_vel < -40:
            self.is_jump = False
            self.jump_vel = 40

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_win(self):
        self.win = True
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def check(self):
        if self.x == 400 and self.y + 20 == 420:
            self.vel = 1

# Клас перешкоди
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load("images/obstacle.png")
        self.image = self.original_image.copy()
        self.rect = Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Створення вікна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Перегони")

player = Player(30, 420, 50, 50)
obstaclePl = Obstacle(400, 440)

horse1 = NewHorse(30, 50, 50, 50, 500, 70)
obstacle1 = Obstacle(500, 70)

horse2 = NewHorse(30, 100, 50, 50, 400, 120)
obstacle2 = Obstacle(400, 120)

horse3 = NewHorse(30, 150, 50, 50, 300, 170)
obstacle3 = Obstacle(300, 170)

horse4 = NewHorse(30, 200, 50, 50, 450, 220)
obstacle4 = Obstacle(450, 220)

horse5 = NewHorse(30, 300, 50, 50, 370, 320)
obstacle5 = Obstacle(370, 320)

horse6 = NewHorse(30, 350, 50, 50, 600, 380)
obstacle6 = Obstacle(600, 370)

# Додавання фінішної прямої
FINISH_LINE_X = 830
finish_line_image = pygame.image.load("images/finish.png")
finish_line = finish_line_image.get_rect()
finish_line.x = FINISH_LINE_X
finish_line.height = FINISH_LINE_HEIGHT

clock = pygame.time.Clock()

running = True
winner = None
while running:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.move_right()

    if keys[pygame.K_UP] and not player.is_jump:
        player.jump()

    if player.is_jump:
        player.jump_move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if player.x == 830:
        player.is_win()

    if horse1.x == 830:
        horse1.is_win()

    if horse2.x == 830:
        horse2.is_win()

    if horse3.x == 830:
        horse3.is_win()

    if horse4.x == 830:
        horse4.is_win()

    if horse5.x == 830:
        horse5.is_win()

    if horse6.x == 830:
        horse6.is_win()

    # Відображення
    window.fill((0, 128, 0))
    player.draw(window)
    pygame.draw.rect(window, WHITE, Rect(900, 0, 20, 600))  # Відображення фінішної прямої
    obstacle1.draw(window)
    obstaclePl.draw(window)
    horse1.draw(window)
    horse1.update()
    obstacle1.draw(window)
    horse2.draw(window)
    horse2.update()
    obstacle2.draw(window)
    horse3.draw(window)
    horse3.update()
    obstacle3.draw(window)
    horse4.draw(window)
    horse4.update()
    obstacle4.draw(window)
    horse5.draw(window)
    horse5.update()
    obstacle5.draw(window)
    horse6.draw(window)
    horse6.update()
    obstacle6.draw(window)
    pygame.display.flip()

    if horse1.is_jump:
        horse1.jump_move()

    if horse2.is_jump:
        horse2.jump_move()

    if horse3.is_jump:
        horse3.jump_move()

    if horse4.is_jump:
        horse4.jump_move()

    if horse5.is_jump:
        horse5.jump_move()

    if horse6.is_jump:
        horse6.jump_move()

    player.check()

    clock.tick(20)

pygame.quit()

if horse1.win:
    print("Переміг кінь номер", 1)
elif horse2.win:
    print("Переміг кінь номер", 2)
elif horse3.win:
    print("Переміг кінь номер", 3)
elif horse4.win:
    print("Переміг кінь номер", 4)
elif horse5.win:
    print("Переміг кінь номер", 5)
elif horse6.win:
    print("Переміг кінь номер", 6)
elif player.win:
    print("Переміг кінь номер", 7)
