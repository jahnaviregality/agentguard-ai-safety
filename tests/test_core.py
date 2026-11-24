import unittest
from agentguard.core import inspect_action, load_scenarios, requires_approval, summarize

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.items = load_scenarios()

    def test_fault_detection(self):
        self.assertEqual(inspect_action(self.items[2]), ['target_mismatch', 'missing_evidence:recipient_verified'])

    def test_policy(self):
        self.assertFalse(requires_approval(self.items[3], 'sensitive_only'))
        self.assertTrue(requires_approval(self.items[3], 'every_action'))
        with self.assertRaises(ValueError):
            requires_approval(self.items[0], 'invalid')

    def test_counts(self):
        self.assertEqual(summarize(self.items, 'every_action')['prompts'], 6)
        self.assertEqual(summarize(self.items, 'sensitive_only')['prompts'], 4)
        self.assertEqual(summarize(self.items, 'sensitive_only')['flagged_without_review_opportunity'], 1)

if __name__ == '__main__':
    unittest.main()
