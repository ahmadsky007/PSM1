import math


def sin_x_taylor_series(x, n_terms):
    """
Compute sin(x) using the Taylor series approximation.
Parameters:
    - x: The value for which to compute sin(x).
    - n_terms: The number of terms to include in the Taylor series approximation.
Returns:
    - The approximation of sin(x) using the Taylor series.
    """
    sin_x = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_x += term
    return sin_x
# User inputs
x = float(input("Enter the value of x (in radians): "))
n_terms = int(input("Enter the number of terms to use in the Taylor series approximation: "))
# Compute and display the approximation
approx_sin_x = sin_x_taylor_series(x, n_terms)
print(f"The approximation of sin({x}) using {n_terms} terms of its Taylor series is: {approx_sin_x}")
