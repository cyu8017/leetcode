// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

#include <vector>

class Solution {
    int powMod(int base, int exponent, int mod) {
        long long result = 1;
        long long current = base;

        while (exponent) {
            if (exponent & 1) {
                result = result * current % mod;
            }
            current = current * current % mod;
            exponent >>= 1;
        }

        return static_cast<int>(result);
    }

public:
    int superPow(int a, std::vector<int>& b) {
        const int mod = 1337;
        a %= mod;
        int result = 1;

        for (int digit : b) {
            result = static_cast<long long>(powMod(result, 10, mod)) * powMod(a, digit, mod) % mod;
        }

        return result;
    }
};
