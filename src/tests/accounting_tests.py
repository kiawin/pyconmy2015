import unittest
from accounting import Accounting
from unittest.mock import patch

class TestAccounting(unittest.TestCase):

    def setUp(self):
        self.a = Accounting()

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.a.add(1,2,3), 6, "Wrong additions")

    def test_sub(self):
        self.assertEqual(self.a.sub(1,2,3), -4, "Wrong subtractions")

    def test_mul(self):
        self.assertEqual(self.a.mul(1,2,3), 6, "Wrong multiplications")

    def test_div(self):
        self.assertAlmostEqual(self.a.div(1,2,3), 0.17, places=2, msg="Wrong divisions")


    # Not Unit Test
    # Reason: not single unit. involves opening a "instructions.yaml"
    # file and load as a list of dictionaries
    def test_process_ali(self):
        self.assertEqual(self.a.process("ali"), 5, "Wrong calculation")

    def test_process_ahhuat(self):
        self.assertEqual(self.a.process("ahhuat"), 33, "Wrong calculation")

    def test_process_mutu(self):
        self.assertEqual(self.a.process("mutu"), 0, "Wrong calculation")

    def test_process_paul(self):
        with self.assertRaisesRegex(Exception, "Haha Very Funny"):
            self.a.process("paul")

    # Unit Test
    @patch('builtins.open')
    @patch('yaml.load', return_value={'bob': [{'initial': 1}, {'add': [2, 3]}, {'sub': 1}]})
    def test_process(self, mock_load, mock_open):
        self.a = Accounting()
        self.assertEqual(self.a.process("bob"), 5, "Wrong calculation")


if __name__ == "__main__":
    unittest.main()
