# Copyright (c) 2019-2023, NVIDIA CORPORATION.
import pydata_sphinx_theme

# PyData Theme Options
# https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html
#
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ['https://raw.githubusercontent.com/rapidsai/sphinx-theme/main/_static/css/rapids-custom.css']

html_theme_options = {
    "logo": {"text": project},
    "external_links": [],
    "icon_links": [],
    "github_url": f"https://github.com/rapidsai/{project}",
    "twitter_url": "https://twitter.com/rapidsai",
    "show_toc_level": 1,
    "navbar_start": ["navbar-logo", "version-switcher"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher.html","navbar-icon-links.html"],
    "announcement": "https://raw.githubusercontent.com/rapidsai/sphinx-theme/main/_static/rapids-nav.html", 
    "switcher": { 
        "version_match": version,
        "json_url": f"https://raw.githubusercontent.com/rapidsai/sphinx-theme/main/_static/versions/{project}-doc-versions.json"
        }
}
