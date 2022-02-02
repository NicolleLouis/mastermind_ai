from .combination_comparison import CombinationComparison
from .guess import Guess


class Combination:
    combination_length = 4
    number_of_possibilities = 8

    def __init__(self, values):
        if type(values) is list:
            self.values = values
        elif type(values) is str:
            self.values = list(values)

        self.clean()
        self.validator()

    def __str__(self):
        return "".join(
            list(
                map(
                    lambda value: str(value),
                    self.values
                )
            )
        )

    def clean(self):
        self.values = list(
            map(
                lambda value: int(value),
                self.values
            )
        )

    def validator(self):
        if len(self.values) != self.combination_length:
            raise Exception(f"Combination has not the correct length: {len(self.values)}")
        for value in self.values:
            if value not in range(self.number_of_possibilities):
                raise Exception(f"Value not legal: {value}")

    def __eq__(self, other):
        if type(other) is not Combination:
            raise Exception(f"Can only compare Combination not {type(other)}")
        if len(self.values) != len(other.values):
            return False
        for index in range(self.combination_length):
            if self.values[index] != other.values[index]:
                return False
        return True

    def compare_with_combination(self, combination):
        accurate_guess = 0
        misplaced_guess = 0
        values_1 = self.values
        values_2 = combination.values
        non_correct_guesses_1 = []
        non_correct_guesses_2 = []
        for index in range(self.combination_length):
            if values_1[index] == values_2[index]:
                accurate_guess += 1
            else:
                non_correct_guesses_1.append(values_1[index])
                non_correct_guesses_2.append(values_2[index])

        for value in non_correct_guesses_1:
            if value in non_correct_guesses_2:
                misplaced_guess += 1
                non_correct_guesses_2.remove(value)

        return CombinationComparison(
            accurate_guess=accurate_guess,
            misplaced_guess=misplaced_guess
        )

    def is_guess_coherent(self, guess: Guess):
        real_combination_comparison = self.compare_with_combination(guess.combination)
        return real_combination_comparison == guess.combination_comparison
