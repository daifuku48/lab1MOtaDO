import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Кольори
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Розміри вікна
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Розміри іподрому та перешкод
TRACK_WIDTH = 800
TRACK_HEIGHT = 400
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 20

# Розміри фінішної прямої
FINISH_LINE_WIDTH = 10
FINISH_LINE_HEIGHT = TRACK_HEIGHT

# Швидкість та сила кіней
HORSE_SPEED = 3
HORSE_STRENGTH = 100

# Ймовірність перестрибнути перешкоду (у відсотках)
JUMP_PROBABILITY = 10


# Клас коня
class Horse(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.original_image = pygame.image.load("/images/horse1.png")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = HORSE_SPEED
        self.strength = HORSE_STRENGTH
        self.consecutive_obstacles = 0  # Лічильник поспільних перешкод

    def update(self):
        self.rect.x += self.speed

        # Перевірка зіткнень з перешкодами
        obstacles_hit = pygame.sprite.spritecollide(self, obstacles, False)
        for obstacle in obstacles_hit:
            if self.rect.colliderect(obstacle.rect):
                if self.rect.y + self.rect.height <= obstacle.rect.y:
                    # Перестрибуємо перешкоду
                    self.rect.y = obstacle.rect.y - self.rect.height
                    self.consecutive_obstacles = 0  # Скидаємо лічильник поспільних перешкод
                elif obstacle == self.obstacle1:
                    # Кінь сповільнюється при зіткненні з другою перешкодою
                    if random.randint(1, 100) <= JUMP_PROBABILITY:  # Рандомна можливість перестрибнути перешкоду
                        self.rect.y = obstacle.rect.y - self.rect.height
                        self.consecutive_obstacles = 0  # Скидаємо лічильник поспільних перешкод
                    else:
                        self.speed = max(0.5, self.speed - 0.5)
                        self.consecutive_obstacles += 1  # Збільшуємо лічильник поспільних перешкод
                elif obstacle == self.obstacle2:
                    # Кінь повністю зходить з дистанції при зіткненні з третьою перешкодою
                    self.consecutive_obstacles += 1  # Збільшуємо лічильник поспільних перешкод
                    if self.consecutive_obstacles >= 3:
                        self.strength = 0

        if self.rect.x >= FINISH_LINE_X:
            # Кінь досяг фінішної прямої - гра завершується
            global winner
            winner = self
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        if self.strength <= 0:
            # Кінь сходить з дистанції, якщо сила досягла 0
            self.speed = 0

    def jump(self):
        # Анімація стрибка
        jump_height = 50
        jump_speed = 5
        for _ in range(jump_height):
            self.rect.y -= jump_speed
            self.image = pygame.transform.scale(self.original_image, (30, 30))
            pygame.time.delay(10)
            pygame.display.flip()
        for _ in range(jump_height):
            self.rect.y += jump_speed
            self.image = pygame.transform.scale(self.original_image, (30, 30))
            pygame.time.delay(10)
            pygame.display.flip()




# Клас перешкоди
class Obstacle(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.original_image = pygame.image.load("obstacle.png")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Створення вікна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Перегони")

# Створення груп спрайтів
all_sprites = pygame.sprite.Group()
horses = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Створення коней та перешкод
for i in range(7):
    horse = Horse(50, i * 60 + 50)
    all_sprites.add(horse)
    horses.add(horse)

    # Створення перешкод на шляху кожного коня
    obstacle1 = Obstacle(random.randint(200, TRACK_WIDTH - 200), horse.rect.y)
    obstacle2 = Obstacle(random.randint(200, TRACK_WIDTH - 200), horse.rect.y + 40)
    obstacle3 = Obstacle(random.randint(200, TRACK_WIDTH - 200), horse.rect.y + 80)
    all_sprites.add(obstacle1)
    all_sprites.add(obstacle2)
    all_sprites.add(obstacle3)
    obstacles.add(obstacle1)
    obstacles.add(obstacle2)
    obstacles.add(obstacle3)

    horse.obstacle1 = obstacle1
    horse.obstacle2 = obstacle2

# Додавання фінішної прямої
FINISH_LINE_X = TRACK_WIDTH + 50
finish_line_image = pygame.image.load("finish.png")
finish_line = finish_line_image.get_rect()
finish_line.x = FINISH_LINE_X
finish_line.height = FINISH_LINE_HEIGHT

clock = pygame.time.Clock()

running = True
winner = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Оновлення спрайтів
    all_sprites.update()

    # Відображення
    window.fill((0, 128, 0))

    pygame.draw.rect(window, WHITE, finish_line)  # Відображення фінішної прямої
    all_sprites.draw(window)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

if winner is not None:
    print("Переміг кінь номер", horses.sprites().index(winner) + 1)
