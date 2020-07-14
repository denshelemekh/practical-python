"""
Stock class.

Stores basic stock information.

© Denis Shelemekh, 2020
"""

from porty import typedproperty as tp


class Stock:
    """
    Class for holding stock-related data.
    """

    name = tp.String('name')
    shares = tp.Integer('shares')
    price = tp.Float('price')

    def __init__(self, name: str, shares: int, price: float) -> None:
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
        return f"Stock({self.name}, {self.shares}, {self.price})"
