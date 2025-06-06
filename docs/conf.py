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
    'sphinxcontrib.plantuml',
    'sphinxcontrib.test_reports',
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

# fix shinx-needs see https://github.com/useblocks/sphinx-needs/issues/1420
from sphinx_needs.data import NeedsCoreFields
patched_options = [
    ('collapse', 'bool'), ('hide', 'bool'),
    ('template', 'str'), ('pre_template', 'str'), ('post_template', 'str'),
    ('type_color', 'str'), ('type_style', 'str'),
]

for po_name, po_type in patched_options:
    NeedsCoreFields[po_name]["allow_default"] = po_type


# changes for needs_id_prefixes

# define configuration
# patching of links is been need for useblocks sphinx-test-reports
needs_id_prefixes = [
    {
    "postfix": "",
    "prefix":  "A_",
    "prefix_after_type": True,
    "paths": ["components/A/"],
    "links": ["satisfies", "links",],
    },
    {
    "postfix": "_B",
    "prefix":  "",
    "prefix_after_type": False,
    "paths": ["components/B/"],
    "links": ["satisfies", "links",],
    },
    {
    "postfix": "",
    "prefix":  "C_",
    "prefix_after_type": False,
    "paths": ["components/C/"],
    "links": ["satisfies", "links",],
    },
]

# validate that paths not overlap each other
for i in range(len(needs_id_prefixes)):
    for j in range(len(needs_id_prefixes)):
        if i != j:
            i_paths = needs_id_prefixes[i]["paths"]
            j_paths = needs_id_prefixes[i]["paths"]
            for k in range(len(i_paths)):
                for l in range(len(j_paths)):
                    if k != l:
                        overlap: bool = False
                        overlap = overlap or i_paths[k].startswith(j_paths[l])
                        overlap = overlap or j_paths[l].startswith(i_paths[k])
                        if overlap:
                            print("Warning: in needs_id_prefixes")
                            print("It is not allowed to have overlapping 'paths': " + i_paths[k] + " " + j_paths[l])

# patch NeedCheckContext

from sphinx_needs.filter_common import NeedCheckContext


NeedCheckContext.needs_id_prefixes = needs_id_prefixes

def this_prefix(self) -> bool:
    if self._origin_docname is None:
        raise ValueError("`this_doc` can not be used in this context")

    result: bool = False
    check_any_prefix_match_current_file: bool = False
    check_any_prefix_match_current_need: bool = False
    for needs_id_prefix in needs_id_prefixes:
        for path in needs_id_prefix['paths']:
            result = result or \
                (self._origin_docname.startswith(path) and self._need["docname"].startswith(path))
            check_any_prefix_match_current_file = check_any_prefix_match_current_file or \
                self._origin_docname.startswith(path)
            check_any_prefix_match_current_need = check_any_prefix_match_current_need or \
                self._need["docname"].startswith(path)

    if check_any_prefix_match_current_file:
        return result
    else:
        # The current file does not fit in any prefix area
        # -> Return True if need is even not part of any prefix area
        return not check_any_prefix_match_current_need

NeedCheckContext.this_prefix = this_prefix

#function to patch ids
def patch_id(id:str, config: dict):
    new_id: str = ""
    if config["prefix_after_type"]:
        patched: bool = False
        for type_prefix in config['type_prefixes']:
            if id.startswith(type_prefix):
                id_without_type_prefix = id[len(type_prefix):]
                new_id = type_prefix + config["prefix"] + id_without_type_prefix + config["postfix"]
                patched = True
                break

        if not patched:
            new_id = config["prefix"] + id + config["postfix"]
    else:
        new_id = config["prefix"] + id + config["postfix"]
    return new_id

import re

#function to patch links
def patch_links(link:str, config: dict) -> str:
    new_link: str = ''
    if len(link) > 0:
        #link_split = link.split(sep=',')
        link_split = re.split(r"[,;]", link)
        links_main_patched: list = []
        for i in range(len(link_split)):
            link_split[i] = link_split[i].strip()
            link_main_part = link_split[i].split(sep='.', maxsplit=1)
            link_main = link_main_part[0]
            link_main_patched = patch_id(link_main, config)
            if len(link_main_part) == 1:
                links_main_patched.append(link_main_patched)
            else:
                link_main_patched_merged = link_main_patched + '.'+ link_main_part[1]
                links_main_patched.append(link_main_patched_merged)

        result = ', '.join(links_main_patched)
        return result

    else:
        return link

# function to change needs, before we generate a need
from sphinx_needs.config import NeedsSphinxConfig
import aspectlib

@aspectlib.Aspect
def changeid(*args, **kwargs):
    print('before hook:')
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    id = kwargs['id']
    print('id: ' + str(id))
    need_type = kwargs['need_type']
    print('need_type: ' + str(need_type))
    app = args[0]
    print('app: ' + str(app))
    state = args[1]
    print('state: ' + str(state))
    docname = ''
    if len(args) >= 3:
        docname = args[2]
    elif 'docname' in kwargs:
        docname = kwargs['docname']
    else:
        docname = state.document.settings.env.docname
    print('docname: ' + str(docname))

    needs_config = NeedsSphinxConfig(app.config)
    needs_types = needs_config.types
    type_prefixes = [t['prefix'] for t in needs_types]

    found: bool = False
    for config in needs_id_prefixes:
        if 'type_prefixes' not in config:
            # add type_prefixes to config
            config['type_prefixes'] = type_prefixes

        for path in config["paths"]:
            if docname.startswith(path):
                found = True
                new_id = patch_id(id, config)
                print('patched id: ' + str(new_id))
                kwargs['id'] = new_id
                for link in config["links"]:
                    if link in kwargs and len(kwargs[link]) > 0:
                        linkcontent = kwargs[link]
                        patched_linkcontent = patch_links(linkcontent, config)
                        print('patched link: ' + str(link) + ' from: ' + str(linkcontent) +' to:' + str(patched_linkcontent))
                        kwargs[link] = patched_linkcontent
            if found:
                break
        if found:
            break

    result = yield aspectlib.Proceed(*args, **kwargs)
    print('after hook:')
    yield aspectlib.Return(result)

#import function ot be extended
import sphinx_needs.api

sphinx_needs.api.add_need = changeid(sphinx_needs.api.add_need)
