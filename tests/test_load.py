import unittest
import pandas as pd
from unittest.mock import patch
from utils.load import load_data

class TestLoadData(unittest.TestCase):
    
    # Mock
    @patch('utils.load.create_engine')
    @patch('utils.load.gspread.authorize')
    @patch('utils.load.Credentials.from_service_account_file')
    @patch('pandas.DataFrame.to_csv')
    @patch('pandas.DataFrame.to_sql')
    def test_load_data_execution(self, mock_to_sql, mock_to_csv, mock_creds, mock_gspread, mock_engine):
        
        # Dummy Dataframe
        data = {'Title': ['Test Product'], 'Price': [160000.0]}
        df_dummy = pd.DataFrame(data)
        
        # load execution
        try:
            load_data(df_dummy)
            berhasil_tanpa_crash = True
        except Exception:
            berhasil_tanpa_crash = False
            
        # Pengujian
        self.assertTrue(berhasil_tanpa_crash)
        
        # CSV mock
        mock_to_csv.assert_called_once_with('products.csv', index=False)

if __name__ == '__main__':
    unittest.main()