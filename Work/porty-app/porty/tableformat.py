"""
TableFormatter module.

Defines following classes for outputting report data:
* TextTableFormatter - print a table in plain-text format
* CSVTableFormatter - output portfolio data in CSV format
* HTMLTableFormatter - output portfolio data in HTML format

© Denis Shelemekh, 2020
"""

from typing import List, Union, Tuple

# try:
from . import stock
from . import exceptions
# except ImportError:
#     import stock
#     import exceptions

class TableFormatter:
    """
    Abstract base class for table formatters.
    """

    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, row_data):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Print a table in plain-text format.
    """
    def headings(self, headers: Union[List[str], Tuple[str]]) -> None:
        """
        Output headers.
        Args:
             headers: List or tuple of str headers.
        """
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, row_data: Union[List[str], Tuple[str]]) -> None:
        """
        Output row.
        Args:
             row_data: List or tuple of str fields.
        """
        for field in row_data:
            print(f"{field:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers: Union[List[str], Tuple[str]]) -> None:
        """
        Output headers.
        Args:
             headers: List or tuple of str headers.
        """
        print(",".join(headers))

    def row(self, row_data: Union[List[str], Tuple[str]]) -> None:
        """
        Output row.
        Args:
             row_data: List or tuple of str fields.
        """
        print(",".join(row_data))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
    def headings(self, headers: Union[List[str], Tuple[str]]) -> None:
        """
        Output headers.
        Args:
             headers: List or tuple of str headers.
        """
        print("<tr>", end="")
        for header in headers:
            print(f"<th>{header}</th>", end="")
        print("</tr>")

    def row(self, row_data: Union[List[str], Tuple[str]]) -> None:
        """
        Output row.
        Args:
             row_data: List or tuple of str fields.
        """
        print("<tr>", end="")
        for field in row_data:
            print(f"<td>{field}</td>", end="")
        print("</tr>")


def create_formatter(fmt: str) -> TableFormatter:
    """
    Creates table formatter based on the input format.
    Args:
         fmt: Str - abbreviation of desired format.
         One of the following: txt/csv/html.
    Returns:
        Child of TableFormatter.
    Raises:
        ValueError: If fmt argument is not one of predefined.
    """

    if fmt == "txt":
        formatter = TextTableFormatter()
    elif fmt == "csv":
        formatter = CSVTableFormatter()
    elif fmt == "html":
        formatter = HTMLTableFormatter()
    else:
        raise exceptions.FormatError(f"Unknown table format {fmt}")

    return formatter


def print_table(portfolio: Union[List[stock.Stock], Tuple[stock.Stock]],
                columns: List[str],
                formatter: TableFormatter) -> None:
    """
    Generalized function for printing user-defined attributes of stocks.
    Args:
        portfolio: List or tuple of stocks.
        columns: List of attributes to print.
        formatter: TableFormatter object.
    """
    formatter.headings(columns)
    for _stock in portfolio:
        row = []
        for colname in columns:
            attr = getattr(_stock, colname)
            row.append(str(attr))
        formatter.row(row)
