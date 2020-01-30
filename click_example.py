"""Example of using libraries Click and Rich to create CLI"""

import time
import click
from rich.console import Console
from rich.table import Column, Table
console = Console()


@click.group()
def cli():
    pass


def get_length(word: str) -> int:
    time.sleep(1)
    return len(word)


@cli.command()
@click.argument('words', nargs=-1)
def compute(words):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Word", style="dim", width=12)
    table.add_column("Length")
    with click.progressbar(words) as click_words:
        for word in click_words:
            word_length = get_length(word)
            table.add_row(word, str(word_length))
    console.print(table)
    

if __name__ == "__main__":
    cli()