import csv
import glob
import os
import re
import unicodedata

import pypdfium2 as pdfium


def extract(year: int):
    pdf_files = glob.glob(f"{os.path.join('data', str(year))}/*.pdf")
    for pdf in pdf_files:
        p = pdfium.PdfDocument(pdf)
        pdf_pages = len(p)
        result = []

        for i in range(pdf_pages):
            page = p[i]
            text_page = page.get_textpage()
            all_text = text_page.get_text_bounded()
            lines = all_text.splitlines()

            for line in lines:
                if re.match(r"^\d{1,2} ", line):
                    result.append(unicodedata.normalize("NFKC", line).split(" ")[1:])

            filename = os.path.splitext(os.path.basename(pdf))[0]
            path = os.path.join("data", str(year))

            with open(f"{path}/{filename}.csv", "w") as f:
                writer = csv.writer(f, lineterminator="\n")
                writer.writerows(result)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y", "--year", type=int, help="The year to scrape", required=True
    )
    extract(parser.parse_args().year)
