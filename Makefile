clean_build: remove_dist build

remove_dist:
	rm -rf ./dist

build:
	python3 -m build

release: clean_build release_to_pypi

test_release: clean_build release_to_testpypi

release_to_pypi:
	python3 -m twine upload --repository pypi dist/*

release_to_testpypi:
	python3 -m twine upload --repository testpypi dist/*
