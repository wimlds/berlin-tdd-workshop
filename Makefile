.PHONY: setup
setup:
	poetry config virtualenvs.in-project true
	poetry update
	poetry install --no-interaction --no-ansi

.PHONY: test
test:
	poetry run pytest


.PHONY: pretty
pretty:
	poetry run flake8 aggregate.py
	poetry run flake8 .