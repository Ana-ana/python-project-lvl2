install:
	@poetry install

lint:
	poetry run flake8 gendiff

tests:
    poetry run pytest tests/test_gendiff.py

