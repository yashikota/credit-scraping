import argparse

from convert import convert
from extract import extract
from scraping import scraping


def main(year: int):
    if year <= 2019:
        print("Cannot get data before 2019")
        return

    scraping(year)
    extract(year)
    convert(year)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y", "--year", type=int, help="The year to scrape", required=True
    )
    main(parser.parse_args().year)
