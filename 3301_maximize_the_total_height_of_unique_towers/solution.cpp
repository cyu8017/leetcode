// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maximumTotalSum(std::vector<int>& maximumHeight) {
        std::sort(maximumHeight.begin(), maximumHeight.end(), std::greater<int>());
        long long ans = 0;
        long long prev = (long long)1e18;
        for (int h : maximumHeight) {
            long long cur = h;
            if (cur >= prev) cur = prev - 1;
            if (cur <= 0) return -1;
            ans += cur;
            prev = cur;
        }
        return ans;
    }
};
