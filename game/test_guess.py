import pytest

from .combination import Combination
from .combination_comparison import CombinationComparison
from .guess import Guess


class TestGuess:
    def test_str_case_no_comparison(self):
        combination = Combination(
            values='1111'
        )
        guess = Guess(
            combination=combination
        )
        expected_result = """
        Guess: 1111
        Result: None
        """
        assert expected_result == str(guess)

    def test_str_case_comparison(self):
        combination_1 = Combination(
            values='1122'
        )
        combination_2 = Combination(
            values='1331'
        )
        combination_comparison = combination_1.compare_with_combination(combination_2)

        guess = Guess(
            combination=combination_1,
            combination_comparison=combination_comparison,
        )
        expected_result = f"""
        Guess: 1122
        Result: {str(combination_comparison)}
        """
        assert expected_result == str(guess)

    def test_validator_case_combination(self):
        with pytest.raises(Exception):
            Guess(
                combination=1
            )

    def test_validator_case_combination_comparison(self):
        with pytest.raises(Exception):
            Guess(
                combination=Combination(
                    values="1111"
                ),
                combination_comparison=1234
            )

    def test_equality_case_breaking(self):
        guess = Guess(
                combination=Combination(
                    values="1111"
                ),
                combination_comparison=CombinationComparison(
                    accurate_guess=0,
                    misplaced_guess=0,
                )
            )
        with pytest.raises(Exception):
            guess.__eq__(1234)

    def test_equality_case_false_combination(self):
        guess_1 = Guess(
                combination=Combination(
                    values="1111"
                ),
                combination_comparison=CombinationComparison(
                    accurate_guess=0,
                    misplaced_guess=0,
                )
            )
        guess_2 = Guess(
            combination=Combination(
                values="1121"
            ),
            combination_comparison=CombinationComparison(
                accurate_guess=0,
                misplaced_guess=0,
            )
        )
        assert not guess_1 == guess_2

    def test_equality_case_false_combination_comparison(self):
        guess_1 = Guess(
                combination=Combination(
                    values="1111"
                ),
                combination_comparison=CombinationComparison(
                    accurate_guess=0,
                    misplaced_guess=0,
                )
            )
        guess_2 = Guess(
            combination=Combination(
                values="1111"
            ),
            combination_comparison=CombinationComparison(
                accurate_guess=1,
                misplaced_guess=0,
            )
        )
        assert not guess_1 == guess_2

    def test_equality_case_true(self):
        guess_1 = Guess(
                combination=Combination(
                    values="1111"
                ),
                combination_comparison=CombinationComparison(
                    accurate_guess=0,
                    misplaced_guess=0,
                )
            )
        guess_2 = Guess(
            combination=Combination(
                values="1111"
            ),
            combination_comparison=CombinationComparison(
                accurate_guess=0,
                misplaced_guess=0,
            )
        )
        assert guess_1 == guess_2
