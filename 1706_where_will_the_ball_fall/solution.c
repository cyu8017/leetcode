// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findBall(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int* ans = (int*)malloc(n * sizeof(int));
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
    *returnSize = n;
    return ans;
}
