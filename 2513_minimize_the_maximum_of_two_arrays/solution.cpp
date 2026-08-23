// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

#include <numeric>

class Solution {
public:
    int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        long long lcm = 1LL * divisor1 / std::gcd(divisor1, divisor2) * divisor2;
        auto ok = [&](long long x) {
            long long a = x - x / divisor1;
            long long b = x - x / divisor2;
            long long both = x - x / lcm;
            return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1 + uniqueCnt2;
        };
        long long lo = 1, hi = 1LL << 62;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }
};
