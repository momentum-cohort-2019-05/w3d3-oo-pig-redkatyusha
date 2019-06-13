import random

class Game:
    """
    Plays the dice game Pig with two players.
    """

    def __init__(self):
        self.scoreboard = Scoreboard()
        player1 = input("What is your name, Player 1? ")
        player2 = input("What is your name, Player 2? ")
        self.players = Player(player1, player2)

class Scoreboard:
    """
    Keep track of the turn score and total score.
    """

    def __init__(self):
        pass

class Player:
    """
    Represents the players in the game.
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Die:
    """
    Represents a die with six sides.
    """

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides + 1)