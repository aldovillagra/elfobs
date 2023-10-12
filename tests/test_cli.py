from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["conf"])
    assert result.exit_code == 0
