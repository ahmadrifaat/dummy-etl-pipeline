import pandas as pd

def transform_data(df):
    if df.empty or 'Title' not in df.columns:
        print("Peringatan: DataFrame kosong atau tidak valid.")
        return df

    print("Memulai proses Transform...")
    df_clean = df.copy()

    # 1. Hapus data invalid 
    df_clean = df_clean[df_clean['Title'] != "Unknown Product"]
    df_clean = df_clean.dropna(subset=['Title', 'Price'])

    # 2. Transformasi Harga 
    df_clean['Price'] = df_clean['Price'].astype(str).str.replace('$', '').str.replace(',', '')
    df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce') 
    df_clean = df_clean.dropna(subset=['Price']) 
    df_clean['Price'] = df_clean['Price'] * 16000

    # 3. Transformasi Rating 
    df_clean['Rating'] = df_clean['Rating'].astype(str).str.extract(r'(\d+\.\d+|\d+)').astype(float)

    # 4. Transformasi Colors 
    df_clean['Colors'] = df_clean['Colors'].astype(str).str.extract(r'(\d+)').astype(int)

    # 5. Pembersihan Size & Gender 
    df_clean['Size'] = df_clean['Size'].astype(str).str.replace('Size: ', '').str.strip()
    df_clean['Gender'] = df_clean['Gender'].astype(str).str.replace('Gender: ', '').str.strip()

    # 6. Final Clean-up 
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna()

    df_clean = df_clean.reset_index(drop=True)
    df_clean.index = df_clean.index + 1

    return df_clean