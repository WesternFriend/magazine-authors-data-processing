"""
Given a raw Drupal export of Magazine Authors,
parse the author name into given and family name columns.
"""

import csv

parsed_authors = []

with open("magazine_authors_uncleaned.csv", "r") as authors_csv:
    authors = csv.DictReader(authors_csv)

    for author in authors:
        original_name = author["drupal_full_name"]
        author_split = original_name.split(sep=" ")
        family_name = author_split.pop()
        given_name = " ".join(author_split)

        parsed_author = {
            "given_name": given_name,
            "family_name": family_name,
            "original_name": original_name,
            "drupal_author_id": author["drupal_author_id"],
        }

        parsed_authors.append(parsed_author)

with open("magazine_authors_parsed.csv", "w", newline="") as parsed_authors_csv:
    fieldnames = [
        "given_name",
        "family_name",
        "original_name",
        "drupal_author_id",
    ]
    writer = csv.DictWriter(
        parsed_authors_csv,
        fieldnames=fieldnames,
    )

    writer.writeheader()

    for author in parsed_authors:
        writer.writerow(author)
