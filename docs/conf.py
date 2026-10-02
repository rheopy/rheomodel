import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

project = "rheomodel"
author = "Marco Caggioni"
release = "0.1.0"

extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
myst_enable_extensions = ["dollarmath"]
templates_path = ["_templates"]
# The exported WASM explorers live under _static/interactive/.
# The shared Pyodide runtime ships .md files: keep sphinx from treating
# them as docs sources, while still copying everything as static assets.
exclude_patterns = ["_build", "_static/**/*.md"]
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"

autodoc_member_order = "bysource"

# Guide pages link like [TC](tc); the same name also exists as a Python
# module (rheomodel.models.tc). The guides are the intended target.
suppress_warnings = ["myst.xref_ambiguous"]
