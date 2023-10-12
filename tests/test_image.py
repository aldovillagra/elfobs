from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["image", "--help"])
    assert result.exit_code == 0


def test_output():
    result = runner.invoke(app, ["image", "output"])
    assert result.exit_code == 0


def test_create():
    result = runner.invoke(app, ["image", "create"])
    assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["image", "conf"])
    assert result.exit_code == 0
