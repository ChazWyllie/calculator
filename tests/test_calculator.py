"""Unit tests for the calculator module."""

import unittest
import math

from src.calculator import Calculator
from src.enums import OperationType


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        self.assertEqual(self.calc.calculate("2 + 3"), 5.0)
        self.assertEqual(self.calc.calculate("10 - 4"), 6.0)
        self.assertEqual(self.calc.calculate("3 * 4"), 12.0)
        self.assertEqual(self.calc.calculate("10 / 2"), 5.0)
    
    def test_modulo_operation(self):
        """Test modulo operation."""
        self.assertEqual(self.calc.calculate("10 % 3"), 1.0)
    
    def test_power_operation(self):
        """Test power operations."""
        self.assertEqual(self.calc.calculate("2 ** 3"), 8.0)
        self.assertEqual(self.calc.calculate("2 ^ 3"), 8.0)
    
    def test_square_root(self):
        """Test square root function."""
        self.assertEqual(self.calc.calculate("sqrt(16)"), 4.0)
        self.assertEqual(self.calc.calculate("sqrt(25)"), 5.0)
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        result = self.calc.calculate("sin(pi/2)")
        self.assertAlmostEqual(result, 1.0, places=5)
        
        result = self.calc.calculate("cos(0)")
        self.assertAlmostEqual(result, 1.0, places=5)
    
    def test_logarithmic_functions(self):
        """Test logarithmic functions."""
        result = self.calc.calculate("log(100)")
        self.assertAlmostEqual(result, 2.0, places=5)
    
    def test_constants(self):
        """Test mathematical constants."""
        result = self.calc.calculate("pi")
        self.assertAlmostEqual(result, math.pi, places=5)
        
        result = self.calc.calculate("e")
        self.assertAlmostEqual(result, math.e, places=5)
    
    def test_implicit_multiplication(self):
        """Test implicit multiplication handling."""
        result = self.calc.calculate("2pi")
        self.assertAlmostEqual(result, 2 * math.pi, places=5)
    
    def test_complex_expression(self):
        """Test complex expressions."""
        result = self.calc.calculate("2 + 3 * 4")
        self.assertEqual(result, 14.0)
        
        result = self.calc.calculate("(2 + 3) * 4")
        self.assertEqual(result, 20.0)
    
    def test_division_by_zero(self):
        """Test division by zero handling."""
        result = self.calc.calculate("1 / 0")
        self.assertIn("Error", str(result))
    
    def test_invalid_expression(self):
        """Test invalid expression handling."""
        result = self.calc.calculate("")
        self.assertIn("Error", str(result))
        
        result = self.calc.calculate("(2 + 3")
        self.assertIn("Error", str(result))
    
    def test_calculation_history(self):
        """Test calculation history tracking."""
        self.calc.calculate("2 + 3")
        self.calc.calculate("5 * 2")
        history = self.calc.get_history()
        
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0][0], "2 + 3")
        self.assertEqual(history[0][1], 5.0)
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.calculate("2 + 3")
        self.calc.clear_history()
        history = self.calc.get_history()
        
        self.assertEqual(len(history), 0)
    
    def test_format_result(self):
        """Test result formatting."""
        self.assertEqual(Calculator.format_result(5.0), "5")
        self.assertEqual(Calculator.format_result(5.5), "5.50")
        self.assertEqual(Calculator.format_result("Error"), "Error")
    
    def test_batch_calculation(self):
        """Test batch calculation."""
        expressions = ["2 + 3", "4 * 5", "sqrt(16)"]
        results = self.calc.calculate_batch(expressions)
        
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], 5.0)
        self.assertEqual(results[1], 20.0)
        self.assertEqual(results[2], 4.0)
    
    def test_operation_type_detection(self):
        """Test operation type detection."""
        self.assertEqual(
            Calculator.get_operation_type("sin(x)"),
            OperationType.TRIGONOMETRIC
        )
        self.assertEqual(
            Calculator.get_operation_type("log(x)"),
            OperationType.LOGARITHMIC
        )
        self.assertEqual(
            Calculator.get_operation_type("2 ** 3"),
            OperationType.POWER
        )
        self.assertEqual(
            Calculator.get_operation_type("2 + 3"),
            OperationType.ARITHMETIC
        )


class TestCalculatorValidation(unittest.TestCase):
    """Test cases for expression validation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_empty_expression(self):
        """Test empty expression validation."""
        is_valid, error = self.calc.validate_expression("")
        self.assertFalse(is_valid)
        self.assertIn("Empty", error)
    
    def test_unbalanced_parentheses(self):
        """Test unbalanced parentheses detection."""
        is_valid, error = self.calc.validate_expression("(2 + 3")
        self.assertFalse(is_valid)
        self.assertIn("parentheses", error)
    
    def test_invalid_characters(self):
        """Test invalid character detection."""
        is_valid, error = self.calc.validate_expression("2 + 3 @")
        self.assertFalse(is_valid)
        self.assertIn("Invalid", error)
    
    def test_valid_expression(self):
        """Test valid expression passes validation."""
        is_valid, error = self.calc.validate_expression("2 + 3")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")


if __name__ == "__main__":
    unittest.main()
