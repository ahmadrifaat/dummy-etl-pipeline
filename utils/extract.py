import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time

def scrape_fashion_studio():
    all_products = []
    base_url = "https://fashion-studio.dicoding.dev"
    session = requests.Session()

    print("Memulai proses Extract...")
    # range
    for page in range(1, 51):
        try:
            # perbaikan review
            if page == 1:
                url = f"{base_url}/"
            else:
                url = f"{base_url}/page{page}"
            
            response = session.get(url, timeout=10)
            
            # Error handling
            if response.status_code != 200:
                print(f"Halaman {page} tidak ditemukan (Status: {response.status_code}). Menghentikan scraping.")
                break

            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            container = soup.find('div', id='collectionList')
            if not container:
                print(f"Kontainer data tidak ditemukan di halaman {page}. Menghentikan scraping.")
                break

            cards = container.find_all('div', class_='collection-card')
            
            if len(cards) == 0:
                print(f"Tidak ada produk lagi di halaman {page}. Menghentikan scraping.")
                break

            for card in cards:
                title_tag = card.find('h3', class_='product-title')
                title = title_tag.text.strip() if title_tag else "Unknown Product"

                price_tag = card.find('span', class_='price') or card.find('p', class_='price')
                price = price_tag.text.strip() if price_tag else "Price Unavailable"

                details_data = {
                    'Title': title,
                    'Price': price,
                    'Rating': None,
                    'Colors': None,
                    'Size': None,
                    'Gender': None,
                    'timestamp': datetime.now().isoformat()
                }

                for p_tag in card.find_all('p'):
                    txt = p_tag.text.strip()
                    if 'Rating:' in txt: details_data['Rating'] = txt
                    elif 'Colors' in txt: details_data['Colors'] = txt
                    elif 'Size:' in txt: details_data['Size'] = txt
                    elif 'Gender:' in txt: details_data['Gender'] = txt

                all_products.append(details_data)

            time.sleep(0.2) # server break
            
        except requests.exceptions.RequestException as e:
            # Error handling 
            print(f"Gagal memuat halaman {page}: {e}")
            break 

    print(f"Proses Extract selesai. Berhasil mengambil {len(all_products)} produk mentah.")
    return pd.DataFrame(all_products)