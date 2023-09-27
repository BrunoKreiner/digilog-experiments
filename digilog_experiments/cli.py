import click
import csv
import pandas as pd
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

@click.command()
@click.argument('csv_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('n', type=int)
@click.option('--seed', default=42, help='Random seed for reproducibility.')
@click.option('--include-luqa', default = True, type=click.BOOL, help='Include Luqa, Malta in the top n examples.')
@click.option('--shuffle', default = True, type=click.BOOL, help='Shuffle the data before taking the top n examples.')
def human_labeling_preprocess(csv_path, output_path, n, seed, include_luqa, shuffle):
    """Preprocess a CSV file for human annotation."""
    df = pd.read_csv(csv_path)

    # Filter out invalid urls:
    df = df[~df["status"].str.contains("invalid url|no website found|no wikipedia page found", case=False, na=False)]

    if shuffle:
        df = df.sample(frac=1, random_state=seed)

    # Ensure the "Luqa, Malta" row is included
    if include_luqa:
        luqa_row = df[(df["Municipality"] == "Luqa") & (df["Country"] == "Malta")]
    
    df = df[df["Website"].notna()]

    # Depending on whether Luqa is already in the shuffled set, we might append or just keep as-is
    if include_luqa:
        if not df.head(n).isin(luqa_row.to_dict(orient='list')).all(1).any():
            df = pd.concat([luqa_row, df]).reset_index(drop=True)

    # Take the top n examples
    df_top_n = df.head(n)
    print("shuffle", shuffle)
    print("include_luqa", include_luqa)
    # Add the "Label", "Comment", and an example "Confidence" column for human annotators
    df_top_n['Label'] = ''  # Empty string to start, to be filled in by annotators
    df_top_n['Comment'] = ''  # Space for annotators to add any notes or comments
    df_top_n['Confidence'] = ''  # A column where annotators can rate their confidence in their label (e.g., "High", "Medium", "Low")

    # Save the updated dataframe to a new CSV file
    df_top_n.to_csv(output_path, index=False)

@click.command()
@click.argument('csv_file', default='../data/HumanAnnotated.csv', type=click.Path(exists=True))
def label_data(csv_file):
    df = pd.read_csv(csv_file)

    while True:
        # Find the first unlabeled row
        unlabeled_rows = df[df['Label'].isna()]
        if unlabeled_rows.empty:
            click.echo("All rows have been labeled!")
            break

        row = unlabeled_rows.iloc[0]

        # Display the information
        click.echo(f"Website: {row['Website']}")
        click.echo(f"Municipality: {row['Municipality']}")
        click.echo(f"Country: {row['Country']}")
        click.echo("------------------------------")

        # Get annotations from the user
        label = click.prompt("Enter label (0 for incorrect, 1 for correct, 2 for website problem)", type=int)
        comment = click.prompt("Enter any comments", default="")
        confidence = click.prompt("Enter confidence level (0-100)", type=int)

        # Update the dataframe with the new annotations
        idx = row.name
        df.at[idx, 'Label'] = label
        df.at[idx, 'Comment'] = comment
        df.at[idx, 'Confidence'] = confidence

        # Save changes to the CSV
        df.to_csv(csv_file, index=False)

        # Ask if the annotator wants to continue
        if not click.confirm("Would you like to continue annotating?"):
            break

cli.add_command(check)
cli.add_command(human_labeling_preprocess)
cli.add_command(label_data)

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m digilog_experiments` and `$ digilog_experiments `.
    """
    cli()

if __name__ == "__main__":
    main()
