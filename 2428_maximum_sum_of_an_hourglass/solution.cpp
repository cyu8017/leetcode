// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSum(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int ans = 0;
        for (int i = 0; i + 2 < m; i++) {
            for (int j = 0; j + 2 < n; j++) {
                int s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                      + grid[i + 1][j + 1]
                      + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
                ans = std::max(ans, s);
            }
        }
        return ans;
    }
};
