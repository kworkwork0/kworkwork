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
    'sphinx_rtd_theme',
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
html_theme = "sphinx_book_theme"
# html_logo = "/static/photo2.png"

# Настройка параметров оформления для темы
html_theme_options = {
    "repository_url": "https://github.com/your/repo",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": True,
}

html_title = "Your Title"
html_logo = "path/to/logo.png"


html_theme_options = {
    "use_download_button": False,
    "use_fullscreen_button": False,
    "use_edit_page_button": False,
}

html_theme_options = {
    "extra_navbar": "<strong>Extra Navigation Bar</strong>",
}

html_theme_options = {
    "font_family": "Arial, sans-serif",
    "head_font_family": "Georgia, serif",
    "code_font_family": "Monaco, 'Courier New', monospace",
    "css_override": "body { font-size: 16px; }",  # Дополнительные пользовательские стили
}

html_theme_options = {
    "page_width": "90%",
}

html_theme_options = {
    "body_bg_color": "#FFFFFF",
    "text_color": "#000000",
}

html_theme_options = {
    "show_navbar": True,
    "navbar_links": {
        "Home": "index.html",
        "About": "about.html",
        "Contact": "contact.html",
    },
}

html_theme_options = {
    "social_icons": [
        ("GitHub", "https://github.com/youraccount"),
        ("Twitter", "https://twitter.com/youraccount"),
        ("LinkedIn", "https://www.linkedin.com/in/youraccount"),
    ],
}

html_theme_options = {
    "use_search_bar": True,
    "search_bar_position": "sidebar",  # Можно использовать "top" для верхней панели
}



    # Добавить иконку GitHub в навигационной панели
    'github_user': 'username',
    'github_repo': 'project',
    'github_type': 'star',
    'github_banner': True,
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
