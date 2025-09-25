from click.testing import CliRunner
from hello import cli  # Replace with your actual module name

def test_cli_single_name():
    runner = CliRunner()
    result = runner.invoke(cli, ['Paul'])

    assert result.exit_code == 0
    assert 'Hello Paul!' in result.output

def test_cli_multiple_names():
    runner = CliRunner()
    result = runner.invoke(cli, ['john', 'jane', 'bob'])

    assert result.exit_code == 0
    assert 'Hello john!\nHello jane!\nHello bob!' in result.output

def test_cli_no_arguments():
    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 0
    assert 'No Arguments Provided' in result.output

def test_cli_with_paths(mocker):
    runner = CliRunner()
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('builtins.open', mocker.mock_open(read_data='mermzilla'))
    result = runner.invoke(cli, ['/path/to/file', 'another/path'])

    assert result.exit_code == 0
    assert 'mermzilla\nmermzilla' in result.output

def test_cli_with_existing_files(mocker):
    runner = CliRunner()

    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)

    # Mock file reading
    mock_file = mocker.mock_open(read_data='mermzilla')
    mocker.patch('builtins.open', mock_file)

    result = runner.invoke(cli, ['/path/to/file', 'another/path'])

    assert result.exit_code == 0
    assert 'mermzilla' in result.output

    # Verify open was called twice (once for each file)
    assert mock_file.call_count == 2

def test_cli_with_non_existing_files(mocker):
    runner = CliRunner()

    # Mock os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)

    result = runner.invoke(cli, ['john', 'jane'])

    assert result.exit_code == 0
    assert 'Hello john!' in result.output
    assert 'Hello jane!' in result.output

def test_cli_mixed_files_and_names(mocker):
    runner = CliRunner()

    # Mock exists to return True for first arg, False for second
    mocker.patch('os.path.exists', side_effect=[True, False])

    # Mock file reading for the "existing" file
    mock_file = mocker.mock_open(read_data='file content')
    mocker.patch('builtins.open', mock_file)

    result = runner.invoke(cli, ['/existing/file', 'regular_name'])

    assert result.exit_code == 0
    assert 'file content' in result.output
    assert 'Hello regular_name!' in result.output

def test_cli_different_file_contents(mocker):
    runner = CliRunner()

    mocker.patch('os.path.exists', return_value=True)

    # Mock different content for each file
    mock_file = mocker.mock_open()
    mock_file.side_effect = [
        mocker.mock_open(read_data='content1').return_value,
        mocker.mock_open(read_data='content2').return_value
    ]
    mocker.patch('builtins.open', mock_file)

    result = runner.invoke(cli, ['file1.txt', 'file2.txt'])

    assert result.exit_code == 0
    assert 'content1' in result.output
    assert 'content2' in result.output