"""Q2: Simple addition function, refactored with clear comments and type hints.

This module provides a small, well-documented `add` function that accepts
numeric inputs (ints or floats) and returns their sum. The function performs
basic input validation and includes a short demonstration when run as a
script.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
	"""Return the sum of two numeric values.

	Parameters
	- a (int|float): The first addend.
	- b (int|float): The second addend.

	Returns
	- int|float: The arithmetic sum of `a` and `b`.

	Raises
	- TypeError: If either `a` or `b` is not an int or float.

	Notes
	- This function keeps integer results as ints when possible (e.g. 3 + 5 -> 8).
	- Floats are accepted and returned as floats (e.g. 2.5 + 1 -> 3.5).
	"""

	# Input validation: prefer explicit error to silent coercion
	if not isinstance(a, (int, float)):
		raise TypeError(f"add() expected a number for argument 'a', got {type(a).__name__}")
	if not isinstance(b, (int, float)):
		raise TypeError(f"add() expected a number for argument 'b', got {type(b).__name__}")

	# Perform and return the addition. Python preserves int type when possible.
	return a + b


if __name__ == "__main__":
	# Demo usage: call add and print the result. This mirrors the original
	# usage (add(3, 5) and print the return value) but with clearer structure.
	result = add(3, 5)  # Passing integer values
	print(result)  # Expect: 8

