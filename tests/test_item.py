import os
import unittest
from unittest.mock import patch

from pyflow.item import Item
from pyflow.workflow import Workflow

ENVIRONMENT = {
    "alfred_debug": "1",
    "alfred_workflow_bundleid": "com.bundle.name",
    "alfred_workflow_name": "name",
    "alfred_workflow_version": "0.0.0",
}


@patch.dict(os.environ, ENVIRONMENT, clear=True)
class TestItem(unittest.TestCase):
    def test_set_icon_file(self):
        wf: Workflow = Workflow()

        item: Item = wf.new_item(title="title")
        item.set_icon_file(path="./icon.png")

        self.assertEqual(item.serialized["icon"]["path"], "./icon.png")
        self.assertIsNone(item.serialized["icon"]["type"])
