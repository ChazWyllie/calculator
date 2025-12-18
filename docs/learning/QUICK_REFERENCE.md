# 🎓 Quick Reference Card - Learning This Project

Print this page and keep it handy!

---

## 🚀 Get Started (5 minutes)

```bash
# 1. Navigate to project
cd /Users/chazwyllie/Git/calculator

# 2. Activate virtual environment
source venv/bin/activate

# 3. Run interactive explorer
python explore.py

# 4. Or run the calculator
python main.py web
```

---

## 📂 Project Files at a Glance

```
calculator/
├── src/                    Core code
│   ├── calculator.py       ← MOST IMPORTANT (read first!)
│   ├── enums.py           Supporting enums
│   ├── ui.py              Terminal interface
│   └── gui_*.py           GUI implementations (3 versions)
│
├── tests/
│   └── test_calculator.py  Unit tests (20 tests)
│
└── Documentation
    ├── README.md                ← Start here
    ├── SETUP.md                 Setup guide
    ├── DEVELOPER_GUIDE.md        ← Deep dive with diagrams
    ├── LEARNING_PATH.md          ← Full curriculum
    └── LEARNING_RESOURCES.md     This resources guide
```

---

## 🎯 30-Minute Learning Path

### Minute 1-5: Read
- Open and skim README.md

### Minute 6-15: Explore
- Run: `python explore.py`
- Choose option 6 (test edge cases)
- See the calculator in action

### Minute 16-25: Understand
- Read Architecture section of DEVELOPER_GUIDE.md

### Minute 26-30: Hands-On
- Run: `python main.py "2 + 3 * 4"`
- Try: `python main.py "sin(pi/2)"`
- Observe the results

---

## 🔑 Key Code Sections

### Most Important
```python
# src/calculator.py - Lines 137-190
def calculate(self, expression: str) -> Union[float, str]:
    """HEART OF THE PROJECT - understand this!"""
    validate() → preprocess() → eval() → store → return
```

### Next Most Important
```python
# src/calculator.py - Lines 107-135
def preprocess_expression(self, expression: str) -> str:
    """Transform user input for evaluation"""
    Replaces constants, handles implicit multiplication
```

### Test Everything
```python
# tests/test_calculator.py
20 test cases covering all functionality
Command: pytest tests/ -v
```

---

## 💾 Code You Should Memorize

### The Pipeline Pattern
```
INPUT → VALIDATE → PREPROCESS → EVALUATE → STORE → OUTPUT
```

### Class Structure
```python
class Calculator:
    CONSTANTS = {...}        # Class variable
    FUNCTIONS = {...}        # Class variable
    
    def __init__(self):       # Initialize
    def validate(self):       # Check input
    def preprocess(self):     # Transform input
    def calculate(self):      # Main method
```

### How to Add a Function
```python
# In src/calculator.py, FUNCTIONS dict, add:
'newfunction': math.newfunction,
```

### How to Add a Constant
```python
# In src/calculator.py, CONSTANTS dict, add:
'newconstant': 3.14159,
```

---

## 📖 5 Documents to Master

1. **README.md** (15 min)
   - What is this?
   - What can it do?

2. **DEVELOPER_GUIDE.md** (1 hour)
   - How is it organized?
   - What patterns are used?

3. **LEARNING_PATH.md** (2 hours)
   - Detailed curriculum
   - 10 parts, exercises included

4. **explore.py** (30 min)
   - Interactive exploration
   - Run: `python explore.py`

5. **LEARNING_RESOURCES.md** (this file)
   - Navigation guide
   - Learning tips

---

## 🧪 Essential Commands

```bash
# Run calculator
python main.py                          # Interactive menu
python main.py "2 + 3"                 # Calculate expression
python main.py web                      # Web GUI

# Run tests
pytest tests/                          # All tests
pytest tests/ -v                       # Verbose output
pytest tests/ --cov=src                # With coverage

# Explore code
python explore.py                      # Interactive explorer

# Development
make test                              # Run tests
make lint                              # Check code style
make format                            # Format code
```

---

## 🎯 Learning Milestones

### ✅ Level 1: Understand (Day 1)
- [ ] Read README.md
- [ ] Run `python explore.py`
- [ ] Can you explain what the calculator does?

### ✅ Level 2: Navigate (Day 2-3)
- [ ] Read DEVELOPER_GUIDE.md
- [ ] Find calculator.py and understand it
- [ ] Can you trace a calculation?

### ✅ Level 3: Modify (Day 4-5)
- [ ] Complete exercises 1-3
- [ ] Add a new function
- [ ] Write a test for it

### ✅ Level 4: Master (Day 6-7)
- [ ] Complete exercises 4-5
- [ ] Modify a GUI
- [ ] Suggest an improvement

### ✅ Level 5: Teach (Day 8)
- [ ] Explain to someone else
- [ ] Answer their questions
- [ ] You've mastered it!

---

## 🐛 Debugging Tips

### Problem: Don't understand a line
**Solution:** Add print statement before that line
```python
print(f"DEBUG: variable = {variable}")
```

### Problem: Function not working
**Solution:** Look at tests first
```bash
grep -n "test_function_name" tests/test_calculator.py
```

### Problem: Can't find where something is used
**Solution:** Search the codebase
```bash
grep -r "function_name" src/
```

### Problem: Error message unclear
**Solution:** Run with verbose mode
```python
calc = Calculator(verbose=True)
calc.calculate("expression")
```

---

## 📊 Code Statistics

- **Total Lines of Code:** ~2,000
- **Core Logic:** ~265 lines (calculator.py)
- **GUI Code:** ~1,200 lines (3 GUIs)
- **Tests:** ~170 lines (20 test cases)
- **Documentation:** ~1,000 lines (you're reading it!)

**Total Learning Material:** ~5,000+ lines

---

## 🏆 Success Indicators

### You're on the right track if:
- ✓ You can run the calculator
- ✓ You understand validate/preprocess/evaluate
- ✓ You can add a function
- ✓ You can write a test
- ✓ You can explain it to someone

### You've mastered it if:
- ✓ You could code this from scratch
- ✓ You could teach others
- ✓ You could add advanced features
- ✓ You understand all design patterns
- ✓ You could deploy it to production

---

## 🎓 What You'll Learn

| Concept | Where | Time |
|---------|-------|------|
| Architecture | DEVELOPER_GUIDE | 30 min |
| Python patterns | LEARNING_PATH | 1 hour |
| Testing | test_calculator.py | 45 min |
| GUI design | gui_*.py | 1 hour |
| Design patterns | DEVELOPER_GUIDE | 1 hour |
| Error handling | calculator.py | 30 min |
| Type hints | Any .py file | 20 min |
| Project structure | README + structure | 15 min |

**Total:** 6-10 hours for full mastery

---

## 🔍 Quick File Finder

```
I want to understand...

The core logic?
→ src/calculator.py (lines 137-190)

How to add features?
→ src/calculator.py (look for FUNCTIONS, CONSTANTS)

How tests work?
→ tests/test_calculator.py

How UIs work?
→ src/gui_web.py (simplest to understand)

How it all connects?
→ main.py + gui.py

Project structure rationale?
→ DEVELOPER_GUIDE.md (Architecture section)
```

---

## 💪 Motivation

Remember why you're learning this:

1. **Real code** - Not a tutorial, actual production code
2. **Professional structure** - Industry best practices
3. **Multiple skills** - Python, testing, GUIs, patterns
4. **Career valuable** - These skills are in demand
5. **Foundation** - Build on this knowledge forever

**You're investing in your future! 🚀**

---

## 📞 When You're Stuck

1. Check LEARNING_RESOURCES.md
2. Search DEVELOPER_GUIDE.md
3. Look at relevant tests
4. Add print statements
5. Ask yourself: "Why?"
6. Read the docstrings
7. Run explore.py

---

## 🎯 One Month Mastery Plan

**Week 1:** Foundations (5 hours)
- Read documentation
- Run the code
- Understand architecture

**Week 2:** Deep Dive (6 hours)
- Study each module
- Trace calculations
- Complete exercises

**Week 3:** Hands-On (4 hours)
- Add features
- Write tests
- Modify UI

**Week 4:** Mastery (3 hours)
- Teach others
- Suggest improvements
- Deploy/share

**Total: ~18 hours to mastery**

---

## 🚀 After You Master This

Your next challenge:

```
Build something similar but different:
- A unit converter
- A statistics analyzer
- A physics calculator
- A chemistry calculator
- Your own unique tool!

Use what you learned here as the blueprint!
```

---

**Good luck! You've got this! 💪**

*Last updated: December 2025*
