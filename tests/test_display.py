from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["display", "--help"])
    assert result.exit_code == 0


def test_providers():
    result = runner.invoke(app, ["display", "providers"])
    assert result.exit_code == 0


def test_monitors():
    result = runner.invoke(app, ["display", "monitors"])
    assert result.exit_code == 0


def test_active_monitors():
    result = runner.invoke(app, ["display", "active-monitors"])
    assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["display", "conf"])
    assert result.exit_code == 0
