"""User interface components for the calculator."""

from typing import List, Tuple, Union

from .calculator import Calculator


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
    """
    Display calculation history.
    
    Args:
        calculator: The calculator instance with history to display
    """
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
