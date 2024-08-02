import unittest
from src.add_intent import intent_check
from src.add_parameter import parameter_check


class MyTestCase(unittest.TestCase):
    def test_intent_check(self):

        TEST_1 = intent_check()
        TEST_2 = intent_check()
        TEST_3 = intent_check()
        TEST_4 = intent_check()

        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here

    def test_parameter_check(self):
        TEST_1 = parameter_check()
        TEST_2 = parameter_check()
        TEST_3 = parameter_check()
        TEST_4 = parameter_check()

        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
