.PHONY: test
test:

	py.test test/test_*.py
	py.test --pep8 code/client.py
	py.test --pep8 code/finances.py
