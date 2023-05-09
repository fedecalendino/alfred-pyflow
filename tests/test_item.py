import requests
from pyflow.icon import Icon
from pyflow.item import Item
from pyflow.testing import WorklowTestCase
import ddt


@ddt.ddt
class TestItems(WorklowTestCase):
    @property
    def alfred_workflow_bundleid(self):
        return "com.bundle.test"

    @property
    def alfred_workflow_version(self):
        return "0.0.0"

    @ddt.data(
        ("200", "200 OK", True),
        ("404", "404 Not Found", False),
    )
    @ddt.unpack
    def test_success(self, status_code: str, text: str, ok: bool):
        def aux(wf):
            response = requests.get(f"http://httpstat.us/{wf.args[0]}")

            item: Item = wf.new_item(
                title=response.text,
                subtitle=response.url,
                valid=response.ok,
            )

            if response.ok:
                item.set_icon_file("./success.png")
            else:
                item.set_icon_builtin(Icon.ALERT_STOP)

        workflow = self.workflow()
        feedback = self.run_workflow(workflow, aux, status_code)

        item = feedback["items"][0]

        self.assertEqual(item["title"], text)
        self.assertEqual(item["subtitle"], f"http://httpstat.us/{status_code}")

        if ok:
            self.assertTrue(item["valid"])
            self.assertEqual(item["icon"]["path"], "./success.png")
            self.assertIsNone(item["icon"]["type"])
        else:
            self.assertFalse(item["valid"])
            self.assertEqual(item["icon"]["path"], str(Icon.ALERT_STOP))
            self.assertIsNone(item["icon"]["type"])

    def test_error(self):
        def aux(_):
            1 / 0

        workflow = self.workflow()
        feedback = self.run_workflow(workflow, aux)

        item = feedback["items"][0]

        self.assertEqual(item["title"], "division by zero")
        self.assertEqual(item["subtitle"], "Error while running workflow 'test:v0.0.0'")
        self.assertEqual(item["icon"]["path"], str(Icon.ALERT_STOP))
