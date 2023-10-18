from os import path
from typing import Dict

from sphinx.application import Sphinx

__version__ = "0.0.0"


def setup(app: Sphinx) -> Dict[str, bool]:
    app.add_html_theme("rapidsai_sphinx_theme", path.abspath(path.dirname(__file__)))
    app.add_js_file("rapidsai.js", loading_method="defer")

    # Override PyData theme defaults here
    app.config["html_theme_options"].update(
        {
            "navbar_align": "left",
            "show_toc_level": 2,
            "header_links_before_dropdown": 2,
            "navbar_start": ["navbar-logo", "version-switcher"],
            "external_links": [
                {"name": "Ecosystem", "url": "https://rapids.ai/ecosystem"},
                {"name": "Learn More", "url": "https://rapids.ai/learn-more"},
                {"name": "News", "url": "https://rapids.ai/news"},
                {"name": "User Guides", "url": "https://rapids.ai/user-guides"},
                {"name": "API Docs", "url": "https://rapids.ai/api-docs"},
                {"name": "Install", "url": "https://rapids.ai/install"},
            ],
        }
    )
    return {"parallel_read_safe": True, "parallel_write_safe": True}
