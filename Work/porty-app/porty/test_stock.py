"""
Tests for Stock class.
"""
import unittest

from porty import stock


class TestStockClass(unittest.TestCase):
    """
    Class for testing Stock class.
    """

    def setUp(self) -> None:
        self.stock = stock.Stock('GOOG', 100, 490.1)

    def test_create(self) -> None:
        """
        Tests creation phase of Stock.
        """
        self.assertEqual(self.stock.name, 'GOOG')
        self.assertEqual(self.stock.shares, 100)
        self.assertEqual(self.stock.price, 490.1)

    def test_cost(self) -> None:
        """
        Tests of cost property works properly.
        """
        self.assertEqual(self.stock.cost, 49010)

    def test_sell(self) -> None:
        """
        Tests correct work of sell method.
        """
        self.stock.sell(25)
        self.assertEqual(self.stock.shares, 75)

    def test_repr(self) -> None:
        """
        Tests repr() gives correct string.
        """
        self.assertEqual(str(self.stock), 'Stock(GOOG, 100, 490.1)')

    def test_typed_props(self) -> None:
        """
        Tests if typed properties do not allow wrong type assignments.
        """
        with self.assertRaises(TypeError):
            self.stock.name = 985
        with self.assertRaises(TypeError):
            self.stock.shares = '100'
        with self.assertRaises(TypeError):
            self.stock.price = '98.1'

    def test_props_assigns(self) -> None:
        """
        Test set/get sides of typed properties.
        """
        self.stock.name = 'IBM'
        self.stock.shares = 50
        self.stock.price = 100.1

        self.assertEqual(self.stock.name, 'IBM')
        self.assertEqual(self.stock.shares, 50)
        self.assertEqual(self.stock.price, 100.1)


if __name__ == '__main__':
    unittest.main()
