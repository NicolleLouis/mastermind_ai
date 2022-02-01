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
