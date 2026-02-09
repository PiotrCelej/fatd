"""Unit tests for the elements module."""

import unittest
from unittest.mock import patch
import elements


class TestRollDice(unittest.TestCase):
    """Test cases for the roll_dice function."""

    def test_roll_dice_single_die_single_side(self):
        """Test rolling a single die with one side."""
        result = elements.roll_dice(1, 1)
        self.assertEqual(result, 1, "Rolling 1d1 should always return 1")

    def test_roll_dice_single_die_six_sides(self):
        """Test rolling a single d6."""
        for _ in range(100):
            result = elements.roll_dice(1, 6)
            self.assertIn(result, range(1, 7), "1d6 should return values 1-6")

    def test_roll_dice_multiple_dice(self):
        """Test rolling multiple dice."""
        result = elements.roll_dice(2, 6)
        self.assertGreaterEqual(result, 2, "2d6 minimum is 2")
        self.assertLessEqual(result, 12, "2d6 maximum is 12")

    def test_roll_dice_many_dice(self):
        """Test rolling many dice."""
        result = elements.roll_dice(10, 20)
        self.assertGreaterEqual(result, 10, "10d20 minimum is 10")
        self.assertLessEqual(result, 200, "10d20 maximum is 200")

    def test_roll_dice_zero_dice(self):
        """Test rolling zero dice."""
        result = elements.roll_dice(0, 6)
        self.assertEqual(result, 0, "Rolling 0 dice should return 0")

    def test_roll_dice_large_numbers(self):
        """Test rolling with large numbers."""
        result = elements.roll_dice(100, 100)
        self.assertGreaterEqual(result, 100, "100d100 minimum is 100")
        self.assertLessEqual(result, 10000, "100d100 maximum is 10000")

    @patch('elements.random.randint')
    def test_roll_dice_deterministic(self, mock_randint):
        """Test roll_dice with mocked random values."""
        mock_randint.side_effect = [3, 4, 5]  # Returns 3, 4, 5 on successive calls
        result = elements.roll_dice(3, 6)
        self.assertEqual(result, 12, "3+4+5 should equal 12")
        self.assertEqual(mock_randint.call_count, 3, "randint should be called 3 times")

    @patch('elements.random.randint')
    def test_roll_dice_calls_randint_correctly(self, mock_randint):
        """Test that roll_dice calls randint with correct parameters."""
        mock_randint.return_value = 1
        elements.roll_dice(2, 8)
        self.assertEqual(mock_randint.call_count, 2, "Should call randint twice for 2d8")
        # Check that all calls were with correct parameters
        for call in mock_randint.call_args_list:
            args = call[0]
            self.assertEqual(args[0], 1, "First argument to randint should be 1")
            self.assertEqual(args[1], 8, "Second argument to randint should be 8")

    def test_roll_dice_distribution(self):
        """Test that roll_dice produces reasonable distribution."""
        # Roll 1d6 many times and check distribution
        results = [elements.roll_dice(1, 6) for _ in range(600)]
        
        # Each outcome should appear roughly 100 times (with some variance)
        for outcome in range(1, 7):
            count = results.count(outcome)
            # Allow for statistical variance - should be between 50-150
            self.assertGreater(count, 50, f"Outcome {outcome} appears too rarely")
            self.assertLess(count, 150, f"Outcome {outcome} appears too often")


class TestElementsModule(unittest.TestCase):
    """Test cases for the elements module overall."""

    def test_module_imports(self):
        """Test that the module imports successfully."""
        self.assertTrue(hasattr(elements, 'roll_dice'), "Module should have roll_dice function")

    def test_roll_dice_is_callable(self):
        """Test that roll_dice is a callable function."""
        self.assertTrue(callable(elements.roll_dice), "roll_dice should be callable")


if __name__ == '__main__':
    unittest.main()
