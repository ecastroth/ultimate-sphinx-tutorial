# The ultimate Sphinx tutorial

[![Documentation Status](https://readthedocs.org/projects/the-ultimate-sphinx-tutorial/badge/?version=latest)](https://the-ultimate-sphinx-tutorial.readthedocs.io/en/latest/?badge=latest)

This repository contains the necessary information to generate [PEP257](https://peps.python.org/pep-0257/) and [NumpyDocs](https://numpydoc.readthedocs.io/en/latest/index.html) compliant automathic documentation of projects with nested packages using Sphinx. It's thinked to serve as a demo for a real repository.

## Tutorials

This guide contains the following sections.

### A primer on docstrings
- What is a docstring.
- How to write correctly formatted docstrings.
- What is reStructuredText.
- How to write some simple reStructuredText files.

### A practic guide on how to add Sphinx to your project
- How initialize Sphinx in your project.
- How to build documentation.
- Detail explanations to understand how the `conf.py` file works.
- Theme selection and customization.
- Activate built-in or third party extensions.
- Add support for markdown files.
- Detail explanations to understand how the `conf.py` file works.
- Translate docstrings in your code to reStructuredText files.
- Dealing with nested packages or modules.
- Take your documentation to the next level using extensions and templates.
- Detail explanations to understand how the `custom-templates.rst` files works.
- A primer on the Jinja template engine.
- Sphinx support for Jinja.


## Installation and use

To learn how to use Sphinx to generate your documentation, you must build and follow the guide from the `guide` directory. To do this clone the repo using:

```bash
git clone https://github.com/ecastroth/ultimate-sphinx-tutorial.git
```

Now you'll need to install the dependencies, if you use `conda` do:

```bash
conda env create -f requirements/conda-requirements.yaml
```

or if you use `pip`:

```bash
pip install -r requirements/pip-requirements.txt
```

Once the dependencies are installed, you can build the tutorial. For this, in the `guide` directory do:

```bash
make clean html
```

Then simply open the `guide/build/html/index.html` file and follow the steps.
