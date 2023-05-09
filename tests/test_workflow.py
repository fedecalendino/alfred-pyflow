from pyflow.testing import WorklowTestCase


class TestWorkflow(WorklowTestCase):
    @property
    def alfred_workflow_bundleid(self):
        return "com.bundle.test"

    @property
    def alfred_workflow_version(self):
        return "0.0.0"

    def test_properties(self):
        workflow = self.workflow

        self.assertTrue(workflow.debugging)
        self.assertEqual(workflow.bundleid, "com.bundle.test")
        self.assertEqual(workflow.name, "test")
        self.assertEqual(workflow.version, "0.0.0")
        self.assertEqual(workflow.cachedir, "/tmp/test")
