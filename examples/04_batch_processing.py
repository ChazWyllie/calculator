"""
Example 4: Batch Processing Multiple Calculations

Learn how to process multiple expressions at once.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calculator import Calculator

def main():
    """Run batch processing examples."""
    calc = Calculator()
    
    print("=" * 60)
    print("EXAMPLE 4: Batch Processing Multiple Calculations")
    print("=" * 60)
    print()
    
    # Example 1: Simple List of Expressions
    print("1. TEMPERATURE CONVERSIONS (Fahrenheit to Celsius)")
    print("-" * 60)
    temps_fahrenheit = [32, 68, 86, 104, 212]
    expressions = [f"(temp - 32) * 5 / 9".replace("temp", str(f)) for f in temps_fahrenheit]
    
    print("Fahrenheit → Celsius conversions:")
    for f_temp, expr in zip(temps_fahrenheit, expressions):
        result = calc.calculate(expr)
        print(f"  {f_temp}°F = {result:.1f}°C")
    print()
    
    # Example 2: Geometric Calculations
    print("2. GEOMETRIC AREA CALCULATIONS")
    print("-" * 60)
    print()
    
    print("Circle areas for different radii:")
    radii = [1, 2, 5, 10]
    for r in radii:
        expr = f"pi * {r} ** 2"
        result = calc.calculate(expr)
        print(f"  Radius {r:2d}: Area = {result:.2f} units²")
    print()
    
    print("Triangle areas (using formula: 1/2 * base * height):")
    triangles = [(3, 4), (5, 12), (7, 8), (10, 15)]
    for base, height in triangles:
        expr = f"0.5 * {base} * {height}"
        result = calc.calculate(expr)
        print(f"  Base={base:2d}, Height={height:2d}: Area = {result:.1f} units²")
    print()
    
    # Example 3: Physics Calculations
    print("3. PHYSICS CALCULATIONS")
    print("-" * 60)
    print()
    
    print("Kinetic energy (KE = 1/2 * m * v²):")
    print("(mass in kg, velocity in m/s)")
    objects = [("Car", 1000, 20), ("Bullet", 0.01, 400), ("Person", 70, 5)]
    for name, mass, velocity in objects:
        expr = f"0.5 * {mass} * {velocity}**2"
        result = calc.calculate(expr)
        print(f"  {name:8s} (m={mass:7}, v={velocity:3}): KE = {result:.2f} Joules")
    print()
    
    # Example 4: Financial Calculations
    print("4. FINANCIAL CALCULATIONS")
    print("-" * 60)
    print()
    
    print("Compound Interest (A = P(1 + r/n)^nt)")
    print("  Principal=$1000, Rate=5%, Years=10, Compounds=Annually")
    principal = 1000
    rate = 0.05
    years = 10
    compounds = 1
    expr = f"{principal} * (1 + {rate}/{compounds})**({compounds}*{years})"
    result = calc.calculate(expr)
    print(f"  Final Amount: ${result:.2f}")
    print()
    
    # Example 5: Statistical Calculations
    print("5. STATISTICAL CALCULATIONS")
    print("-" * 60)
    print()
    
    # Dataset: Student test scores
    scores = [85, 92, 78, 95, 88, 76, 91, 89]
    print(f"Student scores: {scores}")
    print()
    
    # Calculate mean
    mean_expr = f"({'+'.join(map(str, scores))})/{len(scores)}"
    mean = calc.calculate(mean_expr)
    print(f"Mean (Average): {mean:.2f}")
    print()
    
    # Calculate each deviation from mean
    print("Deviations from mean:")
    for i, score in enumerate(scores, 1):
        deviation = calc.calculate(f"{score} - {mean:.2f}")
        print(f"  Score {i}: {score} - {mean:.2f} = {deviation:.2f}")
    print()
    
    # Example 6: Engineering Calculations
    print("6. ENGINEERING CALCULATIONS")
    print("-" * 60)
    print()
    
    print("Resistor network calculations (Ohm's law: V = I × R):")
    voltages = [5, 12, 24]
    resistances = [100, 220, 470]
    for v in voltages:
        print(f"  Voltage = {v}V:")
        for r in resistances:
            expr = f"{v} / {r}"
            current = calc.calculate(expr)
            print(f"    R={r}Ω: Current = {current:.4f} A")
    print()
    
    # Example 7: Batch Math Operations
    print("7. BATCH MATH OPERATIONS")
    print("-" * 60)
    print()
    
    print("Powers of 2:")
    for n in range(1, 11):
        expr = f"2**{n}"
        result = calc.calculate(expr)
        print(f"  2^{n:2d} = {result:.0f}")
    print()
    
    # Example 8: Complex Batch Calculations
    print("8. SEQUENCE OF RELATED CALCULATIONS")
    print("-" * 60)
    print()
    
    print("Calculating terms of a sequence:")
    print("Formula: a(n) = n² + 2n + 1 = (n+1)²")
    for n in range(1, 6):
        expr = f"{n}**2 + 2*{n} + 1"
        result = calc.calculate(expr)
        print(f"  a({n}) = {result:.0f}")
    print()
    
    print("=" * 60)
    print(f"TOTAL CALCULATIONS PERFORMED: {len(calc.history)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
