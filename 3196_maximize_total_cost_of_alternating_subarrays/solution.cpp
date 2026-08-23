// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

#include <vector>
#include <array>
#include <algorithm>

class Solution {
public:
    long long maximumTotalCost(std::vector<int>& nums) {
        int n = (int)nums.size();
        const long long NEG = (long long)-1e18;
        std::vector<std::array<long long, 2>> memo(n, {NEG, NEG});
        auto dfs = [&](auto&& self, int i, int j) -> long long {
            if (i >= n) return 0;
            if (memo[i][j] != NEG) return memo[i][j];
            long long res = nums[i] + self(self, i + 1, 1);
            if (j > 0) res = std::max(res, -nums[i] + self(self, i + 1, 0));
            return memo[i][j] = res;
        };
        return dfs(dfs, 0, 0);
    }
};
