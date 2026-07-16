// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static void dfs(
    int** heights,
    int rows,
    int cols,
    int row,
    int col,
    bool** visited,
    int previous
) {
    if (row < 0 || row >= rows || col < 0 || col >= cols || visited[row][col] ||
        heights[row][col] < previous) {
        return;
    }
    visited[row][col] = true;
    int height = heights[row][col];
    dfs(heights, rows, cols, row + 1, col, visited, height);
    dfs(heights, rows, cols, row - 1, col, visited, height);
    dfs(heights, rows, cols, row, col + 1, visited, height);
    dfs(heights, rows, cols, row, col - 1, visited, height);
}

int** pacificAtlantic(int** heights, int heightsSize, int* heightsColSize, int* returnSize,
                      int** returnColumnSizes) {
    if (heightsSize == 0 || heightsColSize[0] == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int rows = heightsSize;
    int cols = heightsColSize[0];
    bool** pacific = (bool**)malloc((size_t)rows * sizeof(bool*));
    bool** atlantic = (bool**)malloc((size_t)rows * sizeof(bool*));
    for (int row = 0; row < rows; row++) {
        pacific[row] = (bool*)calloc((size_t)cols, sizeof(bool));
        atlantic[row] = (bool*)calloc((size_t)cols, sizeof(bool));
    }

    for (int row = 0; row < rows; row++) {
        dfs(heights, rows, cols, row, 0, pacific, heights[row][0]);
        dfs(heights, rows, cols, row, cols - 1, atlantic, heights[row][cols - 1]);
    }
    for (int col = 0; col < cols; col++) {
        dfs(heights, rows, cols, 0, col, pacific, heights[0][col]);
        dfs(heights, rows, cols, rows - 1, col, atlantic, heights[rows - 1][col]);
    }

    int capacity = 16;
    int count = 0;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (pacific[row][col] && atlantic[row][col]) {
                if (count >= capacity) {
                    capacity *= 2;
                    result = (int**)realloc(result, (size_t)capacity * sizeof(int*));
                    colSizes = (int*)realloc(colSizes, (size_t)capacity * sizeof(int));
                }
                result[count] = (int*)malloc(2 * sizeof(int));
                result[count][0] = row;
                result[count][1] = col;
                colSizes[count] = 2;
                count++;
            }
        }
    }

    for (int row = 0; row < rows; row++) {
        free(pacific[row]);
        free(atlantic[row]);
    }
    free(pacific);
    free(atlantic);

    *returnSize = count;
    *returnColumnSizes = colSizes;
    return result;
}
