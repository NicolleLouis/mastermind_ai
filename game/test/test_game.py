import builtins
from unittest.mock import Mock

import pytest

from file_service.file_service import FileService
from game.game_model import Game
from game.step import Step
from generate_combinations.combinations_generator import CombinationGenerator


class TestGame:
    def test_reset_file(self):
        Game.reset_file()
        expected_result = FileService.read_lines(CombinationGenerator.all_possibilities_file)
        assert FileService.read_lines(Game.game_file) == expected_result

    def test_should_stop(self):
        Game.run = Mock()

        game = Game()
        FileService.clean_file(Game.game_file)
        with pytest.raises(Exception):
            game.should_stop()

    def test_should_stop_case_no_current_step(self):
        Game.run = Mock()

        game = Game()
        assert not game.should_stop()
        assert game.current_step is None

    def test_should_stop_case_victory(self):
        builtins.input = Mock(side_effect=[4, 0])

        game = Game()
        step = Step(Game.game_file)
        game.current_step = step
        assert game.should_stop()

    def test_step(self):
        builtins.input = Mock(side_effect=[4, 0])
        Game.run = Mock()

        game = Game()
        game.step()
        assert len(game.steps) == 1
        assert type(game.current_step) is Step
