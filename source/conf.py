# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'lmhsphinx'
# copyright = '2023, lmh'
# author = 'lmh'
# release = 'v2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

# templates_path = ['_templates']
# exclude_patterns = []

# language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

# ---------------------------自定义------------------------

project = 'lmhsphinx'
copyright = '2023, lmh'
author = 'lmh'
release = 'v2'

# ---------支持md---------https://www.osgeo.cn/sphinx/usage/markdown.html#id7
extensions = ['recommonmark']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
