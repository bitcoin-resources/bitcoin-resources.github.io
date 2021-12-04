# !/usr/bin/python3
# encoding=utf-8
import requests
import csv
from io import StringIO

# GET google-spreadsheet in .csv-format
# and convert from bytes to a list
spreadsheet_req = requests.get('https://docs.google.com/spreadsheets/d/17vjaS77T_roI0ksSR8x9bFzHm35bmiGN2NfpKMyQnus/export?format=csv&gid=1253985780')
spreadsheet_req = spreadsheet_req.content

spreadsheet_str = spreadsheet_req.decode(encoding='utf-8')
spreadsheet_out = StringIO(spreadsheet_str)
spreadsheet_csv = csv.reader(spreadsheet_out, delimiter=',')

list_of_ssdata = list(spreadsheet_csv)

# Export the links from the spreadsheet that hadn't been archived yet
# into 'article_links.txt' for later archiving
with open('article_links.txt', 'w+') as links:
    for link in list_of_ssdata[1:]:
        if 'https://archive' in link[2]:
            pass
        elif link[-3] == '':
            links.write(link[2] + '\n')
