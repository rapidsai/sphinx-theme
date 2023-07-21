# RAPIDS Documentation Sphinx PyData Theme Assets
> **Warning**
> Work In Progress & Experimental 

Using default [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/) with customized configuration to standardized RAPIDS documentation navigation. 

- RAPIDS nav section based on [announcements banner](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/announcements.html)
- Custom colors based on [css styling](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/styling.html)
- Doc versions based on [version switcher](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html)


## How to Use
Append the code in the 'conf.py' file into your projects Sphinx config file. Verify that you have up to date 'project' and 'version' variables and no other configurations that would override the options. 


## Navigation Standardization 
To keep RAPIDS doc site navigation consistent, use the following top level nav directorys for every project:
- **Overview** (pages index, ideally with project introduction copy)
- **User Guides** (install, 10min, best practice guides, blog post links etc)
- **API Docs** (generated docs)
- **Deverloper Guide** (project specific development guides)

Note: There may be some project specific top level navigation necessary, but strive to keep it consistent across RAPIDS. 
