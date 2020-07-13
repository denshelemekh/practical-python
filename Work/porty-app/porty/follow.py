import os
import time

from . import report


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


def follow(filename: str):
    with open(filename, 'rt') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line == "":
                time.sleep(0.1)
            else:
                yield line


def main():
    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")


#if __name__ == '__main__':
   # main()
