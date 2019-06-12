SCORE_TO_WIN = 100

class PlayGame:
    """
    Plays the game dice Pig with two players.
    """

    def __init__(self):
        self.player_one = Player()
        self.player_two = self.get_opponent
        self.scoreboard = Scoreboard(self.player_one, self.player_two)
        self.play_game()

    def get_opponent(self):
        number_of_players = None
        while True:
            number_of_players = input("Input number of players: ")
            try:
                if int(number_of_players) == 2:
                    return Player()
                elif int(number_of_players) == 1:
                    print("Coming soon!")
                else:
                    print("Not supported.")
            except:
                print("Invalid input. Try again.")

    def play_game(self):
        game_over = False
        first_players_turn = True
        while not game_over:
            self.scoreboard.display()
            if first_players_turn:
                print("Player 1")
                game_over = self.player_one.take_turn()
            else:
                print("Player 2")
                game_over = self.player_two.take_turn()
            first_players_turn = not first_players_turn

    def start_game(self):
        pass
    
class Scoreboard:
    """
    Tracks turn score, total score, and multi-game score.
    """

    def __init__(self, player_one, player_two, best_of=1):
        self.player_one = player_one
        self.player_two = player_two
        self.best_of = best_of

    def display(self):
        print(f"{self.player_one.name}: {self.player_one.score}")


class Player:
    """
    Makes a player class.
    """

    def __init__(self, turn=False):
        self.score = 0
        self.winner = False
        self.name = input("What's your name? ")

    def take_turn(self):
        self.score += int(input("Put in a score: "))
        if self.score >= SCORE_TO_WIN:
            print(f"{self.name} wins!")
            self.winner = True
        return self.winner

PlayGame()