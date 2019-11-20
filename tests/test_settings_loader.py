# -*- coding: utf-8 -*-

"""

Brief description.

Some other description
"""

from typing import TypedDict

import pytest

from settings_loader._settings_loader import SettingsLoader

_TEST_FILE_NAME = './tests/settings.toml'  # TODO: change path to file


class Settings(TypedDict):
    """Settings struct."""

    val1: str
    val2: int


def test_read_file_success():
    """Testing read file. Success result."""
    loader = SettingsLoader(file_name=_TEST_FILE_NAME, klass=Settings)

    with open(_TEST_FILE_NAME) as fp:
        file_data_read = fp.read()

    file_data_loader = loader._read_file()  # noqa: WPS437

    assert file_data_loader == file_data_read


def test_read_file_fail():
    """Testing read file. Error open file."""
    loader = SettingsLoader(file_name='WRONG', klass=Settings)

    with pytest.raises(FileNotFoundError):
        loader._read_file()  # noqa: WPS437


def test_get_settings():
    """Testing read settings fro, file."""
    loader = SettingsLoader(file_name=_TEST_FILE_NAME, klass=Settings)

    settings_read = loader.get_settings()
    settings_in_file = {'test': {'val1': 'val2', 'val2': 123}}

    assert settings_in_file == settings_read
