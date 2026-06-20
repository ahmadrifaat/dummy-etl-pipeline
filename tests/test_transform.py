import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransformData(unittest.TestCase):
    def test_clean_data(self):
        # Simulasi 
        raw_data = {
            'Title': ['T-shirt 1', 'Unknown Product'],
            'Price': ['$10.00', 'Price Unavailable'],
            'Rating': ['Rating: 4.8/5', 'Not Rated'],
            'Colors': ['3 Colors', 'None'],
            'Size': ['Size: M', 'Size: Unknown'],
            'Gender': ['Gender: Men', 'Gender: Unisex'],
            'timestamp': ['2023-01-01', '2023-01-01']
        }
        df_raw = pd.DataFrame(raw_data)
        
        # transform
        df_clean = transform_data(df_raw)
        
        # test
        self.assertNotIn('Unknown Product', df_clean['Title'].values)
        self.assertEqual(df_clean.iloc[0]['Price'], 160000.0)
        self.assertEqual(str(df_clean['Rating'].dtype), 'float64')

if __name__ == '__main__':
    unittest.main()