import builtins
from unittest.mock import MagicMock, Mock

from game.combination import Combination
from game.combination_comparison import CombinationComparison
from game.guess import Guess
from game.step import Step


class TestStep:
    test_file = "file/test.txt"

    def test_display_potential_solution(self):
        builtins.input = MagicMock(return_value="1")
        builtins.print = MagicMock()
        step = Step(file=TestStep.test_file)
        step.display_potential_solution()
        builtins.print.assert_called_with(str(step.solution))

    def test_choose_random_solution(self):
        expected_combination = Combination("1234")
        builtins.input = MagicMock(return_value="1")
        step = Step(file=TestStep.test_file)
        result = step.choose_random_solution()
        assert result == expected_combination

    def test_gather_inputs(self):
        builtins.input = Mock(side_effect=[1, 0, 1, 0])
        step = Step(file=TestStep.test_file)
        expected_result = (1, 0)
        assert expected_result == step.gather_inputs()

    def test_step(self):
        builtins.input = Mock(side_effect=[1, 0])
        step = Step(file=TestStep.test_file)
        expected_guess = Guess(
            combination=Combination("1234"),
            combination_comparison=CombinationComparison(
                accurate_guess=1,
                misplaced_guess=0,
            )
        )
        assert expected_guess == step.guess
