import json

import pkg_resources
import rich_click as click
from rich import print
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards CLI"""


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Load a CSV file of employees into the database.

    - Validates data
    - Parses the file
    - Loads the data into the database
    """
    result = core.load(filepath)
    table = Table(title="Dundler Mifflin Associates")
    headers = ["name", "department", "role", "created", "email"]
    for header in headers:
        table.add_column(header, style="blue")
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.option("--department", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Show the data in the database."""
    result = core.read(**query)
    if not result:
        print("No records found")
        return
    if output:
        with open(output, 'w') as output_file:
            output_file.write(json.dumps(result))

    table = Table(title="Dunder Mifflin Report")
    headers = [keys for keys in result[0].keys()]
    for header in headers:
        table.add_column(header, style="blue")
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--department", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Adds points to a person or department."""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--department", required=False)
@click.option("--email", required=False)
@click.pass_context
def remove(ctx, value, **query):
    """Remove points of a person or department."""
    core.add(-value, **query)
    ctx.invoke(show, **query)
