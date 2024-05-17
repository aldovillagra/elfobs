from elfobs.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["obs", "--help"])
    assert result.exit_code == 0


# def test_toggle_stream():
#     result = runner.invoke(app, ["obs", "toggle-stream"])
#     assert result.exit_code == 0

# def test_start_stream():
#     result = runner.invoke(app, ["obs", "start-stream"])
#     assert result.exit_code == 0

# def test_stop_stream():
#     result = runner.invoke(app, ["obs", "stop-stream"])
#     assert result.exit_code == 0


def test_stream_status():
    result = runner.invoke(app, ["obs", "stream-status"])
    assert result.exit_code == 0


def test_scene_list():
    result = runner.invoke(app, ["obs", "scene-list"])
    assert result.exit_code == 0


def test_get_current_program_scene():
    result = runner.invoke(app, ["obs", "get-current-program-scene"])
    assert result.exit_code == 0


# def test_get_current_preview_scene():
#     result = runner.invoke(app, ["obs", "get-current-preview-scene"])
#     assert result.exit_code == 0


def test_conf():
    result = runner.invoke(app, ["obs", "conf"])
    assert result.exit_code == 0
