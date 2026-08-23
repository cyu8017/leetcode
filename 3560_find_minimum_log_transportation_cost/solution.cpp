// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

#include <algorithm>

class Solution {
public:
    long long minCuttingCost(int n, int m, int k) {
        int x = std::max(n, m);
        if (x <= k) return 0;
        return 1LL * k * (x - k);
    }
};
