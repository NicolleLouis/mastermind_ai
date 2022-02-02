import builtins
from unittest.mock import MagicMock, Mock, call

from file_service.file_service import FileService
from game.combination import Combination
from game.combination_comparison import CombinationComparison
from game.guess import Guess
from game.step import Step


class TestStep:
    test_file = "file/test.txt"

    def test_display_potential_solution(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = MagicMock(return_value="1")
        builtins.print = MagicMock()
        step = Step(file=TestStep.test_file)
        step.display_potential_solution()
        builtins.print.assert_called_with(str(step.solution))

    def test_choose_random_solution(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        expected_combination = Combination("1234")
        builtins.input = MagicMock(side_effect=[4, 0])
        step = Step(file=TestStep.test_file)
        result = step.choose_random_solution()
        assert result == expected_combination
        assert step.number_of_potential_solution_before_step == 1

    def test_gather_inputs(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = Mock(side_effect=[1, 0, 1, 0])
        step = Step(file=TestStep.test_file)
        expected_result = (1, 0)
        assert expected_result == step.gather_inputs()

    def test_step_init(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
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

    def test_update_file_case_error(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = Mock(side_effect=[1, 0])
        step = Step(file=TestStep.test_file)
        expected_result = 0
        assert step.number_of_potential_solution_after_step == expected_result

    def test_update_file_case_success(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = Mock(side_effect=[4, 0])
        step = Step(file=TestStep.test_file)
        expected_result = 1
        assert step.number_of_potential_solution_after_step == expected_result

    def test_display_conclusion(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = Mock(side_effect=[4, 0])
        step = Step(file=TestStep.test_file)
        builtins.print = MagicMock()
        step.display_conclusion()
        expected_calls = [
            call('Solution proposed was: 1234'),
            call('Went from: 1 to 1 possibilities')
        ]
        builtins.print.assert_has_calls(expected_calls)

    def test_update_victory(self):
        FileService.write_list_to_file(TestStep.test_file, ["1234"])
        builtins.input = Mock(side_effect=[4, 0])
        step = Step(file=TestStep.test_file)
        assert step.is_victory
