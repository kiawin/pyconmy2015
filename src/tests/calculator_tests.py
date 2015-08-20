from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.c = Calculator()

    def tearDown(self):
        pass

    def test_add(self):
        # NOTE: Bad failed assertion message. Just for fun :)
        self.assertEqual(self.c.add(1,2),3,"Alamak?")

    def test_sub(self):
        self.assertEqual(self.c.sub(1,2),-1,"Invalid subtraction")

    def test_mul(self):
        self.assertEqual(self.c.mul(1,2),2,"Invalid multiplication")

    def test_div(self):
        # Ref: http://stackoverflow.com/a/4842318/822340
        self.assertEqual(self.c.div(1,2),0.5,"Invalid division")

    def test_div_by_zero(self):
        with self.assertRaisesRegex(Exception, "Haha Very Funny"):
            self.c.div(1,0)


if __name__ == '__main__':
    unittest.main()
