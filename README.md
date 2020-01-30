# Building command line interfaces in Python

Read the blog: [Building command line interfaces in Python](https://stribny.name/blog/2020/01/building-command-line-interfaces-in-python).

There are two examples in the repo:

- `click_example.py` utilizing Click and Rich libraries to make progress bar, create tables and use colors
- `typer_example.py` utilizing Typer and Python types to define CLI commands

Run with:
```shell
poetry shell

python click_example.py compute some words as arguments

python typer_example.py --no-reverse blue
```
