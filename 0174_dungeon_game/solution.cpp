// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int calculateMinimumHP(std::vector<std::vector<int>>& dungeon) {
        int rows = dungeon.size();
        int cols = dungeon[0].size();
        std::vector<std::vector<int>> dp(rows + 1, std::vector<int>(cols + 1, INT_MAX));
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1;

        for (int row = rows - 1; row >= 0; --row) {
            for (int col = cols - 1; col >= 0; --col) {
                int need = std::min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col];
                dp[row][col] = std::max(1, need);
            }
        }
        return dp[0][0];
    }
};