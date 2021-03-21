PYTHON       = $(shell which python)
SHELL_FILES  = $(shell find . -type f -name \*.sh)
PYTHON_FILES = $(shell find . -type f -name \*.py)

lint:
	shellcheck $(SHELL_FILES)
	flake8 --statistics $(PYTHON_FILES)
	pylint $(PYTHON_FILES)

config:
	$(PYTHON) ./config.py

