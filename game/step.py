import random

from file_service.file_service import FileService
from game.combination import Combination
from game.combination_comparison import CombinationComparison
from game.guess import Guess


class Step:
    def __init__(
            self,
            file: str,
            solution: Combination = None,
            verbose: bool = False,
    ):
        self.is_victory = False
        self.number_of_potential_solution_after_step = None
        self.number_of_potential_solution_before_step = None

        self.file = file
        self.solution = solution
        self.verbose = verbose

        self.answer = self.choose_random_answer()
        if self.verbose:
            self.display_potential_solution()
        self.result = self.compute_results()
        self.guess = Guess(
            combination=self.answer,
            combination_comparison=self.result
        )
        self.update_file()
        self.update_victory()
        if self.verbose:
            self.display_conclusion()

    def display_potential_solution(self):
        print(str(self.answer))

    def compute_results(self):
        if self.solution is not None:
            return self.solution.compare_with_combination(self.answer)
        else:
            return self.gather_inputs()

    @staticmethod
    def gather_inputs():
        accurate_guess = int(input("Number of accurately placed guess: "))
        misplaced_guess = int(input("Number of misplaced guess number: "))
        return CombinationComparison(
            accurate_guess=accurate_guess,
            misplaced_guess=misplaced_guess,
        )

    def choose_random_answer(self):
        potential_solutions = FileService.read_lines(self.file)
        self.number_of_potential_solution_before_step = len(potential_solutions)
        answer = random.choice(potential_solutions)
        return Combination(
            values=answer
        )

    def update_file(self):
        valid_solution_with_new_guess = []
        potential_solutions = FileService.read_lines(self.file)
        for potential_solution in potential_solutions:
            potential_solution = Combination(potential_solution)
            if potential_solution.is_guess_coherent(self.guess):
                valid_solution_with_new_guess.append(str(potential_solution))
        FileService.write_list_to_file(file=self.file, items=valid_solution_with_new_guess)
        self.number_of_potential_solution_after_step = len(valid_solution_with_new_guess)

    def display_conclusion(self):
        print("#####")
        print(f"Solution proposed was: {str(self.answer)}")
        print(
            f"Went from: {self.number_of_potential_solution_before_step} to"
            f" {self.number_of_potential_solution_after_step} possibilities"
        )
        print("#####")

    def update_victory(self):
        victorious_combination = CombinationComparison(
            accurate_guess=4,
            misplaced_guess=0,
        )
        if self.guess.combination_comparison == victorious_combination:
            self.is_victory = True
