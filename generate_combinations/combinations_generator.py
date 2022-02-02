from file_service.file_service import FileService
from game.combination import Combination


class CombinationGenerator:
    all_possibilities_file = "file/all_possibility_file.txt"

    @staticmethod
    def add_one_possibility(values):
        extended_values = []
        for value in values:
            for possibility in range(Combination.number_of_possibilities):
                extended_value = value.copy()
                extended_value.append(possibility)
                extended_values.append(extended_value)
        return extended_values

    @classmethod
    def generate_all_possibilities(cls):
        values = range(Combination.number_of_possibilities)
        values = list(
            map(
                lambda value: [value],
                values
            )
        )

        for _ in range(Combination.combination_length - 1):
            values = cls.add_one_possibility(values)

        values = list(
            map(
                lambda value: "".join(str(value)),
                values

            )
        )

        FileService.write_list_to_file(
            cls.all_possibilities_file,
            values
        )
