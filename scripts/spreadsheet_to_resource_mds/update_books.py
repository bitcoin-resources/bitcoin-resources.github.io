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

books = client.open("Bitcoin Resources").worksheet("Books")

NO_DATE = "1111-11-11"
NO_AUTHOR_LINKS = ""

for row in books.get_all_values():
    if row[0] == 'Categories':
        continue

    resource_categories = row[0].split(',')
    resource_type = row[1].lower()
    resource_essential = row[2].lower()
    resource_title = row[3].title().replace(":", "&#58")
    resource_subtitle = row[4].replace(":", "&#58")
    resource_authors = row[5].lstrip().rstrip().split(',')
    resource_authors_twitter = row[6].lstrip().rstrip().split(',') if row[6] != '' else NO_AUTHOR_LINKS
    resource_url = row[7]
    resource_amazon_url = row[8]
    resource_wikipedia_url = row[9]
    resource_free_url = row[10]
    resource_summary = row[11]
    if row[12] != '':
        permalink_line = 'permalink: books/' + row[12] + '\n'
    else:
        permalink_line = ''
    resource_rating_order = row[13]
    resource_lesson = row[14].lstrip().rstrip().split(',')
    resource_audiobook = row[16]
    resource_audiobook_free = row[17]

    md_file_path = title_to_file_path(resource_title, resource_type)
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page-{resource_type}\n"
                f"title: {resource_title}\n"
                f"subtitle: {resource_subtitle}\n"
                f"essential: {resource_essential}\n"
                f"categories: {resource_categories}\n"
                f"authors: {resource_authors}\n"
                f"authors_twitter: {resource_authors_twitter}\n"
                f"resource_url: {resource_url}\n"
                f"amazon_url: {resource_amazon_url}\n"
                f"wikipedia_url: {resource_wikipedia_url}\n"
                f"free_url: {resource_free_url}\n"
                f"{permalink_line}"
                f"rating_order: {resource_rating_order}\n"
                f"lesson: {resource_lesson}\n"
                f"audio_url: {resource_audiobook}\n"
                f"free_audio_url: {resource_audiobook_free}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
