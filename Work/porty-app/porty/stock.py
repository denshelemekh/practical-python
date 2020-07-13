"""
Stock class.

Stores basic stock information.
© Denis Shelemekh, 2020
"""

# try:
from . import typedproperty as tp
# except ImportError:
#     import typedproperty as tp


class Stock:
    """
    Class for holding stock-related data.
    """

    name = tp.String('name')
    shares = tp.Integer('shares')
    price = tp.Float('price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        """
        Class constructor.
        Args:
            name: Str - name of the stock.
            shares: Int - number of shares in the position.
            price: Float - price of one share.
        """
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self) -> float:
        """
        Calculates cost of the stock position.
        Returns:
            Cost of the position.
        """
        return self.shares * self.price

    def sell(self, shares: int) -> None:
        """
        'Sells' shares.
        Args:
            shares: Int - number of shares to sell.
        """
        self.shares -= shares

    def __repr__(self) -> str:
        """
        Returns:
            Representation of the instance.
        """
        return f"Stock({self.name}, {self.shares}, {self.price})"
