#!/usr/bin/env python3
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.secho(f"Hello there {name}", fg=typer.colors.GREEN)

@app.command()
def goodbye(name: str):
    typer.secho(f"Goodbye {name}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()
