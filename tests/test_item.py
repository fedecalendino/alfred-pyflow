import os
import unittest
from unittest.mock import patch

from pyflow.icon import Icon
from pyflow.item import Item
from pyflow.workflow import Workflow

ENVIRONMENT = {
    "alfred_debug": "1",
    "alfred_workflow_bundleid": "com.bundle.name",
    "alfred_workflow_cache": "/tmp",
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

    def test_error(self):
        wf: Workflow = Workflow()
        wf.run(lambda _: 1 / 0)

        item: dict = wf.serialized["items"][0]

        self.assertEqual(item["title"], "Error while running workflow 'name:v0.0.0'")
        self.assertEqual(item["subtitle"], "division by zero")
        self.assertEqual(item["icon"]["path"], str(Icon.ALERT_STOP))
