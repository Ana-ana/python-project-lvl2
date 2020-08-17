install:
	@poetry install

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest tests/test_gendiff.py
	poetry run coverage run -m pytest test_gendiff.py
	coverage json -o code_coverage_report.json



