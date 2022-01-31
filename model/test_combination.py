import pytest

from .combination import Combination


class TestCombination:
    def test_str(self):
        combination = Combination(
            values="1234"
        )
        expected_result = "1234"
        assert str(combination) == expected_result

    def test_import_str(self):
        combination = Combination(
            values="1234"
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
