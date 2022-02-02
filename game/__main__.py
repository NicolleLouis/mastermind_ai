from game.step import Step
from generate_combinations.combinations_generator import CombinationGenerator

step = Step(file=CombinationGenerator.all_possibilities_file)
print(step.guess)
