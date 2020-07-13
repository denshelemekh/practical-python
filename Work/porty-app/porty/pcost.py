#!/usr/bin/env python3
"""
Portfolio cost calculation module.

© Denis Shelemekh, 2020
"""
from typing import List

from . import report


def portfolio_cost(filename: str) -> float:
    """
    Computes the total cost of a portfolio of stocks stored in csv file
    Args:
        filename: String - filename to read from.
    Returns:
        Float number - portfolio cost.
    """
    port = report.read_portfolio(filename)
    return port.total_cost


def main(argv: List[str]) -> None:
    """
    Main function.
    Args:
        argv: List of command line arguments.
    """
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_filename')

    cost = portfolio_cost(argv[1])
    print(f'Total cost {cost:0.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
