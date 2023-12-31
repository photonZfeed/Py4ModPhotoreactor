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
import os
import sys

# sys.path.insert(0, os.path.abspath('.'))
current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../../Py4ModPhotoreactor"))
# print(target_dir)
sys.path.insert(0, target_dir)
sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Py4ModPhotoreactor'
copyright = '2023, Daniel Kowalczyk, Dirk Ziegenbalg'
author = 'Daniel Kowalczyk, Dirk Ziegenbalg'
# The short X.Y version.
version = '2.0.0'
# The full version, including alpha/beta/rc tags.
release = version
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'sphinx.ext.intersphinx'
]

autodoc_mock_imports = ["tinkerforge", "simple_pid","zip_longest","serial"]

autodoc_default_options = {
    'imported-members': False,
}

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# Configuration of sphinx.ext.coverage
coverage_show_missing_items = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme_github_versions'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}