// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

#include <cstdint>

class Solution {
public:
    long long countCommas(long long n) {
        int64_t ans = 0;
        for (int64_t x = 1000; x <= n; x *= 1000) ans += n - x + 1;
        return ans;
    }
};
