#!/bin/bash

echo "Removing collections..."
rm -v ../../collections/_articles/*.md
rm -v ../../collections/_books/*.md
rm -v ../../collections/_episodes/*.md

echo "Scraping collections from spreadsheet..."
python update_articles.py
python update_books.py
python update_sodes.py
