"""Test suite runner for the FATD package.

This module runs all unit tests for the FATD package and generates a report.
"""

import unittest
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import test modules
from test_elements import TestRollDice, TestElementsModule
from test_tiles import TestTilesModule


def run_all_tests():
    """Run all unit tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestRollDice))
    suite.addTests(loader.loadTestsFromTestCase(TestElementsModule))
    suite.addTests(loader.loadTestsFromTestCase(TestTilesModule))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    result = run_all_tests()
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
