# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import datetime
import sys
sys.path.insert(0, os.path.abspath('../..'))
from sphinx.builders.html import StandaloneHTMLBuilder


# -- Project information -----------------------------------------------------

project = 'Kwork'
copyright = '{}'.format(datetime.datetime.now().year)
author = 'Kwork'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'guzzle.sphinx.theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.graphviz',
]

# Add any paths that contain templates here, relative to this directory.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]


# Настройка параметров оформления для темы
import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "Project Name",
}

import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {

    # Set the path to a special layout to include for the homepage
    "index_template": "special_index.html",

    # Set the name of the project to appear in the left sidebar.
    "project_nav_name": "Project Name",

    # Set your Disqus short name to enable comments
    "disqus_comments_shortname": "my_disqus_comments_short_name",

    # Set you GA account ID to enable tracking
    "google_analytics_account": "my_ga_account",

    # Path to a touch icon
    "touch_icon": "",

    # Specify a base_url used to generate sitemap.xml links. If not
    # specified, then no sitemap will be built.
    "base_url": "",

    # Allow a separate homepage from the master_doc
    "homepage": "index",

    # Allow the project link to be overriden to a custom URL.
    "projectlink": "http://myproject.url",

    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": -1,

    # If False, expand all TOC entries
    "globaltoc_collapse": False,

    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
}

# -- Extension configuration -------------------------------------------------

# autodoc_inherit_docstrings = False
# napoleon_google_docstring = True
# napoleon_include_init_with_doc = True
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_keyword = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_attr_annotations = False

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
    'member-order': 'bysource',
    'ignore-module-all': True,
}
autoclass_content = 'class'
autodoc_typehints = 'signature'
autodoc_typehints_format = 'short'
autodoc_mock_imports = ['objgraph', 'memory_profiler', 'gprof2dot', 'snakeviz']
