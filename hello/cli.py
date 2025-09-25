import click
import os

@click.command()
@click.argument('names', nargs=-1, type=click.Path())
def cli(names):
    """Simple program that greets NAME for a total of COUNT times."""
    for name in names:
        if os.path.exists(name):
            with open(name, 'r') as file:
                content = file.read().strip()
                if content:
                    click.echo(content)
        else:
            click.echo(f'Hello {name}!')
