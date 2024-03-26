import rich_click as click
import pkg_resources
from dundie import core
from rich import print
from rich.table import Table
from rich.console import Console


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
    headers = ["name", "department", "role", "email"]
    for header in headers:
        table.add_column(header, style="blue")
    for person in result:
        table.add_row(
            *[field.strip() for field in person.split(",")]
        )

    console = Console()
    console.print(table)
