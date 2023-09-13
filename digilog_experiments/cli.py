import click
import csv
from fuzzywuzzy import fuzz

"""CLI interface for digilog_experiments project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

@click.group()
def cli():
    """digilog_experiments CLI."""
    pass

@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
def check(csv_path):
    """Check each row in a CSV for fuzzy matching between 'website' and 'country'."""
    with open(csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            website = row.get("website", "")
            country = row.get("country", "")
            score = fuzz.ratio(website, country)
            if score > 70:  # you can adjust this threshold as needed
                click.echo(f"Match found for {website} and {country} with score: {score}")
            else:
                click.echo(f"No match found for {website} and {country}.")

cli.add_command(check)

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m digilog_experiments` and `$ digilog_experiments `.
    """
    cli()

if __name__ == "__main__":
    main()
