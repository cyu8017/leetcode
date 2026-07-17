// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

#include <vector>

class Solution {
public:
    std::vector<int> findBall(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size());
        int n = static_cast<int>(grid[0].size());
        std::vector<int> ans(n);
        for (int start = 0; start < n; start++) {
            int col = start;
            for (int row = 0; row < m; row++) {
                int next = col + grid[row][col];
                if (next < 0 || next == n || grid[row][next] != grid[row][col]) {
                    col = -1;
                    break;
                }
                col = next;
            }
            ans[start] = col;
        }
        return ans;
    }
};
