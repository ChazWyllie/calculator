# 📁 Project Structure and File Organization

## Overview

This document explains the organization of the calculator project, the purpose of each folder, and the role of each file.

---

## 🗂️ Complete Directory Structure

```
calculator/
│
├── 📋 ROOT LEVEL FILES (Project Configuration)
│   ├── main.py                    ← Entry point to run the calculator
│   ├── README.md                  ← Project overview and features
│   ├── LICENSE                    ← MIT License
│   ├── .gitignore                 ← Git ignore patterns
│   ├── .git/                      ← Git repository files
│   └── .github/                   ← GitHub configuration
│       └── workflows/
│           └── tests.yml          ← CI/CD pipeline
│
├── 📂 src/                        ← CORE APPLICATION CODE
│   ├── __init__.py               ← Package initialization
│   ├── calculator.py             ← Core calculator logic ⭐ MOST IMPORTANT
│   ├── enums.py                  ← Operation type enumerations
│   ├── ui.py                     ← Terminal/CLI interface
│   ├── gui_web.py                ← Flask web GUI (~600 lines)
│   ├── gui_tkinter.py            ← Tkinter desktop GUI (~400 lines)
│   ├── gui_pyqt5.py              ← PyQt5 modern GUI (~500 lines)
│   └── __pycache__/              ← Python compiled cache
│
├── 🧪 tests/                      ← UNIT TESTS
│   ├── __init__.py
│   ├── test_calculator.py        ← 20 comprehensive unit tests ✅
│   └── __pycache__/
│
├── 📚 docs/                       ← DOCUMENTATION (Organized by type)
│   │
│   ├── guides/                    ← Technical guides and reference
│   │   ├── DEVELOPER_GUIDE.md    ← Deep dive into architecture & patterns
│   │   ├── GUI_IMPLEMENTATION.md ← Comparison of 3 GUI implementations
│   │   └── SETUP.md              ← Installation and setup instructions
│   │
│   └── learning/                 ← Learning materials for new developers
│       ├── LEARNING_PATH.md      ← 10-part structured curriculum
│       ├── LEARNING_RESOURCES.md ← Navigation guide for all materials
│       └── QUICK_REFERENCE.md    ← Quick reference card (cheat sheet)
│
├── ⚙️  config/                     ← CONFIGURATION FILES
│   ├── setup.py                  ← Package setup and metadata
│   ├── requirements.txt          ← Python dependencies
│   ├── pytest.ini                ← Pytest configuration
│   ├── Makefile                  ← Common development commands
│   └── .flake8                   ← Code style rules
│
├── 🔧 scripts/                    ← UTILITY SCRIPTS
│   ├── gui.py                    ← GUI launcher (select which GUI to run)
│   ├── explore.py                ← Interactive code explorer (~300 lines)
│   └── quickstart.sh             ← Quick start shell script
│
├── 📖 examples/                   ← EXAMPLE USAGE FILES
│   ├── 01_basic_arithmetic.py   ← Basic arithmetic operations
│   ├── 02_trigonometric.py      ← Trigonometric functions
│   ├── 03_constants.py          ← Using mathematical constants
│   └── 04_batch_processing.py   ← Batch calculations
│
└── 🔒 venv/                       ← Virtual environment (dependencies)

```

---

## 📂 Folder-by-Folder Breakdown

### 1. ROOT LEVEL FILES

**Purpose:** Project-level configuration and entry point

| File | Purpose |
|------|---------|
| `main.py` | **Entry point** - Run calculator with menu, expression, or GUI |
| `README.md` | Complete project documentation with usage examples |
| `LICENSE` | MIT License for open source sharing |
| `.gitignore` | Tells Git which files to ignore (venv, __pycache__, etc.) |
| `.github/workflows/tests.yml` | GitHub Actions CI/CD pipeline |

**How to use:**
```bash
python main.py                # Interactive menu
python main.py "2 + 3"        # Calculate expression
python main.py web            # Launch web GUI
```

---

### 2. src/ - CORE APPLICATION CODE

**Purpose:** All application logic lives here

| File | Lines | Purpose |
|------|-------|---------|
| `calculator.py` | 265 | ⭐ **CORE** - Validation → Preprocess → Evaluate pipeline |
| `enums.py` | 25 | Operation type enumeration (ARITHMETIC, TRIGONOMETRIC, etc.) |
| `ui.py` | 90 | Terminal interface with menu and REPL |
| `gui_web.py` | 600 | Flask web-based GUI with HTML/CSS/JS |
| `gui_tkinter.py` | 400 | Tkinter desktop GUI (works on all OSes) |
| `gui_pyqt5.py` | 500 | Modern PyQt5 desktop GUI |

**The Pipeline (in calculator.py):**
```
User Input → Validate → Preprocess → Evaluate → Store History → Return Result
```

**Key Classes/Functions:**
- `Calculator` class - Main calculator with all methods
- `calculate()` - Core calculation method
- `validate_expression()` - Input validation
- `preprocess_expression()` - Transform user input
- `CONSTANTS` dict - Built-in constants (π, e, φ, τ)
- `FUNCTIONS` dict - Available functions (sin, cos, sqrt, etc.)

---

### 3. tests/ - UNIT TESTS

**Purpose:** Verify all functionality works correctly

| File | Tests | Coverage |
|------|-------|----------|
| `test_calculator.py` | 20 | All operations, edge cases, error handling |

**Test Categories:**
- ✅ Basic arithmetic (addition, subtraction, etc.)
- ✅ Power operations and exponentiation
- ✅ Trigonometric functions
- ✅ Logarithmic functions
- ✅ Constants and implicit multiplication
- ✅ Error handling (division by zero, invalid syntax)
- ✅ History tracking

**Run tests:**
```bash
pytest tests/                 # Run all tests
pytest tests/ -v              # Verbose output with details
pytest tests/ --cov=src       # Show code coverage
```

---

### 4. docs/ - DOCUMENTATION (2 subdirectories)

#### docs/guides/ - Technical Reference

| File | Purpose | Read Time |
|------|---------|-----------|
| `DEVELOPER_GUIDE.md` | Deep dive into architecture, patterns, data flow diagrams | 1-2 hours |
| `GUI_IMPLEMENTATION.md` | Comparison of 3 GUI options with pros/cons | 30 min |
| `SETUP.md` | Installation, troubleshooting, dev workflow | 30 min |

#### docs/learning/ - Learning Materials

| File | Purpose | Read Time |
|------|---------|-----------|
| `LEARNING_PATH.md` | 10-part structured curriculum with exercises | 6-10 hours |
| `LEARNING_RESOURCES.md` | Navigation guide for all materials, learning paths | 30 min |
| `QUICK_REFERENCE.md` | Quick reference card, cheat sheet | 5-10 min |

---

### 5. config/ - CONFIGURATION FILES

**Purpose:** Project configuration and development settings

| File | Purpose |
|------|---------|
| `setup.py` | Package metadata (name, version, dependencies) |
| `requirements.txt` | Python packages to install (Flask, pytest, etc.) |
| `pytest.ini` | Pytest configuration (test discovery, markers) |
| `Makefile` | Common commands (make test, make lint, make format) |
| `.flake8` | Code style rules (line length, ignored rules) |

**Common commands:**
```bash
make test                     # Run all tests
make lint                     # Check code style
make format                   # Auto-format code
make install                  # Install dependencies
```

---

### 6. scripts/ - UTILITY SCRIPTS

**Purpose:** Helper scripts for running the application

| File | Purpose | Lines |
|------|---------|-------|
| `gui.py` | GUI launcher - choose which GUI to run | 80 |
| `explore.py` | Interactive code explorer for learning | 300+ |
| `quickstart.sh` | Quick setup script | 30 |

**Usage:**
```bash
python scripts/gui.py         # Launch GUI selector
python scripts/explore.py     # Interactive code explorer
bash scripts/quickstart.sh    # Quick setup
```

---

### 7. examples/ - EXAMPLE USAGE

**Purpose:** Practical examples showing how to use the calculator

| File | Topic | Examples |
|------|-------|----------|
| `01_basic_arithmetic.py` | Basic math | Addition, subtraction, order of operations |
| `02_trigonometric.py` | Advanced functions | sin, cos, tan, log, exp, etc. |
| `03_constants.py` | Mathematical constants | π, e, φ, τ usage |
| `04_batch_processing.py` | Multiple calculations | Temperature conversion, physics, finance |

**Run an example:**
```bash
python examples/01_basic_arithmetic.py
python examples/02_trigonometric.py
python examples/03_constants.py
python examples/04_batch_processing.py
```

---

### 8. venv/ - VIRTUAL ENVIRONMENT

**Purpose:** Isolated Python environment with dependencies

**Contains:**
- Python interpreter
- Installed packages (Flask, pytest, etc.)
- Package metadata

**Setup:**
```bash
python3 -m venv venv          # Create virtual environment
source venv/bin/activate      # Activate on macOS/Linux
venv\Scripts\activate         # Activate on Windows
pip install -r config/requirements.txt
```

---

## 🎯 File Organization by Purpose

### "I want to..."

#### ...UNDERSTAND THE CODE
1. Read `README.md` (overview)
2. Read `docs/guides/DEVELOPER_GUIDE.md` (architecture)
3. Read `src/calculator.py` (core logic)
4. Study `tests/test_calculator.py` (usage patterns)

#### ...LEARN STEP-BY-STEP
1. Start with `docs/learning/QUICK_REFERENCE.md`
2. Follow `docs/learning/LEARNING_PATH.md`
3. Use `docs/learning/LEARNING_RESOURCES.md` for navigation
4. Run `scripts/explore.py` for interactive learning

#### ...RUN THE CALCULATOR
1. Interactive: `python main.py`
2. Calculate: `python main.py "2 + 3"`
3. GUI: `python main.py web` or `python scripts/gui.py`
4. Examples: `python examples/01_basic_arithmetic.py`

#### ...MODIFY THE CODE
1. Edit files in `src/` (core logic)
2. Edit `tests/` to write new tests
3. Run `pytest tests/` to verify
4. Use `make lint` and `make format`

#### ...DEPLOY/SHARE PROJECT
1. Follow `docs/guides/SETUP.md`
2. Use `config/setup.py` for PyPI
3. Check `.github/workflows/tests.yml` for CI/CD

---

## 📊 Code Distribution

```
Total Project Size: ~5,000+ lines

src/                    1,500 lines (30%)  - Core application
docs/                   1,000 lines (20%)  - Documentation  
examples/               500 lines (10%)    - Usage examples
tests/                  200 lines (4%)     - Unit tests
config/                 150 lines (3%)     - Configuration
scripts/                400 lines (8%)     - Utility scripts
.github/                 50 lines (1%)     - CI/CD
Other files             200 lines (4%)     - Misc
venv/                   [virtual env]      - Dependencies
```

---

## 🔄 Data Flow

```
User Input
    ↓
main.py (entry point)
    ↓
    ├→ Interactive Menu (ui.py)
    ├→ Direct Expression (calculator.py)
    └→ GUI (gui_web.py, gui_tkinter.py, or gui_pyqt5.py)
        ↓
    calculator.py (core pipeline)
        ├→ validate_expression()
        ├→ preprocess_expression()
        ├→ calculate()
        └→ store in history
        ↓
    Result returned to user
    ↓
    Display (UI, web, desktop)
```

---

## 🎓 Learning Progression

1. **Week 1: Foundations**
   - Read README.md
   - Run examples/01_basic_arithmetic.py
   - Read QUICK_REFERENCE.md

2. **Week 2: Architecture**
   - Read DEVELOPER_GUIDE.md
   - Study src/calculator.py
   - Follow LEARNING_PATH.md

3. **Week 3: Hands-On**
   - Run tests with pytest
   - Modify an example
   - Add a new feature

4. **Week 4: Mastery**
   - Teach others
   - Deploy the project
   - Create something similar

---

## 📌 Key Files to Know

| Priority | File | Why |
|----------|------|-----|
| ⭐⭐⭐ | src/calculator.py | Core logic - understand this first |
| ⭐⭐⭐ | README.md | Project overview |
| ⭐⭐⭐ | tests/test_calculator.py | See how code is used |
| ⭐⭐ | docs/guides/DEVELOPER_GUIDE.md | Architecture & patterns |
| ⭐⭐ | docs/learning/LEARNING_PATH.md | Structured curriculum |
| ⭐ | examples/ | Practical usage |
| ⭐ | main.py | Entry point |

---

## 🚀 Quick Start

```bash
# 1. Navigate to project
cd /Users/chazwyllie/Git/calculator

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run example
python examples/01_basic_arithmetic.py

# 4. Run tests
pytest tests/

# 5. Launch GUI
python main.py web

# 6. Interactive explorer
python scripts/explore.py
```

---

**Now you understand the organization! Start with README.md or QUICK_REFERENCE.md** 📚

