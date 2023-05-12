import os
from jinja2 import Template, Environment, FileSystemLoader


def get_parameters(template):
    params = template.get('Parameters')
    if not params:
        params = template.get('parameters')
    if not params:
        params = []
    return params


def get_resources(template):
    resources = template.get('Resources')
    if not resources:
        resources = template.get('resources')
    if not resources:
        resources = []
    return resources


def get_outputs(template):
    outputs = template.get('Outputs')
    if not outputs:
        outputs = template.get('outputs')
    if not outputs:
        outputs = []
    return outputs


def get_description(template):
    description = template.get("Description")
    if not description:
        description = template.get('description')
    if not description:
        description = "No Template description set"
    return description


TEMPLATE = """# {{ name }}
## Description
{{ description }}

### Parameters
The list of parameters for this template:
| Parameter        | Type   | Default   | Description |
|------------------|--------|-----------|-------------|
{% for parameter in parameters %}| {{ parameter }} | {{ parameters[parameter].Type }} | {% if parameters[parameter].Default %}{{ parameters[parameter].Default}}{% endif %} | {% if parameters[parameter].Description %} {{ parameters[parameter].Description}}{% endif %}
{%- endfor %}

### Resources
The list of resources this template creates:
| Resource         | Type   |
|------------------|--------|
{% for resource in resources %}| {{ resource }} | {{ resources[resource].Type }}
{% endfor %}

### Outputs
The list of outputs this template exposes:
| Output           | Description   |
|------------------|---------------|
{% for output in outputs %}| {{ output }} | {% if outputs[output].Description %}{{ outputs[output].Description}}{% endif %}
{% endfor %}
"""

CHILD_TEMPLATE = """{% extends baseTemplate %}
{%- block description -%}
## Description
{{ description }}
{%- endblock -%}

{%- block parameters -%}
### Parameters
The list of parameters for this template:
| Parameter        | Type   | Default   | Description |
|------------------|--------|-----------|-------------|
{% for parameter in parameters %}| {{ parameter }} | {{ parameters[parameter].Type }} | {% if parameters[parameter].Default %}{{ parameters[parameter].Default}}{% endif %} | {% if parameters[parameter].Description %} {{ parameters[parameter].Description}}{% endif %}
{%- endfor -%}
{%- endblock -%}

{%- block resources -%}
### Resources
The list of resources this template creates:
| Resource         | Type   |
|------------------|--------|
{% for resource in resources %}| {{ resource }} | {{ resources[resource].Type }}
{%- endfor -%}
{%- endblock -%}

{%- block outputs -%}
### Outputs
The list of outputs this template exposes:
| Output           | Description   |
|------------------|---------------|
{% for output in outputs %}| {{ output }} | {% if outputs[output].Description %}{{ outputs[output].Description}}{% endif %}
{%- endfor -%}
{%- endblock -%}
"""


def generate(template, name, baseTemplatePath):
    description = get_description(template)
    parameters = get_parameters(template)
    resources = get_resources(template)
    outputs = get_outputs(template)
    try:
        env = Environment(loader=FileSystemLoader(baseTemplatePath))
        baseTemplate=env.get_template('README.jinja')
        return Template(CHILD_TEMPLATE, trim_blocks=True, lstrip_blocks=True).render(
            baseTemplate=baseTemplate,
            name=name,
            description=description,
            parameters=parameters,
            resources=resources,
            outputs=outputs,
        )
    except:
        return Template(TEMPLATE).render(
            name=name,
            description=description,
            parameters=parameters,
            resources=resources,
            outputs=outputs,
        )
