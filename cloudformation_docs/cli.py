import click
import json
import os
from cfn_flip import to_json


from . import core


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("--create-readme", is_flag=True, show_default=True, default=False, help="Write a README.md alongside the template")
@click.argument("files", nargs=-1, type=click.File())

def generate(create_readme, files):
    for f in files:
        extension = f.name.split(".").pop()
        if extension in ["yaml", "yml"]:
            j = to_json(f)
        elif extension in ["json"]:
            j = f
        else:
            raise Exception("{}: not a valid file extension".format(extension))
        template = json.loads(j)
        result = core.generate(template, ".".join(f.name.split(".")[0:-1]))
        if create_readme:
            with open(os.path.dirname(f.name)+"README.md", 'w') as readme:
                readme.write(result)
        click.echo(result)


if __name__ == "__main__":
    generate()
