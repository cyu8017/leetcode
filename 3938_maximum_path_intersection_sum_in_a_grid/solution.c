// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

#include <limits.h>

int maxPathSum(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize, cols = gridColSize[0];
    int answer = INT_MIN;
    for (int row = 0; row < rows; row++) {
        int bestEnding = grid[row][0] + grid[row][1];
        if (bestEnding > answer) answer = bestEnding;
        for (int i = 2; i < cols; i++) {
            int cand = grid[row][i - 1] + grid[row][i];
            if (cand > bestEnding + grid[row][i]) bestEnding = cand;
            else bestEnding += grid[row][i];
            if (bestEnding > answer) answer = bestEnding;
        }
    }
    for (int col = 0; col < cols; col++) {
        int bestEnding = grid[0][col] + grid[1][col];
        if (bestEnding > answer) answer = bestEnding;
        for (int i = 2; i < rows; i++) {
            int cand = grid[i - 1][col] + grid[i][col];
            if (cand > bestEnding + grid[i][col]) bestEnding = cand;
            else bestEnding += grid[i][col];
            if (bestEnding > answer) answer = bestEnding;
        }
    }
    for (int row = 1; row + 1 < rows; row++)
        for (int col = 1; col + 1 < cols; col++)
            if (grid[row][col] > answer) answer = grid[row][col];
    return answer;
}
