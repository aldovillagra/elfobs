import typer

from elfobs import config, console
from elfobs.image import app as image_app

app = typer.Typer()
app.add_typer(image_app)


@app.callback()
def elfobs():
    """
    El Faro OBS
    """
    pass


@app.command()
def conf():
    """
    Show Global Configuration
    """
    console.print(config)


if __name__ == "__main__":
    app()
