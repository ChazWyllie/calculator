"""Advanced Calculator Package."""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A comprehensive mathematical calculator with support for various functions and operations."

from .calculator import Calculator
from .enums import OperationType

__all__ = ["Calculator", "OperationType"]
