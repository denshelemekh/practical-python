#!/usr/bin/env python3
# pcost.py

# from Work import report
import report

def portfolio_cost(filename: str) -> float:
    """
    Computes the total cost (shares * price) of a portfolio of stocks stored in csv file
    """

    total_cost = 0
    portfolio = report.read_portfolio(filename)

    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']

    return total_cost


def main(argv: list) -> None:
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_filename')

    cost = portfolio_cost(argv[1])
    print(f'Total cost {cost:0.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)

