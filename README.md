# Magazine authors data processing

Python scripts to process the exported Magazine authors data into the desired shape.

## Usage

1. download the file `magazine_authors_uncleaned.csv` from the Western Friend website
2. download the most recent "magazine authors merged" file from Western Friend docs
3. run `python magazine_authors_parser.py` to automatically split new author names
4. run `magazine_authors_merge_cleaned.ipynb` to produce merged authors for manual review
5. use the reviewed magazine authors in the new website content importer
