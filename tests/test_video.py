from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["video", "--help"])
    assert result.exit_code == 0


def test_check():
    result = runner.invoke(app, ["video", "check"])
    assert result.exit_code == 0


def test_show():
    result = runner.invoke(app, ["video", "show"])
    assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["video", "conf"])
    assert result.exit_code == 0
