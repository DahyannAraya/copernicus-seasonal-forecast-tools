"""
Unit tests for seasonal_forecast_tools.time_utils.

This test suite covers:
- month_name_to_number: conversion of month names and numbers to integers, with validation
- calculate_leadtimes: computation of lead times (in hours) for various forecast configurations

"""

import unittest
from datetime import date
from seasonal_forecast_tools.utils.time_utils import (
    month_name_to_number,
    calculate_leadtimes,
)

class TestTimeUtils(unittest.TestCase):

    ### Test month_name_to_number with valid full name, abbreviation, and integer ###
    def test_month_name_to_number_valid_inputs(self):
        self.assertEqual(month_name_to_number("March"), 3)
        self.assertEqual(month_name_to_number("Mar"), 3)
        self.assertEqual(month_name_to_number(5), 5)

    ### Test month_name_to_number raises ValueError on invalid or empty input ###
    def test_month_name_to_number_invalid_inputs(self):
        with self.assertRaises(ValueError):
            month_name_to_number("")
        with self.assertRaises(ValueError):
            month_name_to_number("Mars")
        with self.assertRaises(ValueError):
            month_name_to_number(13)

    ### Test calculate_leadtimes for a valid period within the same year ###
    def test_calculate_leadtimes_normal_valid_period(self):
        year = 2023
        initiation = "March"
        valid_period = ["April", "May"]

        start_date = date(2023, 4, 1)
        end_date = date(2023, 5, 31)
        base_date = date(2023, 3, 1)

        expected_start = (start_date - base_date).days * 24
        expected_end = (
            (end_date - base_date).days * 24 + 24
        ) - 6  # 6 excludes the stop value

        leadtimes = calculate_leadtimes(year, initiation, valid_period)
        self.assertEqual(leadtimes[0], expected_start)
        self.assertEqual(leadtimes[-1], expected_end)

    ### Test calculate_leadtimes for a valid period that crosses into the next year ###
    def test_calculate_leadtimes_cross_year(self):
        year = 2023
        initiation = "December"
        valid_period = ["January", "February"]

        start_date = date(2024, 1, 1)
        end_date = date(2024, 2, 29)
        base_date = date(2023, 12, 1)

        expected_start = (start_date - base_date).days * 24
        expected_end = (
            (end_date - base_date).days * 24 + 24
        ) - 6  # 6 excludes the stop value

        leadtimes = calculate_leadtimes(year, initiation, valid_period)
        self.assertEqual(leadtimes[0], expected_start)
        self.assertEqual(leadtimes[-1], expected_end)

    ### Test calculate_leadtimes raises long range ###
    def test_calculate_leadtimes_cross_year_long_range(self):
        """
        Test that a valid long-range cross-year forecast (December to June)
        is correctly interpreted and does not raise an error.
        """
        year = 2023
        initiation = "November"
        valid_period = ["December", "June"]

        try:
            leadtimes = calculate_leadtimes(year, initiation, valid_period)
            self.assertIsInstance(leadtimes, list)
            self.assertGreater(len(leadtimes), 0)
        except ValueError:
            self.fail("calculate_leadtimes() raised ValueError unexpectedly.")

# Execute Tests
if __name__ == "__main__":
    TESTS = unittest.TestLoader().loadTestsFromTestCase(TestTimeUtils)
    unittest.TextTestRunner(verbosity=2).run(TESTS)
