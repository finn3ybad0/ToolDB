import unittest
import os
from src.add_file import operation_check
from src.add_file import check_path
from src.add_file import match_check
from src.add_file import duplicate_check


class MyTestCase(unittest.TestCase):
    def test_operation_check(self):
        current_dir = os.path.dirname(__file__)

        intent = operation_check(os.path.join(current_dir, 'csv','test_intent.csv'))
        parameter = operation_check(os.path.join(current_dir, 'csv','test_parameter.csv'))
        intent_parameter = operation_check(os.path.join(current_dir, 'csv','test_intent_parameter.csv'))

        self.assertEqual(intent, 'INTENT')  # add assertion here
        self.assertEqual(parameter, 'PARAMETER')
        self.assertEqual(intent_parameter, 'INTENT_PARAMETER')

    def test_check_path(self):
        current_file_path = os.path.abspath(__file__)
        result = check_path(current_file_path)
        self.assertEqual(result, True)

    def test_match_check(self):

        adequate_file = match_check()
        inadequate_file = match_check()

        self.assertEqual(True, True)
        self.assertEqual(True, False)

    def test_duplicate_check(self):

        parameter_exist = duplicate_check()
        parameter_do_not_exist = duplicate_check()
        intent_exist = duplicate_check()
        intent_do_not_exist = duplicate_check()

        self.assertEqual(True, False)
        self.assertEqual(True, False)
        self.assertEqual(True, False)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
