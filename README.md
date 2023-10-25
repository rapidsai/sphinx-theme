# RAPIDS Sphinx Theme

> **Warning**
> Work In Progress & Experimental

Using default [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/) with customized configuration to standardized RAPIDS documentation navigation.

- RAPIDS nav section based on [announcements banner](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/announcements.html)
- Custom colors based on [css styling](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/styling.html)
- Doc versions based on [version switcher](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html)

## How to Use

Install the theme:

```sh
pip install git+https://github.com/rapidsai/sphinx-theme.git@main
```

Setup the `conf.py` file:

```py
html_theme = "rapidsai_sphinx_theme"
```

## How to Develop

1. Install the theme locally with:
   ```sh
   pip install -e .
   ```
2. Make any necessary changes to the `rapidsai_sphinx_theme` directory
3. Build the demo docs locally with:
   ```sh
   sphinx-build -b dirhtml docs _html
   ```
4. Start a development server to view the built docs with:
   ```sh
   python -m http.server -d _html
   ```
5. View the rendered docs @ <http://0.0.0.0:8000/>
