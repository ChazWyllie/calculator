# Setup Guide

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/calculator.git
cd calculator
```

#### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
# Install development dependencies (recommended)
pip install -r requirements.txt

# Or install the package in development mode
pip install -e ".[dev]"
```

#### 4. Verify Installation
```bash
python main.py  # Should show interactive menu
```

## Common Commands

### Running the Calculator

**Interactive mode:**
```bash
python main.py
```

**Command-line mode:**
```bash
python main.py "2 + 3 * 4"
python main.py "sqrt(16)"
python main.py "sin(pi/2)"
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_calculator.py::TestCalculator::test_basic_arithmetic -v

# Run with coverage report
python -m pytest --cov=src tests/
```

### Code Quality

```bash
# Run linting
flake8 src/ tests/

# Format code with black
black src/ tests/ main.py

# Run type checking
mypy src/
```

### Using Make Commands

If you have `make` installed (usually pre-installed on macOS/Linux):

```bash
make dev-install    # Install with dev dependencies
make run            # Run the calculator
make test           # Run tests
make coverage       # Run tests with coverage
make lint           # Run linting
make format         # Format code
make type-check     # Run type checking
make clean          # Clean build artifacts
make all            # Run all checks
```

## Project Structure

```
calculator/
├── src/                    # Main source code
│   ├── __init__.py
│   ├── calculator.py       # Core calculator class
│   ├── enums.py           # Enumerations
│   └── ui.py              # User interface
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_calculator.py  # Unit tests
├── docs/                   # Documentation
├── main.py                 # Entry point
├── setup.py                # Package configuration
├── requirements.txt        # Dependencies
├── pytest.ini             # Test configuration
├── .flake8                # Linting rules
├── Makefile               # Common commands
└── README.md              # Documentation
```

## Troubleshooting

### Module Not Found Error
If you get `ModuleNotFoundError: No module named 'src'`:
1. Make sure you're running from the project root directory
2. Ensure your virtual environment is activated
3. Try: `pip install -e .`

### pytest Not Found
```bash
# Install pytest
pip install pytest pytest-cov
```

### Python Version Issues
Check your Python version:
```bash
python --version
```
Must be 3.8 or higher. If needed, create venv with specific version:
```bash
python3.11 -m venv venv
```

### Permission Errors
If you get permission errors:
```bash
# Remove and recreate venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Development Workflow

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `pytest tests/`
4. Format code: `black src/ tests/`
5. Check linting: `flake8 src/ tests/`
6. Commit changes: `git commit -m "Add your message"`
7. Push to branch: `git push origin feature/your-feature`
8. Open a Pull Request

## Next Steps

- Read the [README.md](README.md) for full documentation
- Check `main.py` to understand the entry point
- Explore `src/calculator.py` to see the core implementation
- Review `tests/test_calculator.py` for test examples
