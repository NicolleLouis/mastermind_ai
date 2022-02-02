class Guess:
    def __init__(
            self,
            combination,
            combination_comparison=None,
    ):
        self.combination = combination
        self.combination_comparison = combination_comparison
        self.validator()

    def __str__(self):
        return f"""
        Guess: {self.combination}
        Result: {self.combination_comparison}
        """

    def validator(self):
        from .combination import Combination
        from .combination_comparison import CombinationComparison

        if type(self.combination) is not Combination:
            raise Exception(f"Combination hasn't got the correct type: {type(self.combination)}")
        if self.combination_comparison is not None:
            if type(self.combination_comparison) is not CombinationComparison:
                raise Exception(f"Combination hasn't got the correct type: {type(self.combination_comparison)}")

    def __eq__(self, other):
        if type(other) is not Guess:
            raise Exception(f"Can only compare with Guess not {type(other)}")
        return self.combination == other.combination and self.combination_comparison == other.combination_comparison