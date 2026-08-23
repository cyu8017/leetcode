// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

#include <algorithm>
#include <cstdint>

class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        int64_t a = (int64_t)need1 * cost1 + (int64_t)need2 * cost2;
        int64_t b = (int64_t)costBoth * std::max(need1, need2);
        int mn = std::min(need1, need2);
        int64_t c = (int64_t)costBoth * mn + (int64_t)(need1 - mn) * cost1 + (int64_t)(need2 - mn) * cost2;
        return std::min({a, b, c});
    }
};
