import os
import unittest
from unittest import mock

from pyflow.workflow import Workflow
from pyflow.item import Item


class TestItem(unittest.TestCase):
    @mock.patch.dict(os.environ, {"alfred_workflow_name": "mock"}, clear=True)
    def test_set_icon_file(self):
        wf: Workflow = Workflow()

        item: Item = wf.add_item(title="title")
        item.set_icon_file(path="./icon.png")

        self.assertEqual(item.serialized["icon"]["path"], "./icon.png")
        self.assertIsNone(item.serialized["icon"]["type"])
