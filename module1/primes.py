# Determine if the input number is prime
def isPrime(n):
    for current_number in range(2, n):
        # if the input number is evenly divisible by the current number?
        if n % current_number == 0:
            return False
    return True


# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
    primeCount = 0
    for number in range(2, n):
        if isPrime(number):
            primeCount += 1

    return primeCount


if __name__ == "__main__":
    print(countPrimes(30))
