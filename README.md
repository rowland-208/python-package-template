# Keep me
If you use this template the contents of the README.md file will be displayed on the PyPI page for your package
and on the github repository page.

Be sure to start your README with a simple code example:

```
import packagename

packagename.example.print_data()
```

Next link to example notebooks and include images in your README.

Check out the [examples.ipynb](https://github.com/rowland-208/python-package-template/blob/main/etc/examples.ipynb) jupyter notebook for usage examples.

![Sample image](https://github.com/rowland-208/python-package-template/blob/main/etc/samples.png?raw=True)

Finally provide explanations for questions you can anticipate from users of your package.

# Delete me

Once you make a copy of this template you can remove this section.

## Package structure
```
-- etc/
  -- contains code and data needed for readme, website, etc., not needed for the package
  -- contains helper scripts for building data that goes in the package, e.g., downloading images or data
-- src/packagename/
  -- contains the package code
  -- data/
    -- contains data files that are included in the package
-- tests/
  -- unit tests
.gitignore
LICENSE
pyproject.toml
README.md
setup.cfg
tox.ini
```

## Publishing to pypi

Instructions can be found in the [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

TL;DR

```
$ cd /path/to/your/package
$ python3 -m pip install --upgrade build
$ python3 -m build
$ python3 -m pip install --upgrade twine
$ python3 -m twine upload --repository testpypi dist/*
... supply your api token for testpypi ...
$ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
... test your package ...
$ python3 -m twine upload --repository pypi dist/*
... supply your api token for pypi ...
```

If you update frequently or have multiple contributors considering automating publishing with GitHub Actions or similar CI/CD tools as described in the [GitHub Actions guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

