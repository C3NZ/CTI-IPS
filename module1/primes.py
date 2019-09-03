# Determine if the input number is prime
def isPrime(n):
    """
    Check if a given number is a prime number

    Args:
      n - The number we're trying to determine is a prime or not.

    Runtime:
      O(n) - We have to iterate through all prior numbers up to n, making
      the runtime linearly dependent on n.

    Returns:
      The number of primes that are below the number provided, n.
    """
    for current_number in range(2, n):
        # if the input number is evenly divisible by the current number?
        if n % current_number == 0:
            return False
    return True


# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
    """
    Count the number of primes less than the given number.

    Args:
      n - The number we're using for determining the number of primes

    Runtime:
      O(n^2) - For every number we have to iterate through all preceeding numbers
      for determining if it is a prime number.

    Returns:
      The number of primes that are below the number provided, n.
    """
    # If n is 1, there are no primes
    if n == 1:
        return 0

    # If n is 2, there is only 1 prime.
    if n == 2:
        return 1

    primeCount = 0
    for number in range(2, n):
        if isPrime(number):
            primeCount += 1

    return primeCount


if __name__ == "__main__":
    print(countPrimes(30))
