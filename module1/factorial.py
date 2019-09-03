def last_factorial_digit(n):
    """
    Calculate the last digit of a number, ns, factorial.

    Args:
        n - The number we're going to be computing the factorial of

    Returns:
        The last digit in the factorial of n.
    """
    # Initial condition of 1
    factorial = 1

    # Compute the factorial
    for i in range(1, n + 1):
        factorial = factorial * i

    # Mod the number by 10 in order to get the last digits
    return factorial % 10


print(last_factorial_digit(3))
