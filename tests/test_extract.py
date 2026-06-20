import unittest
import pandas as pd
from unittest.mock import patch
from utils.extract import scrape_fashion_studio

class TestExtractData(unittest.TestCase):
    
    # Mock
    @patch('utils.extract.time.sleep', return_value=None)
    @patch('utils.extract.requests.Session.get')
    def test_extract_returns_dataframe(self, mock_get, mock_sleep):
        # Simulasi HTML 
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'''
        <div id="collectionList">
            <div class="collection-card">
                <h3 class="product-title">Baju Simulasi</h3>
                <span class="price">$50.00</span>
                <p>Rating: 4.5/5</p>
                <p>3 Colors</p>
                <p>Size: M</p>
                <p>Gender: Men</p>
            </div>
        </div>
        '''
        
        # Eksekusi fungsi extract
        df = scrape_fashion_studio()
        
        # Pengujian
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Title', df.columns)
        self.assertEqual(df.iloc[0]['Title'], 'Baju Simulasi')

if __name__ == '__main__':
    unittest.main()