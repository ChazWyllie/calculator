"""Entry point for the Advanced Calculator application."""

import sys
from src.calculator import Calculator
from src.ui import interactive_mode


def main():
    """Main entry point of the calculator application."""
    
    # Check for command-line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        # Web GUI mode (recommended)
        if arg in ["web", "--web", "-w"]:
            try:
                from src.gui_web import main as web_main
                web_main()
            except ImportError:
                print("Error: Flask not installed. Install with: pip install flask")
                sys.exit(1)
        
        # GUI mode (Tkinter)
        elif arg in ["gui", "--gui", "-g", "tkinter"]:
            try:
                from src.gui_tkinter import main as gui_main
                gui_main()
            except ImportError:
                print("Error: tkinter not available on this system")
                print("Try the web GUI instead: python main.py web")
                sys.exit(1)
        
        # GUI mode (PyQt5)
        elif arg in ["gui-pyqt5", "--gui-pyqt5", "-p", "pyqt5"]:
            try:
                from src.gui_pyqt5 import main as gui_pyqt5_main
                gui_pyqt5_main()
            except ImportError:
                print("Error: PyQt5 not installed. Install with: pip install PyQt5")
                sys.exit(1)
        
        # Help
        elif arg in ["help", "-h", "--help"]:
            print_help()
        
        # Calculator mode (regular expression)
        else:
            expression = ' '.join(sys.argv[1:])
            calculator = Calculator(verbose=False)
            result = calculator.calculate(expression)
            formatted = calculator.format_result(result)
            print(f"Input: {expression}")
            print(f"Result: {formatted}")
    else:
        # Interactive mode
        interactive_mode()


def print_help():
    """Print help message."""
    print("""
Advanced Calculator - Usage Guide
==================================

INTERACTIVE MODE:
  python main.py
  
COMMAND-LINE MODE:
  python main.py "2 + 3 * 4"
  python main.py "sqrt(16)"
  python main.py "sin(pi/2)"

WEB GUI (Browser-based, Recommended):
  python main.py web
  python main.py --web
  python gui.py web
  (Requires: pip install flask)

GUI MODE (Tkinter - built-in):
  python main.py gui
  python main.py tkinter
  python gui.py

GUI MODE (PyQt5 - modern):
  python main.py pyqt5
  python main.py gui-pyqt5
  python gui.py pyqt5
  (Requires: pip install PyQt5)

HELP:
  python main.py help
  python main.py --help
  python main.py -h

EXAMPLES:
  Basic arithmetic:
    python main.py "2 + 3"           # 5
    python main.py "10 - 4"          # 6
    python main.py "3 * 4"           # 12
    python main.py "20 / 4"          # 5
    
  Power operations:
    python main.py "2 ** 3"          # 8
    python main.py "2 ^ 10"          # 1024
    
  Trigonometric:
    python main.py "sin(0)"          # 0
    python main.py "cos(0)"          # 1
    python main.py "sin(pi/2)"       # 1
    
  Complex expressions:
    python main.py "2 + 3 * 4"       # 14
    python main.py "(2 + 3) * 4"     # 20
    python main.py "sqrt(16) + 2*pi" # ~10.28
    python main.py "log(100) + ln(e)"  # 3

For more information, see README.md
    """)


if __name__ == "__main__":
    main()