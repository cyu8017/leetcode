// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> minAbsDiff(std::vector<std::vector<int>>& grid, int k) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<int>> ans(m - k + 1, std::vector<int>(n - k + 1));
        for (int i = 0; i <= m - k; i++) {
            for (int j = 0; j <= n - k; j++) {
                std::vector<int> nums;
                for (int x = i; x < i + k; x++)
                    for (int y = j; y < j + k; y++) nums.push_back(grid[x][y]);
                std::sort(nums.begin(), nums.end());
                int d = INT_MAX;
                for (int t = 1; t < (int)nums.size(); t++) {
                    if (nums[t] != nums[t - 1]) d = std::min(d, std::abs(nums[t] - nums[t - 1]));
                }
                if (d != INT_MAX) ans[i][j] = d;
            }
        }
        return ans;
    }
};
