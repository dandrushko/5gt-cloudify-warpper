from cloudify.test_utils import workflow_test

import unittest


class TestBlueprint(unittest.TestCase):


    @workflow_test('5G-T-Cloudify-demo.yaml')
    def test_blueprint(self, cfy_local):
        cfy_local.execute('install', task_retries=1)
        raw_input()
        cfy_local.execute('uninstall', task_retries=1)
