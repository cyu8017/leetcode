// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> f(n);
        auto dfs = [&](auto&& self, int i) -> int {
            if (f[i] > 0) return f[i];
            for (int j = i + 1; j < n; j++) {
                f[i] = std::max(f[i], (j - i) * nums[j] + self(self, j));
            }
            return f[i];
        };
        return dfs(dfs, 0);
    }
};
