import functools
import itertools

PRIMES = (
    5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
    163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
    241, 251, 257, 263, 269, 271
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
