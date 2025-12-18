import math
import re
from typing import Union, List, Tuple
from enum import Enum
from decimal import Decimal, getcontext


# Set decimal precision for accurate calculations
getcontext().prec = 50


class OperationType(Enum):
    """Enumeration for different types of operations supported by the calculator."""
    ARITHMETIC = "arithmetic"
    TRIGONOMETRIC = "trigonometric"
    LOGARITHMIC = "logarithmic"
    POWER = "power"
    STATISTICAL = "statistical"


class Calculator:
    """
    A comprehensive calculator class that supports various mathematical operations.
    
    Supported operations:
    - Basic arithmetic: +, -, *, /, %
    - Power operations: **, ^
    - Trigonometric functions: sin, cos, tan, asin, acos, atan
    - Logarithmic functions: log, log10, ln
    - Statistical functions: sum, avg, min, max
    - Constants: pi, e
    """
    
    # Predefined constants
    CONSTANTS = {
        'pi': math.pi,
        'e': math.e,
        'phi': (1 + math.sqrt(5)) / 2,  # Golden ratio
        'tau': 2 * math.pi,
    }
    
    # Supported mathematical functions
    FUNCTIONS = {
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
        self.last_result = None
    
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
            safe_dict = {
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
    
    def format_result(self, result: Union[float, str], decimal_places: int = 2) -> str:
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


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("ADVANCED CALCULATOR")
    print("="*50)
    print("1. Calculate expression")
    print("2. View calculation history")
    print("3. Clear history")
    print("4. Show supported functions")
    print("5. Show supported constants")
    print("6. Batch calculations")
    print("0. Exit")
    print("="*50)


def show_supported_functions():
    """Display all supported functions."""
    print("\nSupported Functions:")
    print("-" * 40)
    functions_list = sorted(Calculator.FUNCTIONS.keys())
    for i, func in enumerate(functions_list, 1):
        print(f"{i:2d}. {func}")


def show_supported_constants():
    """Display all supported constants."""
    print("\nSupported Constants:")
    print("-" * 40)
    for const_name, const_value in sorted(Calculator.CONSTANTS.items()):
        print(f"{const_name}: {const_value:.10f}")


def display_history(calculator: Calculator):
    """Display calculation history."""
    history = calculator.get_history()
    if not history:
        print("\nNo calculation history.")
        return
    
    print("\nCalculation History:")
    print("-" * 50)
    for i, (expr, result) in enumerate(history, 1):
        result_str = calculator.format_result(result)
        print(f"{i:3d}. {expr:30s} = {result_str}")
    print("-" * 50)


def interactive_mode():
    """Run the calculator in interactive mode."""
    calculator = Calculator(verbose=False)
    
    print("\n" + "="*50)
    print("Welcome to Advanced Calculator!")
    print("="*50)
    print("\nExample expressions:")
    print("  2 + 3 * 4")
    print("  sqrt(16)")
    print("  sin(pi/2)")
    print("  2**10")
    print("  log(100)")
    
    while True:
        display_menu()
        choice = input("\nSelect an option (0-6): ").strip()
        
        if choice == '0':
            print("Thank you for using Advanced Calculator. Goodbye!")
            break
        
        elif choice == '1':
            expression = input("\nEnter expression: ").strip()
            if expression:
                result = calculator.calculate(expression)
                formatted = calculator.format_result(result)
                print(f"Result: {formatted}")
        
        elif choice == '2':
            display_history(calculator)
        
        elif choice == '3':
            calculator.clear_history()
            print("\nHistory cleared.")
        
        elif choice == '4':
            show_supported_functions()
        
        elif choice == '5':
            show_supported_constants()
        
        elif choice == '6':
            num_expressions = input("\nHow many expressions to calculate? ")
            try:
                count = int(num_expressions)
                expressions = []
                for i in range(count):
                    expr = input(f"Expression {i+1}: ").strip()
                    if expr:
                        expressions.append(expr)
                
                if expressions:
                    print("\nResults:")
                    print("-" * 50)
                    results = calculator.calculate_batch(expressions)
                    for expr, result in zip(expressions, results):
                        result_str = calculator.format_result(result)
                        print(f"{expr:30s} = {result_str}")
                    print("-" * 50)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        else:
            print("Invalid option. Please select 0-6.")


def main():
    """Main entry point of the calculator application."""
    import sys
    
    calculator = Calculator(verbose=False)
    
    # Check for command-line arguments
    if len(sys.argv) > 1:
        # Command-line mode
        expression = ' '.join(sys.argv[1:])
        result = calculator.calculate(expression)
        formatted = calculator.format_result(result)
        print(f"Input: {expression}")
        print(f"Result: {formatted}")
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()