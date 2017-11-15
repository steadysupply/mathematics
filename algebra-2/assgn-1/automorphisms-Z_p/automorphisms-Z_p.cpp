#include <iostream>
#include <vector>
#include <array>
#include <map>
#include "cppitertools/itertools.hpp"

std::array<int, 20> TWENTY_PRIMES = {
    5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73
};

template <int n> int addition_modulo(int left, int right) {
    return (left + right) % n;
}

/*
bool check_homomorphism(vector<int> permutation, vector<int> Z_p) {
     map<int int> function = 
*/

int main() {
}
