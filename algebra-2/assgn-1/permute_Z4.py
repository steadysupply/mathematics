import functools
import itertools

PRIMES = (
    4, 5, 6, 7, 8, 9, 10
)

def addition_modulo_n(n, left, right):
    return (left + right) % n

def check_homomorphism(permutation, against):
    function = dict(zip(permutation, against))
    for left, right in itertools.combinations_with_replacement(against, 2):
        left_result  = function[operation(left, right)]
        right_result = operation(function[left], function[right])
        if left_result != right_result:
            return False
    return True

for p in PRIMES:
    count = 0
    Z_p = range(p)
    operation = functools.partial(addition_modulo_n, p)
    permutations = itertools.permutations(Z_p)
    for permutation in permutations:
        is_homomorphism = check_homomorphism(permutation, Z_p)
        if is_homomorphism:
            print("    {0}".format(permutation))
            count = count + 1
    print("{0} automorphisms for Z_{1}".format(count, p))
