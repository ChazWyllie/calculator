# Advanced Calculator

A comprehensive, modular mathematical calculator written in Python with support for various mathematical functions, constants, and operations.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division, modulo
- **Power Operations**: Exponentiation with `**` or `^` notation
- **Trigonometric Functions**: sin, cos, tan, asin, acos, atan
- **Hyperbolic Functions**: sinh, cosh, tanh
- **Logarithmic Functions**: log, log10, ln
- **Mathematical Constants**: pi, e, phi (golden ratio), tau
- **Utility Functions**: sqrt, abs, floor, ceil, round, factorial, degrees, radians
- **Implicit Multiplication**: Automatically handles expressions like `2pi`
- **Calculation History**: Track and view previous calculations
- **Batch Processing**: Calculate multiple expressions at once
- **Expression Validation**: Comprehensive error checking and reporting
- **Interactive and CLI Modes**: Use interactively or from command line

## Project Structure

```
calculator/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── calculator.py         # Core calculator logic
│   ├── enums.py             # Enumerations
│   └── ui.py                # User interface components
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests
├── docs/                     # Documentation
├── main.py                   # Entry point
├── setup.py                  # Package setup
├── requirements.txt          # Dependencies
├── pytest.ini               # Pytest configuration
├── .flake8                  # Flake8 configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/calculator.git
cd calculator

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt
```

### Using pip

```bash
pip install advanced-calculator
```

## Usage

### Graphical User Interface (GUI) - Recommended ⭐

#### Web GUI (Browser-based, Works Everywhere!)

The recommended way to use the calculator. Works in any browser on any platform.

```bash
# Install Flask (first time only)
pip install flask

# Run the web GUI
python main.py web
```

Then open your browser to **http://localhost:5000**

**Features:**
- Beautiful, modern interface
- Responsive design (works on mobile/tablet)
- Tabbed interface: Basic, Functions, Constants, History
- Keyboard shortcuts:
  - Enter: Calculate
  - Escape: Clear input
  - Backspace: Delete last character
- All mathematical functions and constants available
- Calculation history with color-coded results

#### Desktop GUI - Tkinter (Built-in)

```bash
python main.py gui
# or
python gui.py
```

**Features:**
- Tabbed interface with multiple tabs
- Color-coded displays
- Calculation history
- Keyboard shortcuts
- No additional dependencies needed*

*Note: On some systems (like Apple Silicon Macs), tkinter may need to be installed separately.

#### Desktop GUI - PyQt5 (Modern, Polished)

```bash
# Install PyQt5 (first time only)
pip install PyQt5

# Run the GUI
python main.py pyqt5
```

**Features:**
- Modern, professional styling
- Color-themed buttons and displays
- Responsive interface
- Beautiful animations
- Best performance on modern systems

### Interactive Menu Mode

```bash
python main.py
```

A terminal-based interactive menu where you can:
1. Calculate expressions
2. View calculation history
3. Clear history
4. Show supported functions
5. Show supported constants
6. Perform batch calculations

### Command-Line Mode

```bash
python main.py "2 + 3 * 4"
python main.py "sqrt(16)"
python main.py "sin(pi/2)"
python main.py "2**10 + 5"
```

### Python API

```python
from src.calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Simple calculation
result = calc.calculate("2 + 3 * 4")
print(result)  # Output: 14.0

# With formatting
formatted = Calculator.format_result(result)
print(formatted)  # Output: 14

# Batch calculations
expressions = ["2+2", "sqrt(16)", "pi"]
results = calc.calculate_batch(expressions)
print(results)  # Output: [4.0, 4.0, 3.141592653589793]

# View history
history = calc.get_history()
for expr, result in history:
    print(f"{expr} = {result}")

# Get operation type
from src.enums import OperationType
op_type = Calculator.get_operation_type("sin(x)")
print(op_type)  # Output: OperationType.TRIGONOMETRIC
```

## Supported Functions

### Trigonometric
- `sin(x)` - Sine
- `cos(x)` - Cosine
- `tan(x)` - Tangent
- `asin(x)` - Arc sine
- `acos(x)` - Arc cosine
- `atan(x)` - Arc tangent

### Hyperbolic
- `sinh(x)` - Hyperbolic sine
- `cosh(x)` - Hyperbolic cosine
- `tanh(x)` - Hyperbolic tangent

### Logarithmic
- `log(x)` - Base 10 logarithm
- `log10(x)` - Base 10 logarithm
- `ln(x)` - Natural logarithm
- `exp(x)` - Exponential function

### Utility
- `sqrt(x)` - Square root
- `abs(x)` - Absolute value
- `floor(x)` - Floor function
- `ceil(x)` - Ceiling function
- `round(x)` - Rounding
- `degrees(x)` - Radians to degrees
- `radians(x)` - Degrees to radians
- `factorial(x)` - Factorial

## Supported Constants

- `pi` - π (3.14159...)
- `e` - Euler's number (2.71828...)
- `phi` - Golden ratio (1.61803...)
- `tau` - τ = 2π (6.28318...)

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_calculator.py

# Run specific test
pytest tests/test_calculator.py::TestCalculator::test_basic_arithmetic
```

## Code Quality

### Linting

```bash
# Check code style
flake8 src/ tests/

# Format code
black src/ tests/
```

### Type Checking

```bash
# Check type hints
mypy src/
```

## Examples

### Basic Arithmetic

```python
calc.calculate("2 + 3")           # 5.0
calc.calculate("10 - 4")          # 6.0
calc.calculate("3 * 4")           # 12.0
calc.calculate("20 / 4")          # 5.0
calc.calculate("10 % 3")          # 1.0
```

### Power Operations

```python
calc.calculate("2 ** 3")          # 8.0
calc.calculate("2 ^ 10")          # 1024.0
```

### Trigonometric

```python
calc.calculate("sin(0)")          # 0.0
calc.calculate("cos(0)")          # 1.0
calc.calculate("sin(pi/2)")       # 1.0
```

### Complex Expressions

```python
calc.calculate("2 + 3 * 4")       # 14.0
calc.calculate("(2 + 3) * 4")     # 20.0
calc.calculate("sqrt(16) + 2*pi") # 10.283...
calc.calculate("log(100) + ln(e)") # 3.0
```

### Implicit Multiplication

```python
calc.calculate("2pi")             # 6.283...
calc.calculate("3(2+1)")          # 9.0
calc.calculate("2sqrt(16)")       # 8.0
```

## Error Handling

The calculator provides comprehensive error handling:

```python
calc.calculate("1/0")              # "Error: Division by zero."
calc.calculate("")                 # "Error: Empty expression provided."
calc.calculate("(2+3")             # "Error: Unbalanced parentheses."
calc.calculate("2 @ 3")            # "Error: Invalid characters in expression."
calc.calculate("sqrt(-1)")         # "Error: ValueError - ..."
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

## Acknowledgments

- Built with Python's `math` module
- Inspired by scientific calculators
- Uses `unittest` and `pytest` for testing
