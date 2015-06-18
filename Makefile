SHELL := /bin/bash
# Gives the ability to change test verbosity ex: 'make test verbosity=2'
verbosity = 1

help:
	@echo "Usage:"
	@echo " make help       -- displays this help"
	@echo " make test       -- runs tests"

test:
	python -Wmodule -m coverage run tests/run.py -v$(verbosity)
	coverage report -m --fail-under 100
	@flake8 .
