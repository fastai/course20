.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard *.ipynb)

all: docs
	git commit -am update && git push

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

release: pypi
	fastrelease_conda_package --upload_user fastai --build_args '-c pytorch -c fastai'
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

