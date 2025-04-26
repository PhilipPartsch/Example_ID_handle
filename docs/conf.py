# Configuration file for the Sphinx documentation builder.

import os
import sys
from sphinx_needs import __version__
print ('sphinx-needs version: ' + str(__version__))
from sphinx_needs.api import add_dynamic_function

sys.path.append(os.path.abspath('.'))
import metamodel

sys.path.append(os.path.abspath('scripts'))
from filter import filter_id_linked_element_and_back
from reports import stake_req_without_satisfied_by

from gitlink import get_edit_url_from_folder, extent_url_with_file, get_githoster_edit_url_for_need


# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'Example'
copyright = f'2025 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.0.1'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx_needs',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Sphinx-Preview

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case "div-mo-content" is the content area
    # and we handle all links there.
    #"selector": "div.md-content a",
    "selector": "div.body a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button",
    #"not_selector": "div.needs_head a, h1 a, h2 a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔎",
    #"icon": "icon:search",
    "width": 600,
    "height": 400,
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
#html_theme = 'sphinx_immaterial'

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- get edit url for git hoster
print('edit url to git hoster:')
import pathlib
current_folder = pathlib.Path().resolve()
git_hoster_edit_url = get_edit_url_from_folder(current_folder, with_docu_part = True, docu_part_default = 'docs')
print('git hoster edit url: ' + git_hoster_edit_url)

# -- Collections
# For debugging it is possible to disable the clean up after sphinx-build
# collections_final_clean = False

collections = {}

# Fetch coverage data from coverage.json.
# Info: we collect the coverage over all test, so only one file has to be read in.
import json
# relative from here: _static/_external_data/coverage.json
test_coverage_file = os.path.join(os.path.dirname(__file__), '_static', '_external_data', 'coverage.json')
if os.path.exists(test_coverage_file):
    f = open(test_coverage_file)
    json_data = json.load(f)
    f.close()
    files = json_data['files']
    test_coverage = []
    for key, value in files.items():
        test_coverage_per_file = {}
        coverage = value['summary']['percent_covered']
        test_coverage_per_file['name'] = key.replace('/', '_').replace('\\', '_').replace('.py', '')
        test_coverage_per_file['file'] = key
        test_coverage_per_file['coverage'] = coverage
        test_coverage_per_file['github_edit_url'] = extent_url_with_file(git_hoster_edit_url, str(os.path.join('templates', 'test_coverage.rst.template')))
        test_coverage.append(test_coverage_per_file)

    collections['test_coverage'] = {
                                    'driver': 'jinja',
                                    'source': os.path.join('templates', 'test_coverage.rst.template'),
                                    'target': os.path.join('test_coverage', 'test_coverage_for_{{name|lower}}.rst'),
                                    'data': test_coverage,
                                    'active': True,
                                    'multiple_files': True,
                                    }

# sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

print('plantuml path: ' + str(plantuml))

plantuml_output_format = 'svg'

# sphinx_needs configuration

needs_role_need_max_title_length = -1

needs_build_json = True

needs_id_regex = metamodel.needs_id_regex

needs_types = metamodel.needs_types

needs_extra_options = metamodel.needs_extra_options

needs_extra_links = metamodel.needs_extra_links

needs_services = metamodel.needs_services

needs_layouts = metamodel.needs_layouts

needs_global_options = metamodel.needs_global_options

needs_render_context = metamodel.needs_render_context

needs_warnings = metamodel.needs_warnings

needs_string_links = metamodel.needs_string_links

needs_default_layout = 'clean_with_edit_link'

def setup(app):
    app.add_config_value(name = 'gitlink_edit_url_to_git_hoster', default = git_hoster_edit_url, rebuild = '', types = [str])

    add_dynamic_function(app, get_githoster_edit_url_for_need)

    for func in metamodel.needs_functions:
        add_dynamic_function(app, func)

needs_id_prefixes = [
    {
    "postfix": "_A",
    "prefix":  "A_",
    "prefix_after_type": True,
    "paths": ["components/A/"],
    "links": "",
    },
]

def patch_id(id:str, need_type: str, config:dict):
    new_id: str = ""
    if config["prefix_after_type"]:
        new_id = config["prefix"] + id + config["postfix"]
    else:
        new_id = config["prefix"] + id + config["postfix"]
    return new_id


# patch id generation:
import aspectlib

@aspectlib.Aspect
def changeid(cutpoint, *args, **kwargs):
#def changeid(cutpoint,
#    app: Sphinx,
#    state: None | RSTState,
#    docname: None | str,
#    lineno: None | int,
#    need_type: str,
#    title: str,
#    *,
#    id: str | None = None,
#    **kwargs: Any,
#):
    print('before hook:')
    #print("Positional arguments:", args)
    #print("Keyword arguments:", kwargs)
    id = kwargs['id']
    print('id: ' + str(id))
    need_type = kwargs['need_type']
    print('need_type: ' + str(need_type))
    docname = args[1]
    print('docname: ' + str(docname))
    state = args[0]
    output_docname = state.document.settings.env.docname
    print('state docname: ' + str(output_docname))

    found: bool = False
    for config in needs_id_prefixes:
        for path in config["paths"]:
            if output_docname.startswith(path):
                found = True
                kwargs['id'] = patch_id(id, need_type, config)
            if found:
                break
        if found:
            break

    new_id = kwargs['id']
    print('new_id: ' + str(new_id))

    result = yield aspectlib.Proceed
    print('after hook:')
    yield aspectlib.Return(result)

import sphinx_needs.api

sphinx_needs.api.add_need = changeid(sphinx_needs.api.add_need)

# fix shinx-needs
from sphinx_needs.data import NeedsCoreFields
patched_options = [
    ('collapse', 'bool'), ('hide', 'bool'),
    ('template', 'str'), ('pre_template', 'str'), ('post_template', 'str'),
    ('type_color', 'str'), ('type_style', 'str'),
]

for po_name, po_type in patched_options:
    NeedsCoreFields[po_name]["allow_default"] = po_type

