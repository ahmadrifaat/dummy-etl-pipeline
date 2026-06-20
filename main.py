# Import fungsi dari folder utils
from utils.extract import scrape_fashion_studio
from utils.transform import transform_data
from utils.load import load_data

def run_pipeline():
    print("=== Memulai ETL Pipeline Fashion Studio ===")
    
    # Tahap 1: Extract
    df_raw = scrape_fashion_studio()
    
    if not df_raw.empty:
        # Tahap 2: Transform
        df_clean = transform_data(df_raw)
        
        if not df_clean.empty:
            # Tahap 3: Load
            load_data(df_clean)
            print("=== ETL Pipeline Selesai ===")
        else:
            print("Proses dihentikan: Data kosong setelah transformasi.")
    else:
        print("Proses dihentikan: Gagal mengambil data.")

if __name__ == "__main__":
    run_pipeline()