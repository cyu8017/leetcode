// LeetCode 0204 - Count Primes
#include <vector>
class Solution { public: int countPrimes(int n) { if (n <= 2) return 0; std::vector<bool> prime(n, true); prime[0] = prime[1] = false; for (int p = 2; p * p < n; ++p) if (prime[p]) for (int m = p * p; m < n; m += p) prime[m] = false; int count = 0; for (bool value : prime) count += value; return count; } };
