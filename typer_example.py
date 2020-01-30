import typer


app = typer.Typer()


@app.command()
def display(color: str, reverse: bool = True):
    message = f"Hello from typer using {color} color!"
    if not reverse:
        typer.echo(typer.style(message, fg=color))
    else:
        typer.echo(typer.style(message[::-1], fg=color))


if __name__ == "__main__":
    app()