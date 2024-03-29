import csv

parsed_authors = []

with open("data/magazine_authors_uncleaned.csv") as authors_csv:
    authors = csv.DictReader(authors_csv)

    for author in authors:
        original_name = author["drupal_full_name"]
        author_split = original_name.split(sep=" ")
        family_name = author_split.pop()
        given_name = " ".join(author_split)

        parsed_author = {
            "given_name": given_name,
            "family_name": family_name,
            "drupal_full_name": original_name,
            "drupal_author_id": author["drupal_author_id"],
            "civicrm_id": author["civicrm_contact_id"],
        }

        parsed_authors.append(parsed_author)

with open("data/magazine_authors_parsed.csv", "w", newline="") as parsed_authors_csv:
    writer = csv.DictWriter(
        parsed_authors_csv,
        fieldnames=[
            "given_name",
            "family_name",
            "drupal_full_name",
            "drupal_author_id",
            "civicrm_id",
        ],
    )

    writer.writeheader()

    for author in parsed_authors:
        writer.writerow(author)
