// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<int> solve(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        const long long mod = 1000000007LL;
        int n = (int)nums.size();
        int block = (int)std::sqrt((double)n) + 1;
        std::vector<std::vector<int>> dp(block, std::vector<int>(n, 0));
        for (int step = 1; step < block; step++) {
            for (int i = n - 1; i >= 0; i--) {
                long long next = i + step < n ? dp[step][i + step] : 0;
                dp[step][i] = (int)((nums[i] + next) % mod);
            }
        }
        std::vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& query : queries) {
            int start = query[0];
            int step = query[1];
            if (step < block) {
                ans.push_back(dp[step][start]);
            } else {
                long long total = 0;
                for (int i = start; i < n; i += step) {
                    total += nums[i];
                }
                ans.push_back((int)(total % mod));
            }
        }
        return ans;
    }
};
