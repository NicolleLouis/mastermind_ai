import random

from file_service.file_service import FileService
from game.combination import Combination
from game.combination_comparison import CombinationComparison
from game.guess import Guess


class Step:
    def __init__(self, file):
        self.file = file
        self.solution = self.choose_random_solution()
        self.display_potential_solution()
        self.accurate_guess, self.misplaced_guess = self.gather_inputs()
        self.guess = Guess(
            combination=self.solution,
            combination_comparison=CombinationComparison(
                accurate_guess=self.accurate_guess,
                misplaced_guess=self.misplaced_guess,
            )
        )

    def display_potential_solution(self):
        print(str(self.solution))

    @staticmethod
    def gather_inputs():
        accurate_guess = int(input("Number of accurately placed guess: "))
        misplaced_guess = int(input("Number of misplaced guess number: "))
        return accurate_guess, misplaced_guess

    def choose_random_solution(self):
        potential_solutions = FileService.read_lines(self.file)
        solution = random.choice(potential_solutions)
        return Combination(
            values=solution
        )
