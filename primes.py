"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    # Start with an empty list for prime numbers
    prime_numbers = []

    # Skip 1, as prime numbers are greater or equal to 2
    test = 2

    # Count limits length of list 
    while count > len(prime_numbers):
        # Start with Prime being True and will be False if divisible by any previous primes
        prime = True
        for number in prime_numbers:
            if test % number == 0:
                prime = False
                # Break loop so do not test any further numbers
                break
        # Add prime to list
        if prime == True:
            prime_numbers.append(test)
        # Test next number
        test = test + 1
    print prime_numbers


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
