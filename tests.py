#!/c/Users/narayac/AppData/Local/Programs/Python/Python39/python

import unittest
import subs
import json

class Testing(unittest.TestCase):
    """Test case for the azure subscription actions"""
    def test_01_status(self):
        """Verify the subscription creation status"""
        print("Running test 01: Subscription creation status check")
        stat = sub.create()
        response = json.loads(stat)
        self.assertEqual(response["status"], "success")

    def test_02_subscription_id(self):
        """Verify the whether it returned subscription id"""
        print("Running test case 02: Subscription id check")
        stat = sub.create()
        response = json.loads(stat)
        self.assertRegex(response["subscription_id"], r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')

    def test_03_subscription_delete_status(self):
        """Verify the subscription delete call status"""
        print("Running test case 03: Subscription delete status")
        stat = sub.delete()
        response = json.loads(stat)
        self.assertEqual(response["status"], "success")


if __name__ == "__main__":
    sub = subs.Subscription("subs01", "subscription01", "des")
    unittest.main()
