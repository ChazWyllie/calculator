"""Enumerations for the calculator module."""

from enum import Enum


class OperationType(Enum):
    """Enumeration for different types of operations supported by the calculator."""
    
    ARITHMETIC = "arithmetic"
    TRIGONOMETRIC = "trigonometric"
    LOGARITHMIC = "logarithmic"
    POWER = "power"
    STATISTICAL = "statistical"
    HYPERBOLIC = "hyperbolic"
