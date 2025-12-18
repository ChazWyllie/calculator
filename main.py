"""Entry point for the Advanced Calculator application."""

import sys
from src.calculator import Calculator
from src.ui import interactive_mode


def main():
    """Main entry point of the calculator application."""
    
    # Check for command-line arguments
    if len(sys.argv) > 1:
        # Command-line mode
        expression = ' '.join(sys.argv[1:])
        calculator = Calculator(verbose=False)
        result = calculator.calculate(expression)
        formatted = calculator.format_result(result)
        print(f"Input: {expression}")
        print(f"Result: {formatted}")
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()