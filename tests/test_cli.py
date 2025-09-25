from click.testing import CliRunner
from hello import cli  # Replace with your actual module name

def test_cli_single_name():
    runner = CliRunner()
    result = runner.invoke(cli, ['world'])

    assert result.exit_code == 0
    assert 'Hello world!' in result.output

def test_cli_multiple_names():
    runner = CliRunner()
    result = runner.invoke(cli, ['john', 'jane', 'bob'])

    assert result.exit_code == 0
    assert 'Hello john jane bob!' in result.output

def test_cli_no_arguments():
    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 0
    assert 'Hello !' in result.output

def test_cli_with_paths():
    runner = CliRunner()
    result = runner.invoke(cli, ['/path/to/file', 'another/path'])

    assert result.exit_code == 0
    assert 'Hello /path/to/file another/path!' in result.output