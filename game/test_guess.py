import pytest

from .combination import Combination
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
