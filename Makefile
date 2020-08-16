SRC = $(wildcard nbs/*.ipynb)

release: pypi
	nbdev_conda_package --upload_user fastai --build_args '-c pytorch -c fastai'
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

