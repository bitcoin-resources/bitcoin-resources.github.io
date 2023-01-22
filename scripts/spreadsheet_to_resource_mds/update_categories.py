#! /usr/bin/python3
import gspread
import json
import os
import re

from oauth2client.service_account import ServiceAccountCredentials
from util import author_to_file_path, get_excerpt_from_page, get_valid_author_slug, title_to_file_path

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

articles = client.open("Bitcoin Resources").worksheet("Book Categories")

for idx, row in enumerate(articles.get_all_values()):
    category_short = row[0].lstrip().rstrip()
    category_name = row[1].lstrip().rstrip()

    md_file_path = title_to_file_path(category_short, 'categories')
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page-category\n"
                f"title: {category_name}\n"
                f"short: {category_short}\n"
                f"order: {idx}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
