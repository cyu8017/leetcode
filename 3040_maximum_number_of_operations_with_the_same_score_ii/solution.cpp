// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maxOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto g = [&](int i0, int j0, int s) {
            std::vector<std::vector<int>> f(n, std::vector<int>(n, -1));
            std::function<int(int, int)> dfs = [&](int i, int j) -> int {
                if (j - i < 1) return 0;
                if (f[i][j] != -1) return f[i][j];
                int ans = 0;
                if (nums[i] + nums[i + 1] == s) ans = std::max(ans, 1 + dfs(i + 2, j));
                if (nums[i] + nums[j] == s) ans = std::max(ans, 1 + dfs(i + 1, j - 1));
                if (nums[j - 1] + nums[j] == s) ans = std::max(ans, 1 + dfs(i, j - 2));
                return f[i][j] = ans;
            };
            return dfs(i0, j0);
        };
        int a = g(2, n - 1, nums[0] + nums[1]);
        int b = g(0, n - 3, nums[n - 1] + nums[n - 2]);
        int c = g(1, n - 2, nums[0] + nums[n - 1]);
        return 1 + std::max({a, b, c});
    }
};
