from pyflow.testing import WorklowTestCase


class TestWorkflow(WorklowTestCase):
    @property
    def alfred_workflow_bundleid(self):
        return "com.bundle.test"

    @property
    def alfred_workflow_version(self):
        return "0.0.0"

    def test_params(self):
        def aux(wf):
            wf.new_item(
                title=wf.args[0],
                subtitle=wf.env["env1"],
            )

            wf.new_item(
                title=wf.args[1],
                subtitle=wf.env["env2"],
            )

        envs = {
            "env1": "env1",
            "env2": "env2",
        }

        args = ["arg1", "arg2"]

        workflow = self.workflow(**envs)

        self.assertTrue(workflow.debugging)
        self.assertEqual(workflow.bundleid, "com.bundle.test")
        self.assertEqual(workflow.name, "test")
        self.assertEqual(workflow.version, "0.0.0")
        self.assertEqual(workflow.cachedir, "/tmp/test")

        feedback = self.run_workflow(workflow, aux, *args)
        item1, item2 = feedback["items"]

        self.assertEqual(item1["title"], "arg1")
        self.assertEqual(item1["subtitle"], "env1")
        self.assertEqual(item2["title"], "arg2")
        self.assertEqual(item2["subtitle"], "env2")
