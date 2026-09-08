def prime_list(n):
    is_prime = [True] * (n + 1)
# sieve of erathoses
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):

        if is_prime[i]:

            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    primes = []

    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


prime_list(28)