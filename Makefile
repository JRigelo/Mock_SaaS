.PHONY: test
test:

	py.test test/test_*.py
	py.test --pep8 SaaSModel/client.py
	py.test --pep8 SaaSModel/finances.py
