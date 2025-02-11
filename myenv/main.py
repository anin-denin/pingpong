import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Buat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pong")

# Load gambar latar belakang
background_image = pygame.image.load("background.jpg").convert()

# Paddle dan Bola
paddle_left = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 40, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Kecepatan bola
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Skor
score_left = 0
score_right = 0
font = pygame.font.Font(None, 36)

# Fungsi utama game
def main():
    global ball_speed_x, ball_speed_y, score_left, score_right

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Kontrol Paddle Pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_left.top > 0:
            paddle_left.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
            paddle_left.y += PADDLE_SPEED

        # Gerakan Paddle Komputer
        if paddle_right.centery < ball.centery and paddle_right.bottom < HEIGHT:
            paddle_right.y += PADDLE_SPEED
        if paddle_right.centery > ball.centery and paddle_right.top > 0:
            paddle_right.y -= PADDLE_SPEED

        # Gerakan Bola
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Cek tabrakan dengan dinding
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Cek tabrakan dengan paddle
        if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
            ball_speed_x = -ball_speed_x

        # Cek jika bola keluar dari layar
        if ball.left <= 0:
            score_right += 1  # Komputer mendapatkan poin
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x = BALL_SPEED_X
            ball_speed_y = BALL_SPEED_Y
        if ball.right >= WIDTH:
            score_left += 1  # Pemain mendapatkan poin
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x = -BALL_SPEED_X
            ball_speed_y = BALL_SPEED_Y

        # Gambar
        screen.blit(background_image, (0, 0))  # Gambar latar belakang
        pygame.draw.rect(screen, WHITE, paddle_left)
        pygame.draw.rect(screen, WHITE, paddle_right)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Tampilkan skor
        score_text = font.render(f"{score_left} - {score_right}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        pygame.display.flip()
        pygame.time.delay(30)

# Jalankan game
if __name__ == "__main__":
    main()