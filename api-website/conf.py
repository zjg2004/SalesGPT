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

sys.path.insert(0, os.path.abspath(".."))  # Source path
# Load environment variables from .env file in the parent directory
#from dotenv import load_dotenv
#load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
# Load GTAG_API from the .env file
GTAG_API = os.environ.get("GTAG_API", "")


# -- Project information -----------------------------------------------------

project = "SalesGPT"
copyright = "2024, Filip-Michalsky"
author = "Filip-Michalsky"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              "sphinxcontrib.googleanalytics",
              #'sphinxcontrib.gtagjs'
]

googleanalytics_id = "GTM-NX3SZD79"
"""
def setup(app):
    
    app.add_javascript("https://www.googletagmanager.com/gtag/js?id=GTM-NX3SZD79")
    app.add_javascript("google_analytics_tracker.js")
"""
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "custom.css",  # add your custom CSS file here
]
