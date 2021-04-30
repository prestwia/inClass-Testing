from calc import calc
import unittest

c1 = calc()

class testCalc(unittest.TestCase):
    def test_add(self):
        # true tests
        self.assertEqual(c1.add(10, 5), 15)
        self.assertEqual(c1.add(-1, 10), 9)
        self.assertEqual(c1.add(-5, -5), -10)
        self.assertEqual(c1.add(5, -4), 1)
        self.assertEqual(c1.add(0, 0), 0)
        self.assertEqual(c1.add('a', 5), 'only ints allowed')

        # false test
        self.assertEqual(c1.add(10, 2), 15)

    def test_multiply(self):
        # true tests
        self.assertEqual(c1.multiply(4, 5), 20)
        self.assertEqual(c1.multiply(-1, 5), -5)
        self.assertEqual(c1.multiply(-5, -5), 25)
        self.assertEqual(c1.multiply(3, -9), -27)
        self.assertEqual(c1.multiply(0, 0), 0)
        self.assertEqual(c1.multiply(5, 0), 0)
        self.assertEqual(c1.multiply('a', 5), 'only ints allowed')

        # false test
        self.assertEqual(c1.multiply(10, 10), 5)

    def test_subtract(self):
        # true tests
        self.assertEqual(c1.subtract(10, 5), 5)
        self.assertEqual(c1.subtract(-1, 10), -11)
        self.assertEqual(c1.subtract(-5, -5), 0)
        self.assertEqual(c1.subtract(5, -4), 9)
        self.assertEqual(c1.subtract(0, 0), 0)
        self.assertEqual(c1.subtract('a', 5), 'only ints allowed')

        # false test
        self.assertEqual(c1.subtract(5, 5), 5)

    def test_divide(self):
        # true tests
        self.assertEqual(c1.divide(25, 5), 5)
        self.assertEqual(c1.divide(-5, 10), -0.5)
        self.assertEqual(c1.divide(-30, -5), 6)
        self.assertEqual(c1.divide(20, -4), -5)
        self.assertEqual(c1.divide(0, 0), 'undefined')
        self.assertEqual(c1.divide('a', 5), 'only ints allowed')

        # false test
        self.assertEqual(c1.divide(10, 10), 10)

if __name__ == '__main__':
    unittest.main()