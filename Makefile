SHELL := /bin/bash
# Gives the ability to change test verbosity ex: 'make test verbosity=2'
verbosity = 1

help:
	@echo "Usage:"
	@echo " make help       -- displays this help"
	@echo " make release    -- release to pypi"
	@echo " make test       -- runs tests"

release:
	python setup.py register sdist bdist_wheel upload

test:
	@make test-travis
	@flake8 .

test-travis:
	python -Wmodule -m coverage run tests/run.py -v$(verbosity)
	coverage report -m --fail-under 100
