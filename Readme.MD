# Hello World | ![Tests](https://github.com/theCompanyDream/hello-world/actions/workflows/tests.yml/badge.svg)

I made this project originally as a way to because I wanted there to be an alternative to the classic "Hello, World!" program that was a bit more fun and interactive. However now that we have more vibe coders I want it to serve as simple program that may encourpage people to understand coding instead of copying and pasting code from the AI. We all use AI it's totally okay but you need to understand the code you are using and not blindly trust it.

## Features

* Print a customizable greeting like `Hello, Alice!` or `Hello, Universe!`
* Command line interface powered by [Click](https://click.palletsprojects.com/)
* Lightweight and dependency minimal
* Easy to extend for more complex greetings

## Installation

Make sure you have **Python 3.9+** installed.
You can install using [Poetry](https://python-poetry.org/) (recommended):

```bash
git clone https://github.com/theCompanyDream/hello-world.git
cd hello
poetry install
```

## Usage

After installation, a CLI command `hello` becomes available.

```bash
poetry run hello NAME
```

### Examples

```bash
hello World
# Output: Hello, World!

hello Tim
# Output: Hello, Tim!

hello Coffee
# Output: Hello, Coffee!
```

If no name is provided, it defaults to `World`.

## Development

Clone the repo and install dev dependencies:

```bash
git clone https://github.com/theCompanyDream/hello-world.git
cd hello
poetry install --with dev
```

Run tests:

```bash
pytest
```

## Project Structure

```
hello/
│   __init__.py
│   cli.py          # Entry point for the CLI
tests/
pyproject.toml
```

* **`hello/cli.py`** → Contains the CLI logic (powered by `click`).
* **`pyproject.toml`** → Project metadata and dependencies.
* **`tests/`** → Unit tests powered by `pytest`.

The entry point is defined in `pyproject.toml` under `[tool.poetry.scripts]`, mapping the command `hello` to the `cli()` function.

## Extending

This project is intentionally simple. You can extend it by:

* Adding more command-line options (e.g., `--shout` to uppercase greetings).
* Supporting multiple greetings (`Hi`, `Greetings`, etc.).
* Localizing greetings in different languages.

