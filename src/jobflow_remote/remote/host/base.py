from __future__ import annotations

import abc
from pathlib import Path

from monty.json import MSONable


class BaseHost(MSONable):
    """Base Host class."""

    @abc.abstractmethod
    def execute(
        self,
        command: str | list[str],
        workdir: str | Path | None = None,
        timeout: int | None = None,
    ):
        """Execute the given command on the host

        Parameters
        ----------
        command: str or list of str
            Command to execute, as a str or list of str
        workdir: str or None
            path where the command will be executed.

        """
        # TODO: define a common error that is raised or a returned in case the procedure
        # fails to avoid handling different kind of errors for the different hosts
        raise NotImplementedError

    @abc.abstractmethod
    def mkdir(self, directory, recursive: bool = True, exist_ok: bool = True) -> bool:
        """Create directory on the host."""
        # TODO: define a common error that is raised or a returned in case the procedure
        # fails to avoid handling different kind of errors for the different hosts
        raise NotImplementedError

    @abc.abstractmethod
    def write_text_file(self, filepath, content):
        """Write content to a file on the host."""
        # TODO: define a common error that is raised or a returned in case the procedure
        # fails to avoid handling different kind of errors for the different hosts
        raise NotImplementedError

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self) -> bool:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def is_connected(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def put(self, src, dst):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, src, dst):
        raise NotImplementedError

    @abc.abstractmethod
    def copy(self, src, dst):
        raise NotImplementedError
