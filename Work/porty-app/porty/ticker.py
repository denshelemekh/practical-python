import csv

from . import follow
from . import report
from . import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def ticker(portfolio_filename: str,
           feed_filename: str,
           fmt: str = "txt") -> None:
    """

    """
    portfolio = report.read_portfolio(portfolio_filename)
    feed = parse_stock_data(follow.follow(feed_filename))
    rows = (row for row in feed if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        row_data = [row['name'], str(row['price']), str(row['change'])]
        formatter.row(row_data)


def main():
    ticker("Data/portfolio.csv", "Data/stocklog.csv")


if __name__ == '__main__':
    main()
