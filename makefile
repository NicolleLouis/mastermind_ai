test:
	PYTHONPATH=. pytest

dataset:
	PYTHONPATH=. python generate_combinations/__main__.py

run:
	PYTHONPATH=. python game/__main_manual__.py

auto:
	PYTHONPATH=. python game/__main__.py