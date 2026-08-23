// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    long long minIncrease(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::vector<long long>> f(n, std::vector<long long>(2, -1));

        std::function<long long(int, int)> dfs = [&](int i, int j) -> long long {
            if (i >= n - 1) return 0;
            if (f[i][j] != -1) return f[i][j];
            int cost = std::max(0, std::max(nums[i - 1], nums[i + 1]) + 1 - nums[i]);
            long long ans = (long long)cost + dfs(i + 2, j);
            if (j > 0) ans = std::min(ans, dfs(i + 1, 0));
            return f[i][j] = ans;
        };

        return dfs(1, (n & 1) ^ 1);
    }
};
