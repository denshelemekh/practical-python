"""
"tail -f" like functions for tracing new stock quotes.

Uses generators functionality.

© Denis Shelemekh, 2020
"""

import os
import time
from typing import Iterable, Any

from . import report


def filematch(lines: Iterable[Any], substr: str) -> Any:
    """
    Generator function used to filter out records not containing substr.

    Args:
        lines: Iterable to process records from.
        substr: String to search for.
    Returns:
        Record containing substr in it (as implemented by record __contains__ method).
    """
    for line in lines:
        if substr in line:
            yield line


def follow(filename: str) -> str:
    """
    Generator function used for implementation of Linux "tail -f" functionality, i.e.
    watching and parsing in real time stock quotes.

    Args:
        filename: File to watch and process records from.
    Returns:
        Strings from file as they appear.
    """
    with open(filename, 'rt') as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if line == "":
                time.sleep(0.1)
            else:
                yield line


def main():
    """
    Main function.
    Reads the string feed, converts data and prints it to the screen.
    """
    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")


if __name__ == '__main__':
    main()
