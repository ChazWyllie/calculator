"""
Example 2: Trigonometric and Advanced Functions

Learn how to use mathematical functions like sin, cos, log, sqrt, etc.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calculator import Calculator

def main():
    """Run trigonometric and function examples."""
    calc = Calculator()
    
    print("=" * 60)
    print("EXAMPLE 2: Trigonometric and Advanced Functions")
    print("=" * 60)
    print()
    
    # Trigonometric Functions
    print("=" * 60)
    print("TRIGONOMETRIC FUNCTIONS (Angles in radians)")
    print("=" * 60)
    print()
    
    print("1. Sine Function - sin(π/2)")
    result = calc.calculate("sin(pi/2)")
    print(f"   Result: {result}")
    print(f"   Note: sin(90°) = 1")
    print()
    
    print("2. Cosine Function - cos(π)")
    result = calc.calculate("cos(pi)")
    print(f"   Result: {result}")
    print(f"   Note: cos(180°) = -1")
    print()
    
    print("3. Tangent Function - tan(π/4)")
    result = calc.calculate("tan(pi/4)")
    print(f"   Result: {result}")
    print(f"   Note: tan(45°) ≈ 1")
    print()
    
    # Inverse Trigonometric Functions
    print("=" * 60)
    print("INVERSE TRIGONOMETRIC FUNCTIONS")
    print("=" * 60)
    print()
    
    print("4. Inverse Sine - asin(0.5)")
    result = calc.calculate("asin(0.5)")
    print(f"   Result: {result} radians")
    print(f"   Note: sin⁻¹(0.5) = 30° = π/6 radians")
    print()
    
    print("5. Inverse Cosine - acos(0)")
    result = calc.calculate("acos(0)")
    print(f"   Result: {result} radians")
    print(f"   Note: cos⁻¹(0) = 90° = π/2 radians")
    print()
    
    # Logarithmic Functions
    print("=" * 60)
    print("LOGARITHMIC FUNCTIONS")
    print("=" * 60)
    print()
    
    print("6. Natural Logarithm - ln(e)")
    result = calc.calculate("log(e)")
    print(f"   Result: {result}")
    print(f"   Note: ln(e) = 1")
    print()
    
    print("7. Base 10 Logarithm - log10(100)")
    result = calc.calculate("log10(100)")
    print(f"   Result: {result}")
    print(f"   Note: log₁₀(100) = 2")
    print()
    
    # Exponential Function
    print("=" * 60)
    print("EXPONENTIAL FUNCTIONS")
    print("=" * 60)
    print()
    
    print("8. Exponential - exp(1)")
    result = calc.calculate("exp(1)")
    print(f"   Result: {result}")
    print(f"   Note: e¹ ≈ 2.718")
    print()
    
    # Power and Root Functions
    print("=" * 60)
    print("POWER AND ROOT FUNCTIONS")
    print("=" * 60)
    print()
    
    print("9. Square Root - sqrt(16)")
    result = calc.calculate("sqrt(16)")
    print(f"   Result: {result}")
    print()
    
    print("10. Cube Root - cbrt(27)")
    result = calc.calculate("cbrt(27)")
    print(f"   Result: {result}")
    print()
    
    # Hyperbolic Functions
    print("=" * 60)
    print("HYPERBOLIC FUNCTIONS")
    print("=" * 60)
    print()
    
    print("11. Hyperbolic Sine - sinh(1)")
    result = calc.calculate("sinh(1)")
    print(f"   Result: {result}")
    print()
    
    print("12. Hyperbolic Cosine - cosh(0)")
    result = calc.calculate("cosh(0)")
    print(f"   Result: {result}")
    print()
    
    # Absolute Value
    print("=" * 60)
    print("OTHER USEFUL FUNCTIONS")
    print("=" * 60)
    print()
    
    print("13. Absolute Value - abs(-42)")
    result = calc.calculate("abs(-42)")
    print(f"   Result: {result}")
    print()
    
    # Degrees to Radians
    print("14. Convert 180° to Radians - radians(180)")
    result = calc.calculate("radians(180)")
    print(f"   Result: {result}")
    print(f"   Note: 180° = π radians")
    print()
    
    # Degrees Conversion
    print("15. Convert π radians to Degrees - degrees(pi)")
    result = calc.calculate("degrees(pi)")
    print(f"   Result: {result}°")
    print(f"   Note: π radians = 180°")
    print()
    
    print("=" * 60)
    print("CALCULATION HISTORY")
    print("=" * 60)
    for i, (expr, res) in enumerate(calc.history, 1):
        print(f"{i}. {expr} = {res}")

if __name__ == "__main__":
    main()
