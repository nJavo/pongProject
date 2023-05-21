class Elo:
    def __init__(self, player1_initial_rating=1000, player2_initial_rating=1000):
        self.player1_rating = player1_initial_rating
        self.player2_rating = player2_initial_rating

    def calculate_new_ratings(self, winner):
        K = 16  # K-factor, which controls how much an outcome will change the players' ratings

        # Calculate the expected outcomes
        player1_expected = 1 / (1 + 10 ** ((self.player2_rating - self.player1_rating) / 400))
        player2_expected = 1 - player1_expected

        if winner == 1:
            # If player 1 won, set player1_actual to 1 and player2_actual to 0
            player1_actual = 1
            player2_actual = 0
        else:
            # If player 2 won, set player1_actual to 0 and player2_actual to 1
            player1_actual = 0
            player2_actual = 1

        # Update the ratings
        self.player1_rating += K * (player1_actual - player1_expected)
        self.player2_rating += K * (player2_actual - player2_expected)

    def get_ratings(self):
        return self.player1_rating, self.player2_rating
