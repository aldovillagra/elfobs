from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["sound", "--help"])
    assert result.exit_code == 0


def test_playback():
    result = runner.invoke(app, ["sound", "playback"])
    assert result.exit_code == 0


def test_capture():
    result = runner.invoke(app, ["sound", "capture"])
    assert result.exit_code == 0


def test_cards():
    result = runner.invoke(app, ["sound", "cards"])
    assert result.exit_code == 0


def test_mixer():
    result = runner.invoke(app, ["sound", "mixer"])
    assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["sound", "conf"])
    assert result.exit_code == 0
