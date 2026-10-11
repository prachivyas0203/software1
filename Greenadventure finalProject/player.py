# This class stores information about the player.

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0

    def add_points(self, points):
        self.score += points
        return self.score

    def show_score(self):
        return self.score