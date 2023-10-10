import typer

from elfobs import config, console
from elfobs.display import app as display_app
from elfobs.image import app as image_app
from elfobs.sound import app as sound_app

app = typer.Typer()
app.add_typer(image_app)
app.add_typer(sound_app)
app.add_typer(display_app)


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
