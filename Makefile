# Can be overwrite with ENV var => `NAME=".custom_env" make install`
NAME=.env
SHELL:=/bin/bash

.PHONY: check install dev analysis clean

check:
	$(NAME)/bin/pip install -r test-requirements.txt; \
	$(NAME)/bin/py.test test \
	--cov=defacto --cov-report term-missing --cov-report xml \
	--junitxml=test-report.xml

install:
	python -m venv $(NAME)
	$(NAME)/bin/pip install --upgrade pip setuptools wheel
	$(NAME)/bin/pip install .

dev:
	python -m venv $(NAME)
	$(NAME)/bin/pip install --upgrade pip setuptools wheel
	$(NAME)/bin/pip install -e .
	$(NAME)/bin/pip install -r test-requirements.txt

upgrade:
	$(NAME)/bin/pip install --upgrade -r requirements.txt
	$(NAME)/bin/python setup.py install

analysis:
	$(NAME)/bin/pip install pylint; \
	$(NAME)/bin/pylint --rcfile=.pylintrc defacto \
	--output-format=parseable \
	-r y --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" \
	> .pylint.log || true

clean:
	if [ -d $(NAME) ]; \
		then \
		$(NAME)/bin/python setup.py clean; \
		fi
	rm -rf $(NAME)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "*~" -delete
	find . -name "*.swp" -delete
	rm -f coverage.xml
	rm -rf defacto.egg-info
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -f test-report.xml
	rm -f .pylint.log
