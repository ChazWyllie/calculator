"""Core calculator implementation."""

import math
import re
from typing import Union, List, Tuple, Dict, Any
from decimal import Decimal, getcontext

from .enums import OperationType


# Set decimal precision for accurate calculations
getcontext().prec = 50


class Calculator:
    """
    A comprehensive calculator class that supports various mathematical operations.
    
    Supported operations:
    - Basic arithmetic: +, -, *, /, %
    - Power operations: **, ^
    - Trigonometric functions: sin, cos, tan, asin, acos, atan
    - Logarithmic functions: log, log10, ln
    - Statistical functions: sum, avg, min, max
    - Constants: pi, e, phi, tau
    
    Example:
        >>> calc = Calculator()
        >>> calc.calculate("2 + 3 * 4")
        14.0
        >>> calc.calculate("sqrt(16)")
        4.0
        >>> calc.calculate("sin(pi/2)")
        1.0
    """
    
    # Predefined constants
    CONSTANTS: Dict[str, float] = {
        'pi': math.pi,
        'e': math.e,
        'phi': (1 + math.sqrt(5)) / 2,  # Golden ratio
        'tau': 2 * math.pi,
    }
    
    # Supported mathematical functions
    FUNCTIONS: Dict[str, callable] = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sinh': math.sinh,
        'cosh': math.cosh,
        'tanh': math.tanh,
        'sqrt': math.sqrt,
        'exp': math.exp,
        'log': math.log10,
        'log10': math.log10,
        'ln': math.log,
        'abs': abs,
        'floor': math.floor,
        'ceil': math.ceil,
        'round': round,
        'degrees': math.degrees,
        'radians': math.radians,
        'factorial': math.factorial,
    }
    
    def __init__(self, verbose: bool = False):
        """
        Initialize the Calculator.
        
        Args:
            verbose: If True, display detailed calculation steps
        """
        self.verbose = verbose
        self.calculation_history: List[Tuple[str, Union[float, str]]] = []
        self.last_result: Union[float, str, None] = None
    
    def validate_expression(self, expression: str) -> Tuple[bool, str]:
        """
        Validate the mathematical expression before evaluation.
        
        Args:
            expression: The expression to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check for empty expression
        if not expression or not expression.strip():
            return False, "Error: Empty expression provided."
        
        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            return False, "Error: Unbalanced parentheses."
        
        # Check for valid characters
        allowed_chars = set('0123456789+-*/%^.()abcdefghijklmnopqrstuvwxyz_ ')
        if not all(c.lower() in allowed_chars for c in expression):
            return False, "Error: Invalid characters in expression."
        
        return True, ""
    
    def preprocess_expression(self, expression: str) -> str:
        """
        Preprocess the expression to replace constants and handle special cases.
        
        Args:
            expression: The raw expression string
            
        Returns:
            The processed expression string
        """
        processed = expression.lower().strip()
        
        # Replace constants
        for const_name, const_value in self.CONSTANTS.items():
            processed = re.sub(r'\b' + const_name + r'\b', str(const_value), processed)
        
        # Replace ^ with ** for exponentiation
        processed = processed.replace('^', '**')
        
        # Add multiplication operator where needed (e.g., "2pi" -> "2*pi")
        processed = re.sub(r'(\d)([a-z])', r'\1*\2', processed)
        processed = re.sub(r'(\))(\()', r'\1*\2', processed)
        processed = re.sub(r'(\d)(\()', r'\1*\2', processed)
        processed = re.sub(r'(\))(\d)', r'\1*\2', processed)
        
        return processed
    
    def calculate(self, expression: str) -> Union[float, str]:
        """
        Calculate the result of a mathematical expression.
        
        Args:
            expression: The mathematical expression to evaluate
            
        Returns:
            The result of the calculation or an error message
        """
        # Validate expression
        is_valid, error_msg = self.validate_expression(expression)
        if not is_valid:
            self.calculation_history.append((expression, error_msg))
            return error_msg
        
        try:
            # Preprocess the expression
            processed = self.preprocess_expression(expression)
            
            if self.verbose:
                print(f"Processing expression: {processed}")
            
            # Create a safe evaluation environment
            safe_dict: Dict[str, Any] = {
                '__builtins__': {},
                **self.FUNCTIONS,
                **self.CONSTANTS,
            }
            
            # Evaluate the expression
            result = eval(processed, safe_dict)
            
            # Store in history and as last result
            self.calculation_history.append((expression, result))
            self.last_result = result
            
            return result
        
        except ZeroDivisionError:
            error_msg = "Error: Division by zero."
            self.calculation_history.append((expression, error_msg))
            return error_msg
        
        except ValueError as e:
            error_msg = f"Error: Invalid mathematical operation - {str(e)}"
            self.calculation_history.append((expression, error_msg))
            return error_msg
        
        except Exception as e:
            error_msg = f"Error: {type(e).__name__} - {str(e)}"
            self.calculation_history.append((expression, error_msg))
            return error_msg
    
    def calculate_batch(self, expressions: List[str]) -> List[Union[float, str]]:
        """
        Calculate multiple expressions in batch.
        
        Args:
            expressions: List of expressions to evaluate
            
        Returns:
            List of results
        """
        return [self.calculate(expr) for expr in expressions]
    
    def get_history(self, limit: int = None) -> List[Tuple[str, Union[float, str]]]:
        """
        Get calculation history.
        
        Args:
            limit: Maximum number of history entries to return
            
        Returns:
            List of (expression, result) tuples
        """
        if limit is None:
            return self.calculation_history
        return self.calculation_history[-limit:]
    
    def clear_history(self):
        """Clear the calculation history."""
        self.calculation_history = []
        self.last_result = None
    
    @staticmethod
    def format_result(result: Union[float, str], decimal_places: int = 2) -> str:
        """
        Format the result for display.
        
        Args:
            result: The calculation result
            decimal_places: Number of decimal places to display
            
        Returns:
            Formatted result string
        """
        if isinstance(result, str):
            return result
        
        if isinstance(result, float):
            if result == int(result):
                return str(int(result))
            return f"{result:.{decimal_places}f}"
        
        return str(result)
    
    @staticmethod
    def get_operation_type(expression: str) -> OperationType:
        """
        Determine the type of operation in an expression.
        
        Args:
            expression: The expression to analyze
            
        Returns:
            The OperationType of the expression
        """
        expr_lower = expression.lower()
        
        if any(func in expr_lower for func in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']):
            return OperationType.TRIGONOMETRIC
        elif any(func in expr_lower for func in ['log', 'ln']):
            return OperationType.LOGARITHMIC
        elif any(func in expr_lower for func in ['sinh', 'cosh', 'tanh']):
            return OperationType.HYPERBOLIC
        elif any(op in expr_lower for op in ['**', '^']):
            return OperationType.POWER
        elif any(func in expr_lower for func in ['sum', 'avg', 'min', 'max']):
            return OperationType.STATISTICAL
        else:
            return OperationType.ARITHMETIC
