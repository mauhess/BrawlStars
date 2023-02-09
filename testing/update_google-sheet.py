from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1AfQCLqsrDbbVnPznqktVOAGM0uWdItfh6wNi8toYIQE'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range="CONC_Modus!A1:B2").execute()
values = result.get('values', [])
print(values)

range = "CONC_Modus!A3"
data = [
    [11, 22],
    ["ab", "cd", "ef"]
]
request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED", body={"values": data}).execute()
print(request)
def update_data(range, data):
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED", body={"values": data}).execute()