"""
Portfolio class.
"""
from collections import Counter

# try:
from . import fileparse
from . import stock
# except ImportError:
#     import fileparse
#     import stock


class Portfolio:

    def __init__(self):
        self.holdings = []

    def append(self, _stock: stock.Stock):
        if not isinstance(_stock, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(_stock)

    def __iter__(self):
        return self.holdings.__iter__()

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, index):
        return self.holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self.holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self.holdings)  # Generator expression

    def tabulate_shares(self):
        total_shares = Counter()
        for _stock in self.holdings:
            total_shares[_stock.name] += _stock.shares
        return total_shares

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        port_dicts = fileparse.parse_csv(lines,
                                         select=['name', 'shares', 'price'],
                                         types=[str, int, float],
                                         **opts)
        for d in port_dicts:
            self.append(stock.Stock(**d))

        return self
