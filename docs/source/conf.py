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
templates_path = ['_templates']

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
html_theme = 'sphinx_rtd_theme'
# html_logo = "/static/photo2.png"

# Настройка параметров оформления для темы Sphinx RTD
html_theme_options = {
    # Отображать только логотип, без заголовка
    'logo_only': True,
    # Показывать версию проекта
    'display_version': True,
    # Заголовок сайта (если не указан 'logo_only')
    'collapse_navigation': True,
    # Отображать навигацию во всплывающем окне при наведении
    'sticky_navigation': True,
    # Отключить автоматическое раскрытие пунктов навигации
    'navigation_depth': 4,
    # Отображать элементы навигации, которые обычно скрыты
    'includehidden': True,
    # Показывать только заголовки в навигации
    'titles_only': False,
    # Добавить favicon в HTML-документацию
    'favicon': 'path/to/favicon.ico',
    # Добавить пользовательскую CSS для темы


    # Добавить иконку GitHub в навигационной панели
    'github_user': 'username',
    'github_repo': 'project',
    'github_type': 'star',
    'github_banner': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_static_path = ['static']

html_css_files = [
    'custom.css',
]



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
