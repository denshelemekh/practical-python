import unittest

from . import stock


class TestStockClass(unittest.TestCase):

    def setUp(self) -> None:
        # print("setUp entered")
        self.stock = stock.Stock('GOOG', 100, 490.1)

    def test_create(self) -> None:
        self.assertEqual(self.stock.name, 'GOOG')
        self.assertEqual(self.stock.shares, 100)
        self.assertEqual(self.stock.price, 490.1)

    def test_cost(self) -> None:
        self.assertEqual(self.stock.cost, 49010)

    def test_sell(self) -> None:
        self.stock.sell(25)
        self.assertEqual(self.stock.shares, 75)

    def test_repr(self) -> None:
        self.assertEqual(str(self.stock), 'Stock(GOOG, 100, 490.1)')

    def test_typed_props(self) -> None:
        with self.assertRaises(TypeError):
            self.stock.name = 985
        with self.assertRaises(TypeError):
            self.stock.shares = '100'
        with self.assertRaises(TypeError):
            self.stock.price = '98.1'

    def test_props_assigns(self) -> None:
        self.stock.name = 'IBM'
        self.stock.shares = 50
        self.stock.price = 100.1

        self.assertEqual(self.stock.name, 'IBM')
        self.assertEqual(self.stock.shares, 50)
        self.assertEqual(self.stock.price, 100.1)


if __name__ == '__main__':
    unittest.main()