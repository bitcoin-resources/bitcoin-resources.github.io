Instructions:

Credential setup:
1. Go to [Google API Console](https://console.developers.google.com/)
2. Create a new project
3. Click `Enable API` for `Google Sheets API`
4. `Create credentials` for a `Web Server` to access `Application Data`.
5. Name the service account and grant it a `Project` role of `Editor`.
6. Download the JSON file.
7. Copy the JSON file to `scripts/spreadsheet_to_resource_mds` and re-name it `client_secret.json`.
8. Find `client_email` inside `client_secret.json` and paste the email into `Share` in your Google Spreadsheet.


Download requirements and run:
```
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt

python spreadsheet_to_resource_mds.py
```
