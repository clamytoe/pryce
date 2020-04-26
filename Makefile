# Makefile for pryce

# Project name
PROJECT_NAME= pryce

# Macro or 'function' definition
BUNDLE_EXEC= bundle exec $(1)

# Assigning the macros
VENV= $(call BUNDLE_EXEC,conda)
PYTEST= $(call BUNDLE_EXEC,pytest)
COVERAGE= $(call BUNDLE_EXEC,pytest)
INSTALL= $(call BUNDLE_EXEC,pip)
MYPY= $(call BUNDLE_EXEC,mypy)

# Shared flags
CONDA_ENV_FLAGS= env create --file environment.yml

PYTEST_FLAGS= -v

COVERAGE_FLAGS= $(PYTEST_FLAGS)
COVERAGE_FLAGS+= p no:warning
COVERAGE_FLAGS+= --cov ./$(PROJECT_NAME)/app
COVERAGE_FLAGS+= --cov-report term-missing

TIMEOUT_FLAGS= --timeout=3 --timeout_method=thread

# Define the make commands
.PHONY: cov env hint test

# Define the rules
all: $(PYTEST) $(COVERAGE) $(MYPY)

# Define each of the commands and specifying their outputs
$(VENV):
	@echo Creating virtual environment
	@$(VENV) $(CONDA_ENV_FLAGS)

env: $(VENV)

$(PYTEST):
	@(PYTEST) PYTEST_FLAGS

test: $(PYTEST)

$(COVERAGE):
	@$(PYTEST) $(COVERAGE_FLAGS)

cov: $(COVERAGE)

$(MYPY):
	@$(MYPY)

hint: $(MYPY)

# Use debug rule to check that all of the variables were
# constructed properly.
debug:
	@echo 'Rule -> $@'
	@echo '    PROJECT_NAME: $(PROJECT_NAME)'
	@echo '          PYTEST: $(PYTEST)'
	@echo '         INSTALL: $(INSTALL)'
	@echo '            MYPY: $(MYPY)'
	@echo ' CONDA ENV FLAGS: $(CONDA_ENV_FLAGS)'
	@echo '   TIMEOUT_FLAGS: $(TIMEOUT_FLAGS)'
	@echo '            VENV: $(VENV)'
	@echo '          PYTEST: $(PYTEST)'
	@echo '        COVERAGE: $(COVERAGE)'
	@echo '            MYPY: $(MYPY)'

# Simple help menu showing what commands are available
# and what they do.
help:
	@echo 'Makefile for generating documents from Asciidoc source files              '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make help                           prints this message                '
	@echo '   make all                            generates all of the file formats  '
	@echo '   make clean                          remove the generated files         '
	@echo '   make debug                          prints all of the variables used   '
	@echo '   make html                           (re)generates an html file         '
	@echo '   make pdf                            (re)generates a pdf file           '
	@echo '   make epub                           (re)generates an epub file         '
	@echo '   make mobi                           (re)generates a mobi file          '
	@echo '   make -n                             prints the commands without        '
	@echo '                                       executing them                     '
	@echo '                                                                          '
	@echo 'Example:                                                                  '
	@echo '   make -n pdf                         woud display the command for       '
	@echo '                                       generating the pdf document        '
	@echo '                                                                          '

# Specify clean-up rules.
clean:
	@/bin/rm -f __pycache__ .mypy_cache .pytest_cache

