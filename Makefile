install:
	@poetry install

tests:
    poetry run pytest tests/test_gendiff.py

lint:
	poetry run flake8 gendiff

