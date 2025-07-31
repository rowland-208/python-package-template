The packagename package is a template library that does nothing.

Be sure to start your README with a simple code example:

```
import packagename

packagename.example.print_data()
```

Next link to example notebooks and include images in your README.

Check out the [examples.ipynb](https://github.com/rowland-208/python-package-template/blob/main/etc/examples.ipynb) jupyter notebook for usage examples.

![Sample image](https://github.com/rowland-208/python-package-template/blob/main/etc/samples.png?raw=True)

Package structure:
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
