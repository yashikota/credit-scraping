import sys

from convert import convert
from extract import extract
from scraping import scraping


def main():
    year = int(sys.argv[1])
    if year <= 2019:
        print("Cannot get data before 2019")
        return

    scraping(year)
    extract(year)
    convert(year)


if __name__ == "__main__":
    main()
