#!/usr/bin/env python3
"""
INTERACTIVE CODE EXPLORER

This script helps you understand the calculator codebase interactively.
Run it and follow the prompts to explore different parts of the code.
"""

import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from src.calculator import Calculator
from src.enums import OperationType


def print_header(title):
    """Print a formatted header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def print_section(title):
    """Print a section header."""
    print(f"\n{'─'*70}")
    print(f"  {title}")
    print(f"{'─'*70}\n")


def explore_constants():
    """Explore mathematical constants."""
    print_section("EXPLORING MATHEMATICAL CONSTANTS")
    
    calc = Calculator()
    
    print("Available constants in the calculator:\n")
    for name, value in sorted(Calculator.CONSTANTS.items()):
        print(f"  {name:10s} = {value:.15f}")
    
    print("\n📝 Questions to think about:")
    print("  1. How many constants are there?")
    print("  2. Which one has the most decimal places?")
    print("  3. What would phi be used for?")
    print("  4. Try: python -c \"from src.calculator import Calculator; c = Calculator(); print(c.calculate('phi**2 - phi - 1'))\"")


def explore_functions():
    """Explore supported functions."""
    print_section("EXPLORING MATHEMATICAL FUNCTIONS")
    
    print("Available functions in the calculator:\n")
    
    functions = sorted(Calculator.FUNCTIONS.keys())
    
    # Group by category
    categories = {
        'Trigonometric': ['sin', 'cos', 'tan', 'asin', 'acos', 'atan'],
        'Hyperbolic': ['sinh', 'cosh', 'tanh'],
        'Logarithmic': ['log', 'log10', 'ln', 'exp'],
        'Utility': ['sqrt', 'abs', 'floor', 'ceil', 'round', 'factorial', 'degrees', 'radians'],
    }
    
    for category, funcs in categories.items():
        print(f"  {category}:")
        for func in funcs:
            if func in functions:
                print(f"    • {func}")
    
    print("\n📝 Questions to think about:")
    print("  1. How many functions are there in total?")
    print("  2. Which functions do you use most?")
    print("  3. What would YOU want to add?")


def trace_calculation(expression):
    """Trace through a calculation step by step."""
    print_section(f"TRACING CALCULATION: {expression}")
    
    calc = Calculator(verbose=True)
    
    print(f"Input: {expression}\n")
    print("Step 1: Validating expression...")
    is_valid, error = calc.validate_expression(expression)
    print(f"  Valid: {is_valid}")
    if not is_valid:
        print(f"  Error: {error}")
        return
    
    print("\nStep 2: Preprocessing expression...")
    processed = calc.preprocess_expression(expression)
    print(f"  Original: {expression}")
    print(f"  Processed: {processed}")
    
    print("\nStep 3: Calculating...")
    result = calc.calculate(expression)
    print(f"  Result: {result}")
    
    print("\nStep 4: History")
    history = calc.get_history()
    print(f"  Stored in history: {history[-1]}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print_section("TESTING EDGE CASES")
    
    calc = Calculator()
    
    test_cases = [
        ("1/0", "Division by zero"),
        ("", "Empty expression"),
        ("(2+3", "Unbalanced parentheses"),
        ("2 @ 3", "Invalid character"),
        ("sqrt(-1)", "Square root of negative"),
        ("2pi", "Implicit multiplication"),
        ("sin(pi/2)", "Trigonometric"),
        ("log(100)", "Logarithmic"),
        ("2**10", "Power operation"),
    ]
    
    print("Testing various expressions:\n")
    for expr, description in test_cases:
        result = calc.calculate(expr)
        status = "✓" if not isinstance(result, str) or "Error" not in result else "✗"
        result_str = str(result)[:40]
        print(f"  {status} {expr:20s} ({description:25s}) → {result_str}")


def understand_validation():
    """Understand validation logic."""
    print_section("UNDERSTANDING VALIDATION")
    
    calc = Calculator()
    
    test_inputs = [
        "2 + 3",
        "",
        "(2+3",
        "2 @ 3",
        "valid_expr",
    ]
    
    print("How validation works:\n")
    for inp in test_inputs:
        is_valid, error = calc.validate_expression(inp)
        status = "VALID ✓" if is_valid else "INVALID ✗"
        print(f"  Input: '{inp}'")
        print(f"    Status: {status}")
        if error:
            print(f"    Error: {error}")
        print()


def understand_preprocessing():
    """Understand preprocessing logic."""
    print_section("UNDERSTANDING PREPROCESSING")
    
    calc = Calculator()
    
    examples = [
        "2pi",
        "sin(pi/2)",
        "2^3",
        "3(2+1)",
        "2sin(x)",
    ]
    
    print("How preprocessing transforms input:\n")
    for expr in examples:
        processed = calc.preprocess_expression(expr)
        print(f"  Original:   {expr:20s}")
        print(f"  Processed:  {processed}")
        print()


def interactive_calculator():
    """Interactive calculator mode for learning."""
    print_section("INTERACTIVE LEARNING MODE")
    
    calc = Calculator()
    
    print("Enter mathematical expressions to calculate.")
    print("Type 'help' for examples, 'quit' to exit.\n")
    
    while True:
        try:
            expr = input(">>> ").strip()
            
            if expr.lower() == 'quit':
                break
            
            if expr.lower() == 'help':
                print("\nExamples:")
                print("  2 + 3 * 4")
                print("  sqrt(16)")
                print("  sin(pi/2)")
                print("  2**10")
                print("  log(100)")
                print()
                continue
            
            if not expr:
                continue
            
            result = calc.calculate(expr)
            formatted = calc.format_result(result)
            print(f"Result: {formatted}\n")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


def show_menu():
    """Show interactive menu."""
    print_header("CODE EXPLORER - LEARN BY DOING")
    
    print("Choose what you want to explore:\n")
    print("  1. Constants ..................... Explore mathematical constants")
    print("  2. Functions ..................... Explore available functions")
    print("  3. Validation .................... Understand input validation")
    print("  4. Preprocessing ................. See how input is transformed")
    print("  5. Trace Calculation ............. Step through a calculation")
    print("  6. Edge Cases .................... Test error handling")
    print("  7. Interactive Mode .............. Calculate & learn")
    print("  8. All Topics .................... Run through everything")
    print("  0. Exit")
    print()


def main():
    """Main menu."""
    while True:
        show_menu()
        
        choice = input("Select option (0-8): ").strip()
        
        if choice == "0":
            print("\nGoodbye! Happy learning! 🚀\n")
            break
        
        elif choice == "1":
            explore_constants()
        
        elif choice == "2":
            explore_functions()
        
        elif choice == "3":
            understand_validation()
        
        elif choice == "4":
            understand_preprocessing()
        
        elif choice == "5":
            expr = input("\nEnter expression to trace: ").strip()
            if expr:
                trace_calculation(expr)
        
        elif choice == "6":
            test_edge_cases()
        
        elif choice == "7":
            interactive_calculator()
        
        elif choice == "8":
            explore_constants()
            explore_functions()
            understand_validation()
            understand_preprocessing()
            test_edge_cases()
            print_header("LEARNING TOUR COMPLETE!")
            print("You've explored:")
            print("  ✓ Constants")
            print("  ✓ Functions")
            print("  ✓ Validation")
            print("  ✓ Preprocessing")
            print("  ✓ Edge Cases")
            print("\nNext step: Read DEVELOPER_GUIDE.md for deep dives!\n")
        
        else:
            print("Invalid option. Please try again.\n")
        
        if choice in ["1", "2", "3", "4", "5", "6"]:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nLearning session interrupted. Goodbye! 🚀\n")
        sys.exit(0)
