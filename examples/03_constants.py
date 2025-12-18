"""
Example 3: Using Built-in Constants

Learn how to use mathematical constants in your calculations.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calculator import Calculator

def main():
    """Run constant examples."""
    calc = Calculator()
    
    print("=" * 60)
    print("EXAMPLE 3: Using Built-in Mathematical Constants")
    print("=" * 60)
    print()
    
    print("Available Constants:")
    print("-" * 60)
    for name, value in calc.CONSTANTS.items():
        print(f"{name:15} = {value}")
    print()
    
    # Pi Examples
    print("=" * 60)
    print("USING π (Pi)")
    print("=" * 60)
    print()
    
    print("1. Circumference of circle with radius 5 - 2*pi*5")
    result = calc.calculate("2*pi*5")
    print(f"   Formula: C = 2πr where r = 5")
    print(f"   Result: {result}")
    print()
    
    print("2. Area of circle with radius 3 - pi*3^2")
    result = calc.calculate("pi*3**2")
    print(f"   Formula: A = πr² where r = 3")
    print(f"   Result: {result}")
    print()
    
    print("3. Half of π - pi/2")
    result = calc.calculate("pi/2")
    print(f"   Result: {result} (90° in radians)")
    print()
    
    # Euler's Number Examples
    print("=" * 60)
    print("USING e (Euler's Number)")
    print("=" * 60)
    print()
    
    print("1. e to the power of 2 - e^2")
    result = calc.calculate("e**2")
    print(f"   Result: {result}")
    print()
    
    print("2. Inverse: ln(e) - log(e)")
    result = calc.calculate("log(e)")
    print(f"   Result: {result}")
    print(f"   Note: Natural log of e always equals 1")
    print()
    
    print("3. Compound interest formula - (1 + 1/n)^n as n→∞ approaches e")
    result = calc.calculate("(1 + 1/1000000)**1000000")
    print(f"   (1 + 1/1,000,000)^1,000,000 ≈ {result}")
    print(f"   Actual e ≈ {calc.CONSTANTS['e']}")
    print()
    
    # Golden Ratio Examples
    print("=" * 60)
    print("USING φ (Golden Ratio/Phi)")
    print("=" * 60)
    print()
    
    print("1. Golden Ratio value - phi")
    result = calc.calculate("phi")
    print(f"   Result: {result}")
    print(f"   Formula: φ = (1 + √5) / 2")
    print()
    
    print("2. Golden Ratio property - phi^2 - phi - 1")
    result = calc.calculate("phi**2 - phi - 1")
    print(f"   Result: {result}")
    print(f"   Note: This always equals 0 (defining property)")
    print()
    
    print("3. Fibonacci approximation - (phi^10) / sqrt(5)")
    result = calc.calculate("phi**10 / sqrt(5)")
    print(f"   Result: {result}")
    print(f"   Note: This approximates the 10th Fibonacci number")
    print()
    
    # Tau Examples
    print("=" * 60)
    print("USING τ (Tau = 2π)")
    print("=" * 60)
    print()
    
    print("1. Tau value - tau")
    result = calc.calculate("tau")
    print(f"   Result: {result}")
    print(f"   Note: τ = 2π (one full circle in radians)")
    print()
    
    print("2. Verify tau = 2*pi")
    result = calc.calculate("tau - 2*pi")
    print(f"   tau - 2*pi = {result}")
    print(f"   Note: Should be ~0")
    print()
    
    # Complex Expression with Multiple Constants
    print("=" * 60)
    print("COMPLEX EXPRESSIONS WITH MULTIPLE CONSTANTS")
    print("=" * 60)
    print()
    
    print("1. Surface area of sphere: 4*pi*r^2 (r=2)")
    result = calc.calculate("4*pi*2**2")
    print(f"   Result: {result}")
    print()
    
    print("2. Euler's formula value: e^(i*pi) = -1")
    print(f"   Note: This is complex numbers (not implemented in basic version)")
    print()
    
    print("3. Energy-mass equivalence scale: c^2 (using speed of light approximation)")
    print(f"   Note: Speed of light c ≈ 3×10⁸ m/s")
    print()
    
    print("4. Mathematical beauty: e^(pi*i) + 1")
    print(f"   Note: This equals 0 (Euler's identity)")
    print()
    
    # Using Constants in Trigonometry
    print("=" * 60)
    print("CONSTANTS WITH TRIGONOMETRIC FUNCTIONS")
    print("=" * 60)
    print()
    
    print("1. sin(pi/2)")
    result = calc.calculate("sin(pi/2)")
    print(f"   Result: {result}")
    print()
    
    print("2. cos(pi)")
    result = calc.calculate("cos(pi)")
    print(f"   Result: {result}")
    print()
    
    print("3. tan(pi/4)")
    result = calc.calculate("tan(pi/4)")
    print(f"   Result: {result}")
    print()
    
    print("=" * 60)
    print("CALCULATION HISTORY")
    print("=" * 60)
    for i, (expr, res) in enumerate(calc.history, 1):
        print(f"{i}. {expr} = {res}")

if __name__ == "__main__":
    main()
