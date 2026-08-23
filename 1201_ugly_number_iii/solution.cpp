// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

#include <numeric>

class Solution {
public:
    int nthUglyNumber(int n, int a, int b, int c) {
        auto lcm64 = [](long long x, long long y) {
            return x / std::gcd(x, y) * y;
        };
        long long ab = lcm64(a, b);
        long long ac = lcm64(a, c);
        long long bc = lcm64(b, c);
        long long abc = lcm64(ab, c);
        auto count = [&](long long x) {
            return x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;
        };
        long long lo = 1, hi = 2000000000LL;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (count(mid) >= n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return static_cast<int>(lo);
    }
};
