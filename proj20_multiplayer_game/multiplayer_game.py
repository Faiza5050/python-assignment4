import pygame
from network import Network

pygame.font.init()

print("Python Project #20 - Online Multiplayer Game")
print("Welcome To The Online Multiplayer Game!")
print("Let's Play Game!!!")

width = 650
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Paper Scissors")

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (220, 20, 60)
GREEN = (34, 139, 34)
BLUE = (30, 144, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 215, 0)


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 160
        self.height = 90

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), border_radius=12)
        font = pygame.font.SysFont("comicsans", 35, bold=True)
        text = font.render(self.text, True, WHITE)
        win.blit(text, (self.x + self.width//2 - text.get_width()//2,
                        self.y + self.height//2 - text.get_height()//2))

    def click(self, pos):
        x1, y1 = pos
        return self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height


def redrawWindow(win, game, p):
    win.fill(GRAY)

    if not game.connected():
        font = pygame.font.SysFont("comicsans", 70, bold=True)
        text = font.render("Waiting for Player...", True, RED)
        win.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
    else:
        font = pygame.font.SysFont("comicsans", 55, bold=True)
        title = font.render("Rock Paper Scissors", True, YELLOW)
        win.blit(title, (width//2 - title.get_width()//2, 40))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        left_x = 50
        right_x = 350
        label_y = 280
        move_y = 350

        if game.bothWent():
            text1 = font.render(move1, True, GREEN)
            text2 = font.render(move2, True, GREEN)
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, True, GREEN)
            elif game.p1Went:
                text1 = font.render("Locked In", True, BLUE)
            else:
                text1 = font.render("Waiting...", True, RED)

            if game.p2Went and p == 1:
                text2 = font.render(move2, True, GREEN)
            elif game.p2Went:
                text2 = font.render("Locked In", True, BLUE)
            else:
                text2 = font.render("Waiting...", True, RED)

        if p == 0:
            myMove = font.render("Your Move", True, BLUE)
            oppMove = font.render("Opponent", True, RED)
            win.blit(myMove, (left_x, label_y))
            win.blit(oppMove, (right_x, label_y))
            win.blit(text1, (left_x, move_y))
            win.blit(text2, (right_x, move_y))
        else:
            myMove = font.render("Your Move", True, BLUE)
            oppMove = font.render("Opponent", True, RED)
            win.blit(myMove, (left_x, label_y))
            win.blit(oppMove, (right_x, label_y))
            win.blit(text2, (left_x, move_y))
            win.blit(text1, (right_x, move_y))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [
    Button("Rock", 40, 480, BLACK),
    Button("Scissors", 220, 480, RED),
    Button("Paper", 400, 480, GREEN)
]


def main():
    run = True
    n = Network()
    p = int(n.getP())
    clock = pygame.time.Clock()
    print("You are Player", p)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            print("Couldn't Get Game")
            break

        if game.bothWent():
            redrawWindow(win, game, p)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                break

            font = pygame.font.SysFont("comicsans", 90, bold=True)
            if game.winner() == -1:
                text = font.render("Tie Game!", True, YELLOW)
            elif game.winner() == p:
                text = font.render("You Won!", True, GREEN)
            else:
                text = font.render("You Lost...", True, RED)

            win.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2 - 80))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if p == 0 and not game.p1Went:
                            n.send(btn.text)
                        elif p == 1 and not game.p2Went:
                            n.send(btn.text)

        redrawWindow(win, game, p)


def menu_screen():
    run = True
    while run:
        win.fill(GRAY)
        font = pygame.font.SysFont("comicsans", 65, bold=True)
        text = font.render("Click to Play!", True, YELLOW)
        win.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    main()


while True:
    menu_screen()
