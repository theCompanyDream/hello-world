import click

@click.command()
@click.argument('name', nargs=-1, type=click.Path())
def cli(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f'Hello %s!' % ' '.join(name))