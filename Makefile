PYTHON       = $(shell which python)
SHELL_FILES  = $(shell find . -type f -name \*.sh)
PYTHON_FILES = $(shell find . -type f -name \*.py)


lint:
	shellcheck $(SHELL_FILES)
	flake8 --statistics $(PYTHON_FILES)
	pylint $(PYTHON_FILES)

requirements:
	python -m pip install -U -r requirements.txt

config:
	$(PYTHON) ./config.py

