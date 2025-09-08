class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        p1 = self.moves[0].lower()[0]
        p2 = self.moves[1].lower()[0]

        winner = -1
        if p1 == "r" and p2 == "s":
            winner = 0
        elif p1 == "s" and p2 == "p":
            winner = 0
        elif p1 == "p" and p2 == "r":
            winner = 0
        elif p1 == "s" and p2 == "r":
            winner = 1
        elif p1 == "p" and p2 == "s":
            winner = 1
        elif p1 == "r" and p2 == "p":
            winner = 1
        else:
            winner = -1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
