// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

#include <limits.h>
#include <stdlib.h>

int calculateMinimumHP(int** dungeon, int dungeonSize, int* dungeonColSize) {
    int rows = dungeonSize;
    int cols = dungeonColSize[0];
    int** dp = malloc((rows + 1) * sizeof(*dp));
    for (int row = 0; row <= rows; row++) {
        dp[row] = malloc((cols + 1) * sizeof(*dp[row]));
        for (int col = 0; col <= cols; col++) {
            dp[row][col] = INT_MAX;
        }
    }
    dp[rows][cols - 1] = dp[rows - 1][cols] = 1;

    for (int row = rows - 1; row >= 0; row--) {
        for (int col = cols - 1; col >= 0; col--) {
            int next = dp[row + 1][col] < dp[row][col + 1]
                ? dp[row + 1][col] : dp[row][col + 1];
            int need = next - dungeon[row][col];
            dp[row][col] = need > 0 ? need : 1;
        }
    }

    int result = dp[0][0];
    for (int row = 0; row <= rows; row++) {
        free(dp[row]);
    }
    free(dp);
    return result;
}