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

sodes = client.open("Bitcoin Resources").worksheet("Episodes")

NO_DATE = "1111-11-11"
NO_AUTHOR_LINKS = ""

for row in sodes.get_all_values():
    if row[0] == 'Episode':
        continue

    sode_episode = row[0]
    sode_podcast = row[1].lstrip().rstrip()
    sode_hosts = row[2].lstrip().rstrip()
    sode_date = row[3] if row[3] != '' else NO_DATE
    sode_guest = row[4].lstrip().rstrip()
    sode_title = sode_guest + ' ' + row[5].lstrip().rstrip()
    sode_lesson = row[7].lstrip().rstrip().split(',')
    sode_link = row[8]

    md_file_path = '../../collections/_episodes/' + sode_podcast + str(sode_episode) + '.md'
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page\n"
                f"title: {sode_title}\n"
                f"podcast: {sode_podcast}\n"
                f"episode: {sode_episode}\n"
                f"hosts: {sode_hosts}\n"
                f"date: {sode_date}\n"
                f"guest: {sode_guest}\n"
                f"lesson: {sode_lesson}\n"
                f"link: {sode_link}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
