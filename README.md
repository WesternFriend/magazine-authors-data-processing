# Magazine Authors data processing

Python scripts to process the exported Magazine Authors data into the desired shape.

## Data processing steps

1. export raw Magazine Authors from Drupal
2. download the previously cleaned and de-duped authors file from Nextcloud
3. use the `magazine_authors_name_parser.py` script to separate author names into `given_name` and `family_name` columns
4. Use `magazine_authors_merge_cleaned.ipynb` to merge the newly parsed authors into the previously cleaned, deduped authors file
5. upload the newly merged authors file to Nextcloud, so Mary can manually review and identify potential duplicates
