import pygame
import random
import math
from pygame import mixer

print("\nPython Project # 25 - Space Invaders Game")
print("Welcome To Space Invaders Game!")
print("Lets Play Game....")

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

background = pygame.image.load('background.jpg')

mixer.music.load('game-music-loop-7-145285.mp3')
mixer.music.play(-1)

laser_sound = mixer.Sound('mixkit-laser-gun-shot-3110.wav')

game_over_sound = mixer.Sound('diamond_outro-332861.mp3')
game_over_sound_played = False

pygame.display.set_caption("Space Invaders Game")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('spaceship1.png')
playerX = 550
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)
menu_font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 200))
    menu_text = menu_font.render("Press R to Play Again or Q to Quit", True, (255, 255, 255))
    screen.blit(menu_text, (100, 300))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

running = True
game_over = False

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        laser_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
            else:
                if event.key == pygame.K_r:
                    score_value = 0
                    playerX = 550
                    bulletY = 480
                    bullet_state = "ready"
                    enemyX = [random.randint(0, 736) for _ in range(num_of_enemies)]
                    enemyY = [random.randint(50, 150) for _ in range(num_of_enemies)]
                    game_over = False
                    game_over_sound_played = False
                if event.key == pygame.K_q:
                    print("\nGame Over!!!")
                    print(f"Final Score: {score_value}")
                    running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if not game_over:
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for i in range(num_of_enemies):

            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over = True
                
                if not game_over_sound_played:
                    game_over_sound.play()
                    game_over_sound_played = True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)

    else:
        game_over_text()

    pygame.display.update()
    clock.tick(60)
