import pytest

from game.combination_comparison import CombinationComparison


class TestCombinationComparison:
    def test_str(self):
        combination_comparison = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        expected_result = """
        Accurate guesses: 1
        Misplaced guesses: 1
        """
        assert expected_result == str(combination_comparison)

    def test_equality_breaking_case(self):
        combination_comparison = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        with pytest.raises(Exception):
            combination_comparison.__eq__(1)

    def test_equality_case_misplaced_guesses(self):
        combination_comparison_1 = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        combination_comparison_2 = CombinationComparison(
            misplaced_guess=2,
            accurate_guess=1,
        )
        assert not combination_comparison_2 == combination_comparison_1

    def test_equality_case_accurate_guesses(self):
        combination_comparison_1 = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        combination_comparison_2 = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=2,
        )
        assert not combination_comparison_2 == combination_comparison_1

    def test_equality(self):
        combination_comparison_1 = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        combination_comparison_2 = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        assert combination_comparison_2 == combination_comparison_1

    def test_init(self):
        combination_comparison = CombinationComparison(
            misplaced_guess=1,
            accurate_guess=1,
        )
        assert combination_comparison.misplaced_guess == 1
        assert combination_comparison.accurate_guess == 1

    @pytest.mark.parametrize(
        "accurate_guess,misplaced_guess",
        [
            ("a", 1),
            (1, "a"),
            (-1, 0),
            (1, -1),
            (1, 10),
        ]
    )
    def test_validator(self, accurate_guess, misplaced_guess):
        with pytest.raises(Exception):
            CombinationComparison(
                accurate_guess=accurate_guess,
                misplaced_guess=misplaced_guess,
            )
