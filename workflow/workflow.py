import os
import json
import sys
from typing import Dict, List
import logging
from logging import Logger, INFO, DEBUG

from .item import Item


ICON_ROOT = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources"
ICON_ERROR = os.path.join(ICON_ROOT, "AlertStopIcon.icns")


class Workflow:
    def __init__(self):
        self._env: Dict[str, str] = None
        self._items: List[dict] = []
        self._logger: Logger = None

    @property
    def args(self) -> List[str]:
        return sys.argv[1:]

    @property
    def env(self) -> Dict[str, str]:
        if self._env is None:
            self._env = dict(os.environ)

        return self._env

    @property
    def debugging(self):
        return self.env.get("alfred_debug") == "1"

    @property
    def logger(self) -> Logger:
        if self._logger is None:
            self._logger = logging.getLogger()
            self._logger.setLevel((INFO, DEBUG)[self.debugging])

        return self._logger

    @property
    def name(self) -> str:
        return self.env["alfred_workflow_name"]

    @property
    def temp_directory(self) -> str:
        return os.getenv("TMPDIR")

    @property
    def working_directory(self) -> str:
        return os.getenv("PWD")

    def run(self, func):
        try:
            func(self)
        except Exception as e:
            self.logger.exception(e)
            self.add_item(
                title=f"Error while running workflow '{self.name}'",
                subtitle=str(e),
                icon=ICON_ERROR,
            )

    def add_item(self, **kwargs) -> Item:
        item: Item = Item(self, **kwargs)
        self._items.append(item)

        return item

    def send_feedback(self):
        json.dump(self.serialized, sys.stdout)
        sys.stdout.flush()

    @property
    def serialized(self) -> dict:
        return {
            "items": list(
                map(
                    lambda item: item.serialized,
                    self._items,
                )
            )
        }
