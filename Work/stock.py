class Stock:
    """
    Class for holding stock-related data.
    """

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
