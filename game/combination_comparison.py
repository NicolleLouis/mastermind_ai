class CombinationComparison:
    def __init__(
            self,
            accurate_guess,
            misplaced_guess,
    ):
        self.accurate_guess = accurate_guess
        self.misplaced_guess = misplaced_guess
        self.validator()

    def __str__(self):
        return f"""
        Accurate guesses: {self.accurate_guess}
        Misplaced guesses: {self.misplaced_guess}
        """

    def __eq__(self, other):
        if type(other) != CombinationComparison:
            raise Exception(f"Can only compare with CombinationComparison not {type(other)}")
        if self.accurate_guess != other.accurate_guess:
            return False
        if self.misplaced_guess != other.misplaced_guess:
            return False
        return True

    def validator(self):
        from .combination import Combination

        if type(self.misplaced_guess) is not int:
            raise Exception(f"Misplaced guess should be int not {type(self.misplaced_guess)}")
        if type(self.accurate_guess) is not int:
            raise Exception(f"Accurate guess should be int not {type(self.accurate_guess)}")
        if self.misplaced_guess < 0:
            raise Exception(f"Misplaced guess can't be negative: {self.misplaced_guess}")
        if self.accurate_guess < 0:
            raise Exception(f"Accurate guess can't be negative: {self.accurate_guess}")
        if self.misplaced_guess + self.accurate_guess > Combination.combination_length:
            raise Exception(f"Can't be more guesses than combination")
