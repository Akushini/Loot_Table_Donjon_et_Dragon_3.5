import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


def auth():

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet1 = client.open("Tableaux Donjon & Dragon 3.5 loot").worksheet('Merveilleux faible')
    sheet2 = client.open("Tableaux Donjon & Dragon 3.5 loot").worksheet('Merveilleux intermédiaire')
    sheet3 = client.open("Tableaux Donjon & Dragon 3.5 loot").worksheet('Merveilleux puissant')
    sheetlist = [sheet1, sheet2, sheet3]
    return sheetlist

