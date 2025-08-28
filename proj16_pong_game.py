import pygame, sys, random

print("Python Project # 16 - Pong")
print("Welcome To Pong Game!")
print("Let\s Play The Game!")

def reset_ball():
  global ball_speed_x, ball_speed_y
  ball.x = screen_width // 2 - 10
  ball.y = random.randint(10, 100)
  ball_speed_y = 6 * random.choice((1, -1))
  ball_speed_x = 6 * random.choice((1, -1))

def point_won(winner):
  global player_points, cpu_points
  if winner == "Player":
    player_points += 1
  elif winner == "CPU":
    cpu_points += 1

  reset_ball()

def animate_ball():
  global ball_speed_x, ball_speed_y
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1

  if ball.right >= screen_width:
    point_won("CPU")
  
  if ball.left <= 0:
    point_won ("Player")

  if ball.colliderect(player) or ball.colliderect(cpu):
    ball_speed_x *= -1

def animate_player():
  player.y += player_speed

  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

def animate_cpu():
  global cpu_speed
  cpu.y += cpu_speed
  if ball.centery <= cpu.centery:
    cpu_speed = -6
  elif ball.centery >= cpu.centery:
    cpu_speed = 6

  if cpu.top <= 0:
    cpu.top = 0
  if cpu.bottom >= screen_height:
    cpu.bottom = screen_height

pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!")

clock = pygame.time.Clock()

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (screen_width // 2, screen_height // 2)

cpu = pygame.Rect(0, 0, 20, 100)
cpu.center = (50, screen_height // 2)

player = pygame.Rect(0, 0, 20, 100)
player.midright = (screen_width - 10, screen_height // 2)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6

cpu_points, player_points = 0, 0
max_points = 5

score_font = pygame.font.Font('freesansbold.ttf', 32)

while True:
  for event in pygame.event.get():
    if event.type == pygame.quit:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_speed = -6
      if event.key == pygame.K_DOWN:
        player_speed = 6
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        player_speed = 0
      if event.key == pygame.K_DOWN:
        player_speed = 0

  animate_ball()
  animate_player()
  animate_cpu()

  screen.fill('black')

  cpu_score_surface = score_font.render(f"{cpu_points}", True, 'white')
  player_score_surface = score_font.render(f"{player_points}", True, 'white')

  screen.blit(cpu_score_surface, (screen_width // 4, 20))
  screen.blit(player_score_surface, (screen_width * 3 // 4, 20))

  pygame.draw.aaline(screen, 'white', (screen_width // 2, 0), (screen_width // 2, screen_height))
  pygame.draw.ellipse(screen, 'white', ball)
  pygame.draw.rect(screen, 'white', cpu)
  pygame.draw.rect(screen, 'white', player)

  pygame.display.update()
  clock.tick(60)

  if player_points >= max_points or cpu_points >= max_points:
        print(f"Final Score -> Player: {player_points} Points, CPU: {cpu_points} Points")
        pygame.quit()
        sys.exit()
