// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

#include <vector>

class Solution {
public:
    std::vector<int> closestPrimes(int left, int right) {
        std::vector<char> isPrime(right + 1, 1);
        if (right >= 0) isPrime[0] = 0;
        if (right >= 1) isPrime[1] = 0;
        for (int i = 2; i * i <= right; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= right; j += i) isPrime[j] = 0;
            }
        }
        std::vector<int> primes;
        for (int i = left; i <= right; i++) if (isPrime[i]) primes.push_back(i);
        if (primes.size() < 2) return {-1, -1};
        std::vector<int> best = {primes[0], primes[1]};
        int diff = primes[1] - primes[0];
        for (int i = 1; i + 1 < (int)primes.size(); i++) {
            int d = primes[i + 1] - primes[i];
            if (d < diff) {
                diff = d;
                best = {primes[i], primes[i + 1]};
            }
        }
        return best;
    }
};
