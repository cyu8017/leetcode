// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

#include <algorithm>
#include <numeric>

class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        const int MOD = 1'000'000'007;
        long long lcm = static_cast<long long>(a) / std::gcd(a, b) * b;
        long long lo = 1, hi = static_cast<long long>(n) * std::min(a, b);
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (mid / a + mid / b - mid / lcm >= n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return static_cast<int>(lo % MOD);
    }
};
