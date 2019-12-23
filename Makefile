install:
	pre-commit install
	pip install -r requirements.txt

build:
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*

clean:
	rm -rf build dist
