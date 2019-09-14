install:
	pre-commit install
	pip install -r requirements.txt

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*
