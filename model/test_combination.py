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
