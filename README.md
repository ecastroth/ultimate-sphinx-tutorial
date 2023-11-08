# Sphinx documentation demo

This repository contains the necessary information to generate correct automathic documentation of projects with nested packages using Sphinx. It's thinked to serve as a demo for a real repository.

To learn how to use Sphinx to generate your documentation, you must build and follow the guide from the `guide` directory. To do this, you'll need to install the dependencies, if you use `conda` do:

```bash
conda env create -f requirements/conda-requirements.yaml
```

or if you use `pip`:

```bash
pip install -r requirements/pip-requirements.txt
```

Once the dependencies are installed, you can build the tutorial. For this, in the `guide` directory use:

```bash
make html
```

Then simply open the `guide/build/html/index.html` file and follow the steps.
