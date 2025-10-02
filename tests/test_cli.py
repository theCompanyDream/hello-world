from click.testing import CliRunner
from hello import cli  # Replace with your actual module name

def test_cli_single_name():
    runner = CliRunner()
    result = runner.invoke(cli, ['Paul'])

    assert result.exit_code == 0
    assert 'Hello Paul' in result.output

def test_cli_multiple_names():
    runner = CliRunner()
    result = runner.invoke(cli, ['john', 'jane', 'bob'])

    assert result.exit_code == 0
    assert 'Hello john jane bob' in result.output

def test_cli_no_arguments():
    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 0
    assert 'No Arguments Provided' in result.output

