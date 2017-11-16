#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <cmath>
#include "cppitertools/itertools.hpp"

const int TWENTY_PRIMES[] = {
  5, 7, 11, // 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79
};

int operation(int n, int left, int right) {
    return (left + right) % n;
}

bool check_homomorphism(int p, std::vector<int> Z_p, std::vector<int> permutation) {
  // check that f(gh) = f(g)f(h) for all g, h in Z_p
  for (auto&& pair: iter::combinations_with_replacement(Z_p, 2)) {
    int left = pair[0];
    int right = pair[1];
    int left_result = permutation[operation(p, left, right)];
    int right_result = operation(p, permutation[left], permutation[right]);
    if (left_result != right_result) return false;
  }
  return true;
}

int main() {
  for (const int p: TWENTY_PRIMES) {
    int count = 0;
    std::vector<int> Z_p;
    for (auto n : iter::range(p)) {
      Z_p.push_back(n);
    }

    auto permutations = iter::permutations(Z_p);
    std::cout << "Z_p, p = " << p << " has " << std::tgamma(p) << " permutations\n";
    // auto combinations = iter::combinations_with_replacement(Z_p, 2);
    // std::cout << "   there are " << combinations.end() << " combinations\n";
    for (auto permutation_: iter::permutations(Z_p)) {
      std::vector<int> permutation;
      for (auto n : permutation_) {
        permutation.push_back(n);
      }

      bool is_homomorphism = check_homomorphism(p, Z_p, permutation);
      if (is_homomorphism){
        count = count + 1;
        std::cout << "  ( ";
        for (auto n: permutation) {
          std::cout << n << " ";
        }
        std::cout << ")\n";
      }
    }
    std::cout << "Z_p, p = " << p << " has " << count << " automorphisms \n";
  }
}
