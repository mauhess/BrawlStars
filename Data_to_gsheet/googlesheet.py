from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '/Users/mauricehess/Documents/BrawlStars_key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = '1AfQCLqsrDbbVnPznqktVOAGM0uWdItfh6wNi8toYIQE'
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def get_values_from_gsheet(spreadsheetID, range):
    result = sheet.values().get(spreadsheetId=spreadsheetID,
                                range=range).execute()
    return result.get('values', [])


def update_data(range, v):
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED",
                          body={"values": v}).execute()


def append(range, data):
    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED",
                                    body={"values": data}).execute()


def insert_row(sheetID):
    request_body = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': sheetID,
                        'dimension': 'ROWS',
                        'startIndex': 1,
                        'endIndex': 2
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=request_body
    ).execute()


def add_data(player, data):
    insert_row(player[1])
    update_data(player[0] + "!A2", data)


def get_timestamps(player):
    return get_values_from_gsheet(SPREADSHEET_ID, player[0] + "!A:A26")


def get_first_timestamp(player):
    return get_values_from_gsheet(SPREADSHEET_ID, player[0] + "!A2")
