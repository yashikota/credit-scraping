import csv
import glob
import json
import os


def convert(year: int):
    path = os.path.join("data", str(year))
    csv_files = glob.glob(f"{path}/*.csv")
    result = []

    for csv_file in csv_files:
        with open(csv_file) as f:
            reader = csv.reader(f)
            term, faculty, department = csv_file.split("/")[-1].split("-")
            print(f"Converting {term} {faculty} {department}")
            for row in reader:
                # 「授業名 X組」の対処
                if row[2][0].isascii() and row[2][0].isalpha() or row[2][0].isdigit():
                    row[1] = row[1] + " " + row[2]
                    row.pop(2)

                # 3つの要素がある場合
                if not (row[4].isdigit()):
                    row[2] = row[2] + " " + row[3] + " " + row[4]
                    row.pop(3)
                    row.pop(3)
                else:
                    row[2] = row[2] + " " + row[3]
                    row.pop(3)

                if len(row) != 24:
                    print(f"Skipping {len(row)}, {row[0]}")
                    continue

                # シラバスへのリンク
                original_syllabus_url = f"https://www.portal.oit.ac.jp/CAMJWEB/slbssbdr.do?value(risyunen)={year}&value(semekikn)=1&value(kougicd)={row[0]}&value(crclumcd)=10201200"
                syllabus_app_url = f"https://syllabus.oit.yashikota.com/{row[0]}"

                result.append(
                    {
                        "year": str(year),
                        "faculty": faculty,
                        "department": department.removesuffix(".csv"),
                        "term": term,
                        "original_syllabus_url": original_syllabus_url,
                        "syllabus_app_url": syllabus_app_url,
                        "numbering": row[0],
                        "lecture_title": row[1],
                        "person": row[2],
                        "enrollment": row[3],
                        "respondent": row[4],
                        "question1": row[5],
                        "question2": row[6],
                        "question3": row[7],
                        "question4": row[8],
                        "question5": row[9],
                        "question6": row[10],
                        "question7": row[11],
                        "question8": row[12],
                        "question9": row[13],
                        "G": row[14],
                        "A": row[15],
                        "B": row[16],
                        "C": row[17],
                        "D": row[18],
                        "F": row[19],
                        "*": row[20],
                        "pass_rate": row[21],
                        "GPA": row[22],
                        "GPA_median": row[23],
                    }
                )

    with open(f"{path}/{year}.json", "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    import sys

    convert(int(sys.argv[1]))
