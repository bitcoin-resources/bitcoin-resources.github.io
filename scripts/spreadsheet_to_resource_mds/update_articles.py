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

articles = client.open("Bitcoin Resources").worksheet("Articles")

NO_DATE = "1111-11-11"
NO_AUTHOR_LINKS = ""

for row in articles.get_all_values():
    if row[0] == 'Author':
        continue

    article_author = row[0]
    article_title = row[1].lstrip().rstrip()
    article_link = row[2].lstrip().rstrip()
    article_category = row[3]
    article_date = row[4] if row[4] != '' else NO_DATE
    article_lesson = row[5].lstrip().rstrip()

    md_file_path = title_to_file_path(article_title, 'articles')
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page\n"
                f"author: {article_author}\n"
                f"title: {article_title}\n"
                f"link: {article_link}\n"
                f"category: {article_category}\n"
                f"date: {article_date}\n"
                f"lesson: {article_lesson}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
