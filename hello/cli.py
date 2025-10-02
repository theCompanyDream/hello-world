import click

@click.command()
@click.argument('arguments', nargs=-1, type=click.Path())
def cli(arguments):
    """Simple program that greets NAME for a total of COUNT times."""

    if not arguments:
        click.echo('No Arguments Provided')
        return

    full_name = ""

    for name in arguments:
        full_name += f"{name} "

    click.echo(f'Hello {full_name}')
