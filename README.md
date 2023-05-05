# What is this?

Installing this tool will provide you with the command ```cfn-docs```.

The command ```cfn-docs``` accepts a list of AWS CloudFormation template paths and returns a description of each 
template in markdown:

```bash
cfn-docs org-bootstrap.template.yaml > org-bootstrap.template.README.md
```

In the example above we redirect the std out into a file.

## What does it read?
The tool will read the description from the template, each parameter, each resource and each output.  It will output
those descriptions in a markdown document under suitable headers.  It also lists parameters, resources and outputs 
that do not have any descriptions.


## Output to a README.md

Passing `--create-readme` to cfn-docs will cause it to write the output to a README.md alongside the CFN template

## README.jinja

A `README.jinja` can be added alongside the cfn template to act as a template for the README.md. If it exists, then cfn-docs will substitute blocks in this template with the relevant sections from the CFN template. The blocks available are:

```
{% block description %}{% endblock %}

{% block parameters %}{% endblock %}

{% block resources %}{% endblock %}

{% block outputs %}{% endblock %}
```

Additional documentation can be added to the README.jinja

## Pre-commit hook

You can use it in your pre-commit-config.yaml like this:

```yaml
  - repo: https://github.com/jamesmelville-gds/cloudformation-doc-generator
    rev: '0.5.7'
    hooks:
      - id: cfn-docs-docker
        files: ^(?!\..*).*/template\.(yml|yaml)$
        args: [--create-readme]
``` 
