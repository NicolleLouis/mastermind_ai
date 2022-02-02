from unittest.mock import MagicMock

from .combinations_generator import CombinationGenerator


class TestCombinationGenerator():
    def test_add_one_possibility_first_step(self):
        values = [[0]]
        expected_result = [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 5],
            [0, 6],
            [0, 7],
        ]
        result = CombinationGenerator.add_one_possibility(values)
        assert result == expected_result

    def test_add_one_possibility_second_step(self):
        values = [[0, 0]]
        expected_result = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 2],
            [0, 0, 3],
            [0, 0, 4],
            [0, 0, 5],
            [0, 0, 6],
            [0, 0, 7],
        ]
        result = CombinationGenerator.add_one_possibility(values)
        assert result == expected_result

    def test_generate_all_possibilities(self):
        CombinationGenerator.add_one_possibility = MagicMock()
        CombinationGenerator.generate_all_possibilities()
        assert CombinationGenerator.add_one_possibility.call_count == 3
