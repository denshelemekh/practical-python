#!/usr/bin/env python3
# report.py

"""
Portfolio Report Generation Module
© Denis Shelemekh, 2020
"""

# from Work import fileparse
import fileparse


def read_portfolio(filename) -> list:
    """
    Reads portfolio from file and returns it as the list of dictionaries
    """
    f = open(filename, 'rt')
    ret = fileparse.parse_csv(f, has_headers=True, types=[str, int, float])
    f.close()

    return ret


def read_prices(filename: str) -> dict:
    """
    Reads prices from file and returns it as the dictionary
    """

    f = open(filename, 'rt')
    prices = fileparse.parse_csv(f, has_headers=False, types=[str, float])
    f.close()
    prices = dict(prices)

    return prices


def make_report(portfolio: list, prices: dict) -> list:
    """
    Returns list of tuples for reporting
    """
    report = []
    for holding in portfolio:
        entry = holding['name'], holding['shares'], \
                prices[holding['name']], \
                prices[holding['name']] - holding['price']
        report.append(entry)
    return report


def convert_date(date: str) -> tuple:
    """
    Returns tuple consisting of date parts. Expected date format: '6/11/2007'
    """
    import re
    ro = re.compile(r'^(\d+)/(\d+)/(\d+)$')
    matches = ro.findall(date)
    matches = map(int, matches[0])
    return tuple(matches)


def print_report(report: list) -> None:
    """
    Prints nicely formatted report
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        str_price = f'${price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {str_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    """
    High-level wrapper for function calls
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv: list) -> None:
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} portfolio_filename prices_filename')
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
