import pygame
import sys

pygame.init() 

# Ukuran layar
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Stack Sederhana")

# Warna
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)

clock = pygame.time.Clock()

# Balok awal
blocks = [(200, 700, 200, 30)]  # x, y, width, height

current_x = 0
current_y = 670
current_width = 200
speed = 5
direction = 1

score = 0
font = pygame.font.SysFont(None, 40)

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                last_x, last_y, last_w, last_h = blocks[-1]

                overlap_left = max(current_x, last_x)
                overlap_right = min(current_x + current_width,
                                    last_x + last_w)

                overlap = overlap_right - overlap_left

                if overlap <= 0:
                    print("Game Over!")
                    running = False
                else:
                    blocks.append((overlap_left,
                                   current_y,
                                   overlap,
                                   30))

                    current_width = overlap
                    current_y -= 30
                    current_x = 0
                    score += 1

    # Gerakan balok
    current_x += speed * direction

    if current_x <= 0 or current_x + current_width >= WIDTH:
        direction *= -1

    # Gambar balok yang sudah ditumpuk
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)

    # Gambar balok bergerak
    pygame.draw.rect(screen, RED,
                     (current_x, current_y,
                      current_width, 30))

    # Tampilkan skor
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)