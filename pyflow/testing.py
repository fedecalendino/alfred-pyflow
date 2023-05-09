import os
import subprocess
from unittest import TestCase

from pyflow.workflow import Workflow


class WorklowTestCase(TestCase):
    @staticmethod
    def cmd(command: str) -> str:
        output = subprocess.check_output(command, shell=True)
        return output.decode()

    @property
    def alfred_debug(self) -> str:
        return "1"

    @property
    def alfred_workflow_bundleid(self) -> str:
        return self.cmd("plutil -extract bundleid raw -o - ./info.plist")

    @property
    def alfred_workflow_name(self) -> str:
        return self.alfred_workflow_bundleid.split(".")[-1]

    @property
    def alfred_workflow_version(self) -> str:
        return self.cmd("poetry version --short")

    @property
    def alfred_workflow_cache(self) -> str:
        return f"/tmp/{self.alfred_workflow_name}"

    @property
    def workflow(self) -> Workflow:
        os.environ.setdefault("alfred_debug", self.alfred_debug)
        os.environ.setdefault("alfred_workflow_bundleid", self.alfred_workflow_bundleid)
        os.environ.setdefault("alfred_workflow_name", self.alfred_workflow_name)
        os.environ.setdefault("alfred_workflow_version", self.alfred_workflow_version)
        os.environ.setdefault("alfred_workflow_cache", self.alfred_workflow_cache)

        return Workflow()
