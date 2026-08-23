// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minIncrementOperations(std::vector<int>& nums, int k) {
        long long dp0 = 0, dp1 = 0, dp2 = 0;
        for (int v : nums) {
            long long cost = v < k ? (k - v) : 0;
            long long nd0 = cost + std::min({dp0, dp1, dp2});
            dp0 = dp1; dp1 = dp2; dp2 = nd0;
        }
        return std::min({dp0, dp1, dp2});
    }
};
