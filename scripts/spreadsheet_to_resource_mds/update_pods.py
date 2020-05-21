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

sodes = client.open("Bitcoin Resources").worksheet("Podcasts")

EMPTY = ""

for row in sodes.get_all_values():
    if row[0] == 'Code':
        continue

    pod_code = row[0]
    pod_name = row[1].lstrip().rstrip()
    pod_hosts = row[2].lstrip().rstrip()
    pod_link = row[3].lstrip().rstrip()
    pod_tier = row[4]
    pod_ios = row[5].lstrip().rstrip()
    pod_android = row[6].lstrip().rstrip().split(',')
    pod_spotify = row[7] if row[7] != '' else EMPTY
    pod_rss = row[8].lstrip().rstrip().split(',')
    pod_rank = row[9]
    pod_twitter = row[10].lstrip().rstrip()
    pod_youtube = row[11].lstrip().rstrip() if row[11] != '' else EMPTY

    md_file_path = '../../collections/_podcasts/' + pod_code + '.md'
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page\n"
                f"code: {pod_code}\n"
                f"name: {pod_name}\n"
                f"hosts: {pod_hosts}\n"
                f"link: {pod_link}\n"
                f"tier: {pod_tier}\n"
                f"ios: {pod_ios}\n"
                f"android: {pod_android}\n"
                f"spotify: {pod_spotify}\n"
                f"rss: {pod_rss}\n"
                f"rank: {pod_rank}\n"
                f"twitter: {pod_twitter}\n"
                f"youtube: {pod_youtube}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
