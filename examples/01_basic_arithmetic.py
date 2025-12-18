"""
Example 1: Basic Arithmetic Operations

Learn how to use the calculator for simple math operations.
"""

import sys
from pathlib import Path

# Add src to path so we can import calculator
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calculator import Calculator

def main():
    """Run basic arithmetic examples."""
    calc = Calculator()
    
    print("=" * 50)
    print("EXAMPLE 1: Basic Arithmetic Operations")
    print("=" * 50)
    print()
    
    # Example 1: Addition
    print("1. Addition")
    result = calc.calculate("2 + 3")
    print(f"   Expression: 2 + 3")
    print(f"   Result: {result}")
    print()
    
    # Example 2: Subtraction
    print("2. Subtraction")
    result = calc.calculate("10 - 4")
    print(f"   Expression: 10 - 4")
    print(f"   Result: {result}")
    print()
    
    # Example 3: Multiplication
    print("3. Multiplication")
    result = calc.calculate("5 * 6")
    print(f"   Expression: 5 * 6")
    print(f"   Result: {result}")
    print()
    
    # Example 4: Division
    print("4. Division")
    result = calc.calculate("20 / 4")
    print(f"   Expression: 20 / 4")
    print(f"   Result: {result}")
    print()
    
    # Example 5: Power (Exponentiation)
    print("5. Power (Exponentiation)")
    result = calc.calculate("2 ** 8")
    print(f"   Expression: 2 ** 8")
    print(f"   Result: {result}")
    print()
    
    # Example 6: Order of Operations (PEMDAS)
    print("6. Order of Operations (PEMDAS)")
    result = calc.calculate("2 + 3 * 4")
    print(f"   Expression: 2 + 3 * 4")
    print(f"   Result: {result}")
    print(f"   Note: Multiplication happens before addition")
    print()
    
    # Example 7: Parentheses
    print("7. Parentheses (Grouping)")
    result = calc.calculate("(2 + 3) * 4")
    print(f"   Expression: (2 + 3) * 4")
    print(f"   Result: {result}")
    print(f"   Note: Parentheses change the order")
    print()
    
    # Example 8: Negative Numbers
    print("8. Negative Numbers")
    result = calc.calculate("-5 + 3")
    print(f"   Expression: -5 + 3")
    print(f"   Result: {result}")
    print()
    
    # Example 9: Decimal Numbers
    print("9. Decimal Numbers")
    result = calc.calculate("3.5 + 2.7")
    print(f"   Expression: 3.5 + 2.7")
    print(f"   Result: {result}")
    print()
    
    # Example 10: Complex Expression
    print("10. Complex Expression")
    result = calc.calculate("((10 + 5) * 2 - 3) / 3")
    print(f"   Expression: ((10 + 5) * 2 - 3) / 3")
    print(f"   Result: {result}")
    print()
    
    print("=" * 50)
    print("View the history of calculations:")
    print("=" * 50)
    for i, (expr, res) in enumerate(calc.history, 1):
        print(f"{i}. {expr} = {res}")

if __name__ == "__main__":
    main()
