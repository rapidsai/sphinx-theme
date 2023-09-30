# Copyright (c) 2019-2023, NVIDIA CORPORATION.
import pydata_sphinx_theme

# -- Project information -----------------------------------------------------
project = "cu---" # NOTE: change to project name
copyright = "2018-2023, NVIDIA Corporation"
author = "NVIDIA Corporation"

###
###

# PyData Theme Options RAPIDS style
# https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

html_theme = "pydata_sphinx_theme"
html_logo= "_static/RAPIDS-logo-sm.png"
html_static_path = ["_static"]
html_css_files = "https://raw.githubusercontent.com/rapidsai/sphinx-theme/main/_static/css/rapids-custom.css"

html_theme_options = {
    "logo": {
        "text": project,
        "link": "https://rapids.ai/"
            },
    "external_links": [
        {"name": "GitHub", "url": f"https://github.com/rapidsai/{project}"},
        {"name": "Ecosystem", "url": "https://rapids.ai/ecosystem"},
        {"name": "Learn More", "url": "https://rapids.ai/learn-more"},
        {"name": "News", "url": "https://rapids.ai/news"},
        {"name": "User Guides", "url": "https://rapids.ai/user-guides"},
        {"name": "API Docs", "url": "https://rapids.ai/api-docs"},
        {"name": "Install", "url": "https://rapids.ai/install"}
    ],
    "header_links_before_dropdown": 2, # NOTE: change based on number of top level directories
    "show_toc_level": 2,
    "navbar_align": "left",
    "navbar_start": ["navbar-logo", "version-switcher"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher.html","navbar-icon-links.html"],
    "switcher": { 
        "version_match": version,
        "json_url": f"https://raw.githubusercontent.com/rapidsai/sphinx-theme/main/_static/versions/{project}-doc-versions.json" # Remote Doc Files Location JSON
    }
}
