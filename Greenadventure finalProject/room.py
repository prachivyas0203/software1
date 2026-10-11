# This class represents a place in the game.

class Room:
    def __init__(self, name, problem, solution):
        self.name = name
        self.problem = problem
        self.solution = solution

    def show_details(self):
        return self.name + ": " + self.problem

    def solve_problem(self):
        return self.solution