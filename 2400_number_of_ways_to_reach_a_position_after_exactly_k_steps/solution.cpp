// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

#include <cmath>
#include <algorithm>

class Solution {
public:
    int numberOfWays(int startPos, int endPos, int k) {
        const int mod = 1000000007;
        int diff = std::abs(endPos - startPos);
        if (diff > k || (k - diff) % 2 != 0) return 0;
        int r = (k + diff) / 2;
        return comb(k, r, mod);
    }

private:
    int comb(int n, int r, int mod) {
        if (r < 0 || r > n) return 0;
        long long num = 1, den = 1;
        for (int i = 0; i < r; i++) {
            num = num * (n - i) % mod;
            den = den * (i + 1) % mod;
        }
        return (int)(num * modInverse((int)den, mod) % mod);
    }

    int modInverse(int a, int mod) {
        return modPow(a, mod - 2, mod);
    }

    int modPow(int a, int e, int mod) {
        long long res = 1, base = a % mod;
        while (e > 0) {
            if (e & 1) res = res * base % mod;
            base = base * base % mod;
            e >>= 1;
        }
        return (int)res;
    }
};
