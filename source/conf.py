# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Avata'
copyright = '2023, minghui'
author = 'minghui'
version = 'v2.0'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['chinese_search', 'sphinx.ext.mathjax', 'sphinx_sitemap', 'sphinx_multiversion']
extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
# language = 'zh_TW'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# html_theme = 'SphinxDoc'
# html_theme = 'alabaster'
# html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
templates_path = ['_templates']
# html_static_path = ['_static']
html_sidebars = {
    '**': ['versions.html']
}
smv_latest_version = 'master'
