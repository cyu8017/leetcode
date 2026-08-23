// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

#include <cstdint>

class Solution {
public:
    int maxSizedArray(long long s) {
        auto ok = [&](long long n) -> bool {
            long long sum = 0;
            for (long long i = 0; i < n; i++) {
                for (long long j = 0; j < n; j++) {
                    long long ij = i | j;
                    sum += ij * (n - 1) * n / 2;
                    if (sum > s) return false;
                }
            }
            return sum <= s;
        };
        long long lo = 1, hi = 2000;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return (int)lo;
    }
};
