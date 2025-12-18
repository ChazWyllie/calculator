"""
DEVELOPER LEARNING PATH - Advanced Calculator Project

This guide is designed to help you understand the codebase from fundamental
concepts to advanced patterns. Work through each section sequentially.
"""

# ==============================================================================
# PART 1: PROJECT OVERVIEW & ARCHITECTURE (30 mins)
# ==============================================================================

"""
START HERE - Understanding the Big Picture

1. READ: README.md and GUI_IMPLEMENTATION.md
   - Why: Understand what this project does
   - Learn about: Features, structure, usage modes
   - Expected time: 10 minutes

2. EXPLORE: Project Structure
   - Open: /calculator root
   - Notice: Separation of concerns (src/, tests/, docs/)
   - Ask: "Why is code organized this way?"
   - Expected time: 5 minutes

3. READ: SETUP.md
   - Why: Learn how to actually RUN the project
   - Learn about: Virtual environments, dependencies, troubleshooting
   - Expected time: 10 minutes

4. RUN: The project in different modes
   - Command: python main.py
   - Command: python main.py "2 + 3 * 4"
   - Command: python main.py web (if Flask installed)
   - Expected time: 5 minutes

KEY LEARNING:
✓ This is a FULL PRODUCTION PROJECT with multiple interfaces
✓ It has tests, documentation, proper structure
✓ It separates concerns (core logic vs UI vs testing)
"""

# ==============================================================================
# PART 2: CORE LOGIC & ARCHITECTURE (1-2 hours)
# ==============================================================================

"""
UNDERSTANDING THE CALCULATOR ENGINE

1. READ: src/enums.py (5 minutes)
   ──────────────────────────────
   
   What to notice:
   - This file is TINY but important
   - It defines enumerations (OperationType)
   - WHY? Enums provide type safety and clarity
   
   Key Learning:
   → Enums are a way to define a fixed set of values
   → They make code more readable than magic strings
   → Python Enum usage pattern
   
   Questions to answer:
   Q1: What are the different operation types?
   Q2: Why not just use strings like "trigonometric"?
   Q3: Where is OperationType actually used?
"""

"""
2. READ: src/calculator.py (30-40 minutes)
   ─────────────────────────────────────────
   
   This is the CORE of the project. Read in sections:
   
   SECTION A: Class Definition & Constants (lines 1-60)
   ────────────────────────────────────────
   - Understand CONSTANTS dictionary
   - Understand FUNCTIONS dictionary
   - WHY are these class variables?
   - What does getcontext().prec = 50 do?
   
   Learning objectives:
   □ Understand class-level vs instance-level attributes
   □ Learn about decimal precision
   □ Know what functions are supported
   
   SECTION B: __init__ Method (lines 66-78)
   ──────────────────────────────────────────
   - This runs when you create a Calculator()
   - It initializes empty history
   - Last result tracking
   
   Learning objectives:
   □ Instance initialization pattern
   □ Why track calculation history?
   
   SECTION C: validate_expression (lines 80-105)
   ──────────────────────────────────────────────
   - FIRST step before calculating
   - Checks: empty? unbalanced parentheses? invalid chars?
   
   Learning objectives:
   □ Defensive programming (validate before processing)
   □ Error handling strategy
   □ Regular expression basics
   
   SECTION D: preprocess_expression (lines 107-135)
   ────────────────────────────────────────────────
   - Transforms user input into evaluable form
   - Replaces constants (pi → 3.14159...)
   - Handles implicit multiplication (2pi → 2*pi)
   
   Learning objectives:
   □ Input preprocessing pattern
   □ Regular expression substitution
   □ String manipulation techniques
   
   SECTION E: calculate (lines 137-190)
   ─────────────────────────────────────
   - MAIN LOGIC - this is the heart of the project
   - Validates → Preprocesses → Evaluates → Records
   
   Learning objectives:
   □ Error handling (try/except blocks)
   □ Safe evaluation with restricted dict
   □ Why use safe_dict instead of raw eval()?
   
   SECTION F: Helper Methods (lines 192-265)
   ──────────────────────────────────────────
   - calculate_batch: Process multiple expressions
   - get_history: Retrieve past calculations
   - format_result: Pretty-print results
   - get_operation_type: Classify the operation
   
   Learning objectives:
   □ Method composition and helper functions
   □ Don't repeat code - reuse common patterns
"""

"""
KEY INSIGHT FOR SECTION 2:
The Calculator class follows a PIPELINE PATTERN:
    User Input → Validate → Preprocess → Evaluate → Format → Return
    
This is how ROBUST software works!
"""

# ==============================================================================
# PART 3: USER INTERFACE LAYER (1-2 hours)
# ==============================================================================

"""
UNDERSTANDING HOW USERS INTERACT WITH CALCULATOR

1. READ: src/ui.py (20 minutes)
   ────────────────────────────
   
   This is the TERMINAL/CLI interface
   
   Notice:
   - It imports Calculator from .calculator
   - It builds interactive menus
   - It calls calculator.calculate()
   
   Learning objectives:
   □ How UI layer uses core logic
   □ Menu-driven interface pattern
   □ User input handling
   
   Questions:
   Q1: How does ui.py interact with calculator.py?
   Q2: What happens when user selects option 1?
   Q3: Why separate UI from calculation logic?

2. COMPARE: Three GUI implementations
   ──────────────────────────────────
   
   They all do the SAME THING but different ways:
   - src/gui_web.py (Flask) - HTML/JavaScript in browser
   - src/gui_tkinter.py (Tkinter) - Desktop GUI
   - src/gui_pyqt5.py (PyQt5) - Modern desktop GUI
   
   Key insight:
   ✓ All three import and use Calculator
   ✓ All three have similar button arrangements
   ✓ All three track history
   ✓ ONLY THE INTERFACE CHANGES, NOT THE LOGIC
   
   Learning objectives:
   □ Understand separation of UI from logic
   □ Learn different UI frameworks
   □ See how same logic works with different UIs
"""

# ==============================================================================
# PART 4: TESTING & QUALITY ASSURANCE (1 hour)
# ==============================================================================

"""
UNDERSTANDING HOW CODE IS TESTED

1. READ: tests/test_calculator.py (40 minutes)
   ───────────────────────────────────────────
   
   This file proves the calculator works correctly!
   
   SECTION A: TestCalculator class
   ────────────────────────────────
   - Tests basic functionality
   - Each test_ method is one test case
   - Follow pattern: Setup → Call function → Assert result
   
   SECTION B: TestCalculatorValidation class
   ──────────────────────────────────────────
   - Tests validation logic
   - Ensures bad inputs are caught
   
   Learning objectives:
   □ Unit testing fundamentals
   □ pytest conventions
   □ How to write testable code
   □ AAA Pattern (Arrange, Act, Assert)
   
   ACTIVITY: Run the tests
   ────────────────────────
   Command: source venv/bin/activate && pytest tests/ -v
   
   Notice:
   - ✓ means test passed
   - See all 20 tests pass
   - This proves calculator works!

2. UNDERSTAND: Test Coverage
   ──────────────────────────
   Not every line needs testing, but:
   ✓ Every public function should have a test
   ✓ Every error condition should have a test
   ✓ Complex logic should have multiple tests
   
   Learning objective:
   □ Why testing matters for code quality
"""

# ==============================================================================
# PART 5: PYTHON PATTERNS & BEST PRACTICES (1-2 hours)
# ==============================================================================

"""
SPECIFIC PYTHON CONCEPTS IN THIS PROJECT

1. TYPE HINTS (Throughout the code)
   ──────────────────────────────────
   Example: def calculate(self, expression: str) -> Union[float, str]:
   
   What it means:
   - expression parameter must be str
   - Returns either float or str
   
   Why?
   ✓ Helps catch bugs early
   ✓ Makes code self-documenting
   ✓ IDEs can provide better autocomplete
   
   Learning objective:
   □ Read and write type hints

2. DOCSTRINGS (Every class and function)
   ──────────────────────────────────────
   Example:
   '''
   Calculate the result of a mathematical expression.
   
   Args:
       expression: The mathematical expression to evaluate
       
   Returns:
       The result of the calculation or an error message
   '''
   
   Why?
   ✓ Users know what the function does
   ✓ Can generate documentation automatically
   ✓ Professional code standard
   
   Learning objective:
   □ Write clear docstrings

3. DICTIONARY COMPREHENSIONS (calculator.py)
   ──────────────────────────────────────────
   CONSTANTS and FUNCTIONS are dictionaries
   
   Usage pattern:
   safe_dict = {
       '__builtins__': {},
       **self.FUNCTIONS,
       **self.CONSTANTS,
   }
   
   Learning objective:
   □ Dictionary unpacking with **

4. REGULAR EXPRESSIONS (preprocess_expression)
   ──────────────────────────────────────────
   Example: re.sub(r'(\d)([a-z])', r'\1*\2', processed)
   
   What it does: Finds digit followed by letter, adds * between
   Why? Converts "2pi" to "2*pi"
   
   Learning objective:
   □ Basic regex patterns

5. TRY/EXCEPT ERROR HANDLING (calculate method)
   ──────────────────────────────────────────
   
   Pattern:
   try:
       # code that might fail
   except SpecificError:
       # handle specific case
   except Exception:
       # handle general case
   
   Learning objective:
   □ Graceful error handling

6. STATIC METHODS (@staticmethod)
   ──────────────────────────────
   Example: @staticmethod
           def format_result(...)
   
   When to use: When function doesn't need self
   Why? Clearer intent, can call without instance
   
   Learning objective:
   □ When and how to use static methods
"""

# ==============================================================================
# PART 6: PROJECT STRUCTURE & ORGANIZATION (30 mins)
# ==============================================================================

"""
WHY THE PROJECT IS ORGANIZED THIS WAY

1. src/ directory
   ─────────────
   - Contains all SOURCE CODE
   - Separated from tests, docs, config
   - When installed, this is what gets packaged
   
   WHY? Professional projects separate source from everything else

2. tests/ directory
   ────────────────
   - Contains all TEST CODE
   - Mirrors src/ structure
   - Separate from production code
   
   WHY? Tests shouldn't be deployed to users

3. docs/ directory
   ───────────────
   - Documentation files
   - Future Sphinx-generated API docs
   
4. Configuration files at root
   ──────────────────────────
   - setup.py: How to install the package
   - requirements.txt: What dependencies to install
   - pytest.ini: How to run tests
   - .flake8: Code style rules
   - Makefile: Common commands
   
5. GitHub specific
   ───────────────
   - .github/workflows/: Automated testing
   - .gitignore: What NOT to commit
   - LICENSE: Legal terms

LEARNING OBJECTIVE:
□ Understand why a professional project looks like this
□ Learn what each directory/file is for
"""

# ==============================================================================
# PART 7: HANDS-ON CODING EXERCISES (2-3 hours)
# ==============================================================================

"""
NOW THAT YOU'VE LEARNED THE STRUCTURE, TRY MODIFYING IT

EXERCISE 1: Add a New Mathematical Function
────────────────────────────────────────────
Goal: Add support for tangent hyperbolic (tanh) - it's already there!
Actually: Add a NEW function that isn't there

Steps:
1. Open src/calculator.py
2. Find the FUNCTIONS dictionary
3. Add a new function:
   'cbrt': lambda x: x ** (1/3),  # Cube root
4. Test it: python main.py "cbrt(8)"
5. Should output 2.0

WHAT YOU'LL LEARN:
✓ How to modify the calculator
✓ How changes propagate to all UIs automatically
✓ The power of modular design

EXERCISE 2: Add a New Constant
───────────────────────────────
Goal: Add a new mathematical constant

Steps:
1. Open src/calculator.py
2. Find the CONSTANTS dictionary
3. Add: 'g': 9.81,  # Gravitational acceleration
4. Test it: python main.py "1 + g"
5. Should output 10.81

WHAT YOU'LL LEARN:
✓ Even easier than adding functions
✓ How constants are used globally

EXERCISE 3: Write a Test
────────────────────────
Goal: Test your new function

Steps:
1. Open tests/test_calculator.py
2. Find a test method like test_basic_arithmetic
3. Copy it and create test_cbrt
4. Write: self.assertEqual(self.calc.calculate("cbrt(8)"), 2.0)
5. Run: pytest tests/test_calculator.py::TestCalculator::test_cbrt -v

WHAT YOU'LL LEARN:
✓ How to write tests
✓ TDD (Test-Driven Development)
✓ Confidence that code works

EXERCISE 4: Modify UI
─────────────────────
Goal: Add your new function to the web GUI

Steps:
1. Open src/gui_web.py
2. Find the Functions section in HTML
3. Add a new button:
   <button class="btn btn-function" onclick="addToInput('cbrt(')">cbrt</button>
4. Run: python main.py web
5. Use the new button!

WHAT YOU'LL LEARN:
✓ How UI modification works
✓ HTML/JavaScript basics
✓ How UIs and logic interact

EXERCISE 5: Add Error Validation
────────────────────────────────
Goal: Add validation for negative numbers in sqrt

Steps:
1. Open src/calculator.py
2. Find the calculate method
3. Add check before eval:
   if 'sqrt(-' in processed:
       return "Error: Cannot take sqrt of negative number"
4. Test: python main.py "sqrt(-1)"

WHAT YOU'LL LEARN:
✓ Input validation patterns
✓ User-friendly error messages
"""

# ==============================================================================
# PART 8: NEXT LEVEL - UNDERSTANDING PATTERNS (1-2 hours)
# ==============================================================================

"""
DESIGN PATTERNS USED IN THIS PROJECT

1. STRATEGY PATTERN (Multiple UIs)
   ───────────────────────────────
   All GUIs implement different strategies but use same Calculator
   
   BENEFIT: Can add new UI without changing core logic
   
2. PIPELINE PATTERN (Calculator logic)
   ──────────────────────────────────
   Input → Validate → Preprocess → Evaluate → Store → Return
   
   BENEFIT: Each step is independent and testable
   
3. FACTORY PATTERN (gui.py)
   ────────────────────────
   Decides which GUI to create based on argument
   
   BENEFIT: Easy to add new GUIs
   
4. FACADE PATTERN (Calculator class)
   ──────────────────────────────────
   Hides complex evaluation logic behind simple calculate() method
   
   BENEFIT: Users don't need to understand internals

LEARNING OBJECTIVE:
□ Recognize these patterns in your code
□ Use them in future projects
"""

# ==============================================================================
# PART 9: STUDY CHECKLIST
# ==============================================================================

STUDY_CHECKLIST = """
□ Read README.md completely
□ Understand project structure by opening each file
□ Read src/calculator.py and take notes
□ Run the calculator in all modes
□ Read and run tests
□ Do Exercise 1-5 above
□ Modify one UI element and see changes
□ Write your own test for a feature
□ Understand why files are organized as they are
□ Could you explain this project to a friend?
   → If yes, you've learned it!
"""

# ==============================================================================
# PART 10: ADVANCED STUDY - WHAT TO LEARN NEXT
# ==============================================================================

"""
After mastering this calculator, study these to level up:

1. DESIGN PATTERNS
   - Gang of Four patterns
   - When to use each pattern
   - Anti-patterns to avoid

2. TESTING
   - Mocking and fixtures
   - Property-based testing
   - Integration testing

3. ASYNC PROGRAMMING
   - How to make GUI responsive
   - Concurrent calculations

4. WEB FRAMEWORKS
   - Flask (already used here)
   - Django, FastAPI
   - Building REST APIs

5. DATABASE
   - Store calculation history
   - User preferences
   - Analytics

6. DEPLOYMENT
   - Docker containerization
   - Cloud deployment (AWS, Heroku)
   - CI/CD pipelines

7. ADVANCED PYTHON
   - Metaclasses
   - Decorators
   - Context managers
   - Generators
"""

# ==============================================================================
# STUDY TIPS
# ==============================================================================

"""
💡 HOW TO STUDY CODE EFFECTIVELY

1. READ BEFORE RUNNING
   - Understand what code does before running it
   - Predict output before testing
   - Compare prediction with actual result

2. TRACE EXECUTION
   - Follow a calculation from input to output
   - Add print statements to see what's happening
   - Use debugger to step through code

3. MODIFY AND OBSERVE
   - Change one thing at a time
   - See what breaks, what improves
   - This is how you learn!

4. EXPLAIN OUT LOUD
   - Pretend you're teaching someone
   - If you can't explain it, you don't understand it
   - This is the BEST learning technique

5. DRAW DIAGRAMS
   - How does data flow?
   - What calls what?
   - Visual understanding is powerful

6. WRITE NOTES
   - Summarize each section
   - Write down patterns you notice
   - Your notes are your reference

7. ASK QUESTIONS
   - Why is it done this way?
   - Could it be done differently?
   - What are the tradeoffs?

8. TEACH OTHERS
   - Explain code to someone else
   - Answer their questions
   - This solidifies your understanding

⏱️ ESTIMATED TOTAL TIME: 6-10 HOURS
   This might seem like a lot, but you're learning:
   ✓ Architecture
   ✓ Python patterns
   ✓ Testing
   ✓ UI design
   ✓ Professional project structure
   
   This is equivalent to a full college course!
"""

# ==============================================================================
# SUCCESS CRITERIA
# ==============================================================================

"""
You've successfully learned this project when you can:

□ Explain the project to someone in 2 minutes
□ Draw the architecture on paper
□ Modify a feature without looking at examples
□ Write a test for a new function
□ Add a new UI element without breaking anything
□ Understand and use design patterns
□ Explain why files are organized as they are
□ Suggest improvements and implement them
□ Help someone else understand the code

NEXT STEP:
Create your own small project using what you learned!
"""
