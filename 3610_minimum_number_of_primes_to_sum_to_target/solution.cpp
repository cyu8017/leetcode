// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

#include <climits>
#include <vector>

class Solution {
    static std::vector<int> primes;
    static void ensurePrimes() {
        if (!primes.empty()) return;
        int x = 2;
        while ((int)primes.size() < 1000) {
            bool is_prime = true;
            for (int p : primes) {
                if (p * p > x) break;
                if (x % p == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) primes.push_back(x);
            x++;
        }
    }

public:
    int minNumberOfPrimes(int n, int m) {
        ensurePrimes();
        const int inf = INT_MAX / 2;
        std::vector<int> f(n + 1, inf);
        f[0] = 0;
        for (int pi = 0; pi < m; pi++) {
            int x = primes[pi];
            for (int i = x; i <= n; i++)
                if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1;
        }
        return f[n] < inf ? f[n] : -1;
    }
};

std::vector<int> Solution::primes;
