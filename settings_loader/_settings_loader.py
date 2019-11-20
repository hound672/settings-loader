# -*- coding: utf-8 -*-

"""

Settings loader.

Class for loading settings
"""

from typing import cast, TypeVar, Type

import toml

TSettingsType = TypeVar('TSettingsType')


class SettingsLoader:
    """Class for loading settings."""

    def __init__(
        self,
        *,
        file_name: str,
        klass: Type[TSettingsType],
    ) -> None:
        """
        Create settings loaders inctance.

        :param file_name: name file of settings
        """
        self._file_name = file_name
        self._klass = klass

    def get_settings(self) -> TSettingsType:
        """Return settings."""
        raw_data = self._read_file()
        toml_data = toml.loads(raw_data)
        return cast(TSettingsType, toml_data)

    def _read_file(self) -> str:
        """Read file and return its content."""
        with open(self._file_name) as fp:
            return fp.read()
