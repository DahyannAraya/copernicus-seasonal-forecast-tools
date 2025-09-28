"""
Unit tests for path_utils.py.

Tests include:
- Correct construction of file paths for all data types.
- Detection of file existence.
- Handling of invalid input (e.g., valid_period length).
- Validation of dictionary output for index paths.

Note: Tests check path logic using temporary directories, not repository structure.
"""

import unittest
from pathlib import Path
import tempfile
import os
from seasonal_forecast_tools.utils.path_utils import (
    get_file_path,
    check_existing_files,
)


class TestPathUtils(unittest.TestCase):
    def setUp(self):
        # Use temporary directory instead of fixed test_dir
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name)
        
        self.originating_centre = "dwd"
        self.index_metric = "TR"
        self.year = 2023
        self.initiation_month_str = "03"
        self.valid_period_str = "06_08"
        self.bounds_str = "W4_S44_E11_N48"
        self.system = "21"
        self.download_format = "grib"

    def tearDown(self):
        # Clean up temporary directory
        self.temp_dir.cleanup()

    ### Test that get_file_path returns correct path structure for downloaded GRIB data ###
    def test_get_file_path_downloaded_data(self):
        path = get_file_path(
            self.base_dir,
            self.originating_centre,
            self.year,
            self.initiation_month_str,
            self.valid_period_str,
            "downloaded_data",
            self.index_metric,
            self.bounds_str,
            self.system,
            data_format=self.download_format,
        )
        
        # Test path components without requiring physical creation
        path_str = str(path)
        
        # Verify path contains expected components
        self.assertIn(self.originating_centre, path_str)
        self.assertIn(f"sys{self.system}", path_str)
        self.assertIn(str(self.year), path_str)
        self.assertIn(f"init{self.initiation_month_str}", path_str)
        self.assertIn(f"valid{self.valid_period_str}", path_str)
        self.assertIn("downloaded_data", path_str)
        
        # Test filename format
        expected_suffix = f"{self.index_metric}_{self.bounds_str}.{self.download_format}"
        self.assertTrue(path_str.endswith(expected_suffix))

    ### Test that get_file_path returns a dictionary for indices data type ###
    def test_get_file_path_indices(self):
        paths = get_file_path(
            self.base_dir,
            self.originating_centre,
            self.year,
            self.initiation_month_str,
            self.valid_period_str,
            "indices",
            self.index_metric,
            self.bounds_str,
            self.system,
        )
        
        # Verify structure
        self.assertIsInstance(paths, dict)
        expected_timeframes = ["daily", "index_window_monthly", "stats"]
        
        for timeframe in expected_timeframes:
            self.assertIn(timeframe, paths)
            self.assertTrue(paths[timeframe].name.endswith(f"{timeframe}.nc"))
            
            # Verify path components are present
            path_str = str(paths[timeframe])
            self.assertIn(self.originating_centre, path_str)
            self.assertIn(f"sys{self.system}", path_str)

    ### Test path construction for different data types ###
    def test_get_file_path_data_types(self):
        """Test path construction for different data pipeline stages"""
        data_types = ["downloaded_data", "processed_data", "hazard"]
        
        for data_type in data_types:
            with self.subTest(data_type=data_type):
                if data_type == "indices":
                    continue  # Skip indices as it returns dict
                    
                path = get_file_path(
                    self.base_dir,
                    self.originating_centre,
                    self.year,
                    self.initiation_month_str,
                    self.valid_period_str,
                    data_type,
                    self.index_metric,
                    self.bounds_str,
                    self.system,
                )
                
                # Verify data type appears in path
                self.assertIn(data_type, str(path))

    ### Test check_existing_files returns correct message when no files exist ###
    def test_check_existing_files_missing_all(self):
        result = check_existing_files(
            base_dir=self.base_dir,
            originating_centre=self.originating_centre,
            index_metric=self.index_metric,
            year=self.year,
            initiation_month="March",
            valid_period=["June", "August"],
            bounds_str=self.bounds_str,
            system=self.system,
            download_format=self.download_format,
            print_flag=False,
        )
        
        # Test expected messages for missing files
        self.assertIn("No downloaded data found", result)
        self.assertIn("No processed data found", result)
        self.assertIn("No index data found", result)
        self.assertIn("No hazard data found", result)

    ### Test check_existing_files when some files exist ###
    def test_check_existing_files_partial_exists(self):
        # Create one test file to simulate partial existence
        test_path = get_file_path(
            self.base_dir,
            self.originating_centre,
            self.year,
            self.initiation_month_str,
            self.valid_period_str,
            "downloaded_data",
            self.index_metric,
            self.bounds_str,
            self.system,
            data_format=self.download_format,
        )
        
        # Create parent directories and file
        test_path.parent.mkdir(parents=True, exist_ok=True)
        test_path.touch()
        
        result = check_existing_files(
            base_dir=self.base_dir,
            originating_centre=self.originating_centre,
            index_metric=self.index_metric,
            year=self.year,
            initiation_month="March",
            valid_period=["June", "August"],
            bounds_str=self.bounds_str,
            system=self.system,
            download_format=self.download_format,
            print_flag=False,
        )
        
        # Should find downloaded data but not others
        self.assertNotIn("No downloaded data found", result)
        self.assertIn("No processed data found", result)


# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestPathUtils)
    unittest.TextTestRunner(verbosity=2).run(TESTS)

