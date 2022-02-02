import pytest

from game.combination import Combination
from game.combination_comparison import CombinationComparison
from game.guess import Guess


class TestCombination:
    def test_str(self):
        combination = Combination(
            values="1234"
        )
        expected_result = "1234"
        assert str(combination) == expected_result

    def test_import_str_case_numeric(self):
        combination = Combination(
            values="1234"
        )
        expected_values = [1, 2, 3, 4]
        assert combination.values == expected_values

    def test_import_str_case_list(self):
        combination = Combination(
            values="[1, 2, 3, 4]"
        )
        expected_values = [1, 2, 3, 4]
        assert combination.values == expected_values

    def test_import_list_str(self):
        combination = Combination(
            values=["1", "2", "3", "4"]
        )
        expected_values = [1, 2, 3, 4]
        assert combination.values == expected_values

    def test_import_list_int(self):
        combination = Combination(
            values=[1, 2, 3, 4]
        )
        expected_values = [1, 2, 3, 4]
        assert combination.values == expected_values

    def test_clean(self):
        combination = Combination(
            values=[1, "2", "3", "4"]
        )
        expected_values = [1, 2, 3, 4]
        assert combination.values == expected_values

    @pytest.mark.parametrize(
        "values",
        [
            "123",
            [10, 1, 1, 1],
        ]
    )
    def test_validator(self, values):
        with pytest.raises(Exception):
            Combination(
                values=values,
            )

    @pytest.mark.parametrize(
        "values",
        [
            "[1, 2, 3, 4]",
            "1234",
            "1,2,3,4",
            "1[234",
            "12]34",
            "12     34",
        ]
    )
    def test_clean_list_pattern_input(self, values):
        expected_result = "1234"
        assert Combination.clean_list_pattern_input(values) == expected_result

    def test_clean_input_case_numeric(self):
        values = "1234"
        expected_result = ["1", "2", "3", "4"]
        assert Combination.clean_input(values) == expected_result

    def test_clean_input_case_list(self):
        values = "[1, 2, 3, 4]"
        expected_result = ["1", "2", "3", "4"]
        assert Combination.clean_input(values) == expected_result

    @pytest.mark.parametrize(
        "values",
        [
            "1, 2, 3, 4",
            "['1', '2', '3', '4']",
        ]
    )
    def test_clean_input_case_exception(self, values):
        with pytest.raises(Exception):
            Combination.clean_input(values)

    def test_equality_case_uncomparable(self):
        combination = Combination(
            values="1234",
        )
        with pytest.raises(Exception):
            combination.__eq__("1234")

    def test_equality_case_distinct(self):
        combination_1 = Combination(
            values="1234",
        )
        combination_2 = Combination(
            values="1235",
        )
        assert not combination_1 == combination_2

    def test_equality_case_success(self):
        combination_1 = Combination(
            values="1234",
        )
        combination_2 = Combination(
            values="1234",
        )
        assert combination_1 == combination_2

    @pytest.mark.parametrize(
        "values_1,values_2,correct_guess,misplaced_guess",
        [
            ("1234", "1234", 4, 0),
            ("1234", "4321", 0, 4),
            ("1234", "5677", 0, 0),
            ("1234", "1545", 1, 1),
            ("1111", "1111", 4, 0),
            ("1111", "1221", 2, 0),
            ("1122", "1331", 1, 1),
            ("1122", "3311", 0, 2),
        ]
    )
    def test_combination_comparison(
            self,
            values_1,
            values_2,
            correct_guess,
            misplaced_guess
    ):
        combination_1 = Combination(
            values=values_1,
        )
        combination_2 = Combination(
            values=values_2,
        )
        expected_combination_comparison = CombinationComparison(
            accurate_guess=correct_guess,
            misplaced_guess=misplaced_guess
        )
        assert expected_combination_comparison == combination_1.compare_with_combination(combination_2)

    def test_is_guess_coherent_case_false(self):
        combination = Combination(
            values="1111",
        )
        guess = Guess(
            combination=Combination(
                values="2222",
            ),
            combination_comparison=CombinationComparison(
                accurate_guess=4,
                misplaced_guess=0
            )
        )
        assert not combination.is_guess_coherent(guess)

    def test_is_guess_coherent_case_true(self):
        combination = Combination(
            values="1111",
        )
        guess = Guess(
            combination=Combination(
                values="1111",
            ),
            combination_comparison=CombinationComparison(
                accurate_guess=4,
                misplaced_guess=0
            )
        )
        assert combination.is_guess_coherent(guess)
