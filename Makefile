.PHONY: test
test:

	py.test test/test_client.py
	py.test --pep8 code/client.py
	
