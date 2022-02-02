test:
	PYTHONPATH=. pytest

dataset:
	PYTHONPATH=. python generate_combinations/__main__.py