import random
from typing import Optional

from file_service.file_service import FileService
from game.combination import Combination
from game.step import Step
from generate_combinations.combinations_generator import CombinationGenerator


class Game:
    game_file = "file/game_file.txt"
    reference_file = CombinationGenerator.all_possibilities_file

    def __init__(self, manual=True):
        self.manual = manual
        self.solution = None if self.manual else self.choose_random_solution()

        self.steps = []
        self.current_step: Optional[Step] = None

        self.reset_file()
        self.run()
        self.display_victory()

    @classmethod
    def reset_file(cls):
        all_possibilities = FileService.read_lines(cls.reference_file)
        FileService.write_list_to_file(cls.game_file, all_possibilities)

    def should_stop(self):
        if FileService.number_of_line_in_file(self.game_file) == 0:
            raise Exception("There was an incoherence in your input")
        if self.current_step is not None:
            if self.current_step.is_victory:
                return True
        return False

    def step(self):
        step = Step(
            self.game_file,
            verbose=self.manual,
            solution=self.solution
        )
        self.steps.append(step)
        self.current_step = step

    def run(self):
        while not self.should_stop():
            self.step()

    def compute_possibilities_history(self):
        possibilities = [FileService.number_of_line_in_file(self.reference_file)]
        possibilities.extend(
            list(
                map(
                    lambda step: step.number_of_potential_solution_after_step,
                    self.steps
                )
            )
        )
        return possibilities

    @property
    def tries_history(self):
        return list(
            map(
                lambda step: str(step.guess.combination),
                self.steps
            )
        )

    def choose_random_solution(self):
        potential_solutions = FileService.read_lines(self.game_file)
        answer = random.choice(potential_solutions)
        return Combination(
            values=answer
        )

    def display_victory(self):
        print("#####")
        print("Victory!")
        print(f"Guess made in {len(self.steps)} tries")
        print(f"Successive possibilities {self.compute_possibilities_history()}")
        print(f"Successive tries {self.tries_history}")
        print("#####")
