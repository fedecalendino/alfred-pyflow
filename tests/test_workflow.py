import os
import unittest
from unittest.mock import patch

from pyflow.workflow import Workflow


ENVIRONMENT = {
    "alfred_debug": "1",
    "alfred_workflow_bundleid": "com.bundle.name",
    "alfred_workflow_cache": "/tmp",
    "alfred_workflow_name": "name",
    "alfred_workflow_version": "0.0.0",
}


@patch.dict(os.environ, ENVIRONMENT, clear=True)
class TestWorkflow(unittest.TestCase):
    def test_properties(self):
        workflow = Workflow()

        self.assertEqual(workflow.bundleid, "com.bundle.name")
        self.assertEqual(workflow.name, "name")
        self.assertEqual(workflow.version, "0.0.0")
        self.assertTrue(workflow.debugging)
