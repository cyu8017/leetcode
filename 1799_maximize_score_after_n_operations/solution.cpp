// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> memo(1 << n, -1);
        return dp(0, n, nums, memo);
    }

private:
    int dp(int mask, int n, const std::vector<int>& nums, std::vector<int>& memo) {
        if (mask == (1 << n) - 1) return 0;
        if (memo[mask] != -1) return memo[mask];
        int step = __builtin_popcount(mask) / 2 + 1;
        int best = 0;
        for (int i = 0; i < n; i++) {
            if (mask >> i & 1) continue;
            for (int j = i + 1; j < n; j++) {
                if (mask >> j & 1) continue;
                best = std::max(
                    best,
                    step * std::gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j), n, nums, memo)
                );
            }
        }
        return memo[mask] = best;
    }
};
