class Combination:
    combination_length = 4
    number_of_possibilities = 8

    def __init__(self, values):
        if type(values) is list:
            self.values = values
        elif type(values) is str:
            self.values = list(values)

        self.clean()
        self.validator()

    def __str__(self):
        return "".join(
            list(
                map(
                    lambda value: str(value),
                    self.values
                )
            )
        )

    def clean(self):
        self.values = list(
            map(
                lambda value: int(value),
                self.values
            )
        )

    def validator(self):
        if len(self.values) != self.combination_length:
            raise Exception(f"Combination has not the correct length: {len(self.values)}")
        for value in self.values:
            if value not in range(self.number_of_possibilities):
                raise Exception(f"Value not legal: {value}")
