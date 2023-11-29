# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'The ultimate Sphinx tutorial'
copyright = '2023, Eduardo Castro'
author = 'Eduardo Castro'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',             # NumPy documentation
    'sphinx.ext.viewcode',  # Link to local code
    'myst_parser',          # For using Markdown inside reST
    'sphinx_design',        # To add buttons and cards
    'sphinx_copybutton',    # Add the "copy to clipboard" button on code cells
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Language 
language = "en"


# -- Extension config --------------------------------------------------------

# Numpydoc
numpydoc_show_class_members = True 
numpydoc_class_members_toctree = False
numpydoc_show_inherited_class_members = False

# Autodoc
autodoc_default_options = {
    # Autodoc members
    "members": True,
    # Autodoc undocumented memebers
    "undoc-members": False, 
    # Autodoc private memebers
    "private-members": True
    }
# No document TypeHints
autodoc_typehints = "none"

# Autosummary
autosummary_generate = True
autosummary_generate_overwrite = True

# MyST
myst_heading_anchors = 4


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'pydata_sphinx_theme' 

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Theme configuration -----------------------------------------------------

# Sidebar configuration
html_sidebars = {
    "**": ["search-field.html", "sidebar-nav-bs.html"]
    }

# General theme options
html_theme_options = {
    # Logo
    'logo': {'text': project},
    # Upper bar icons
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    # Icon links
    "icon_links": [
        # GitHub of the proyect
        {"name": "GitHub",
         "url": "https://github.com/ecastroth/sphinx-documentation-demo",
         "icon": "fa-brands fa-square-github",
         "type": "fontawesome",}
    ]
}