# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyCon JP TV #25 sample project'
copyright = '2023, takanory'
author = 'takanory'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'bizstyle'
html_theme = "furo"
html_static_path = ['_static']
html_logo = "_static/logo.png"

# sphinxext-opengraph
ogp_site_url = "https://pyconjptv25-sphinx-sample.readthedocs.io/"
ogp_image = "https://pyconjptv25-sphinx-sample.readthedocs.io/en/latest/_static/logo.png"
