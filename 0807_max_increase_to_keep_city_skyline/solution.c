// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

#include <stdlib.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize) {
    int cols = gridColSize[0];
    int* rowMax = (int*)calloc((size_t)gridSize, sizeof(int));
    int* colMax = (int*)calloc((size_t)cols, sizeof(int));
    for (int r = 0; r < gridSize; r++) {
        for (int c = 0; c < cols; c++) {
            rowMax[r] = MAX(rowMax[r], grid[r][c]);
            colMax[c] = MAX(colMax[c], grid[r][c]);
        }
    }
    int ans = 0;
    for (int r = 0; r < gridSize; r++) {
        for (int c = 0; c < cols; c++) {
            ans += MIN(rowMax[r], colMax[c]) - grid[r][c];
        }
    }
    free(rowMax);
    free(colMax);
    return ans;
}
