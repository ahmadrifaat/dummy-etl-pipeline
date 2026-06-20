import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from sqlalchemy import create_engine
import urllib.parse 

def load_data(df):
    print("Memulai proses Load...")
    
    # load csv
    try:
        df.to_csv('products.csv', index=False)
        print("Berhasil menyimpan ke products.csv")
    except Exception as e:
        print(f"Gagal menyimpan ke CSV: {e}")

    # 2. load google sheets
    try:
        scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file('google-sheets-api.json', scopes=scopes)
        gc = gspread.authorize(credentials)
        
        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1da_S99NcBK1UrJh8vPhw51C88tiDtf_FwpZX4RTnmCU/edit?usp=sharing'
        sh = gc.open_by_url(spreadsheet_url)
        worksheet = sh.get_worksheet(0)
        
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Berhasil menyimpan ke Google Sheets")
    except Exception as e:
        print(f"Gagal ke Google Sheets: {e}")

    # 3. load postgresql
    try:
        password = "Ardm251;"
        safe_password = urllib.parse.quote_plus(password)
        db_uri = f'postgresql+pg8000://postgres:{safe_password}@127.0.0.1:5432/fashion_db'
        engine = create_engine(db_uri)
        
        df.to_sql('competitor_products', engine, if_exists='replace', index=False)
        print("Berhasil menyimpan ke PostgreSQL")
    except Exception as e:
        print(f"Gagal ke PostgreSQL: {e}")