// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

#include <stdlib.h>

int maxKilledEnemies(char** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize[0] == 0) {
        return 0;
    }

    int rows = gridSize;
    int cols = gridColSize[0];
    int* rowHits = (int*)calloc((size_t)rows * cols, sizeof(int));
    int* colHits = (int*)calloc((size_t)rows * cols, sizeof(int));

    for (int row = 0; row < rows; row++) {
        int count = 0;
        for (int col = 0; col < cols; col++) {
            char cell = grid[row][col];
            if (cell == 'W') {
                count = 0;
            } else if (cell == 'E') {
                count += 1;
            } else {
                rowHits[row * cols + col] = count;
            }
        }
        count = 0;
        for (int col = cols - 1; col >= 0; col--) {
            char cell = grid[row][col];
            if (cell == 'W') {
                count = 0;
            } else if (cell == 'E') {
                count += 1;
            } else {
                rowHits[row * cols + col] += count;
            }
        }
    }

    for (int col = 0; col < cols; col++) {
        int count = 0;
        for (int row = 0; row < rows; row++) {
            char cell = grid[row][col];
            if (cell == 'W') {
                count = 0;
            } else if (cell == 'E') {
                count += 1;
            } else {
                colHits[row * cols + col] = count;
            }
        }
        count = 0;
        for (int row = rows - 1; row >= 0; row--) {
            char cell = grid[row][col];
            if (cell == 'W') {
                count = 0;
            } else if (cell == 'E') {
                count += 1;
            } else {
                colHits[row * cols + col] += count;
            }
        }
    }

    int result = 0;
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            int total = rowHits[row * cols + col] + colHits[row * cols + col];
            if (total > result) {
                result = total;
            }
        }
    }

    free(rowHits);
    free(colHits);
    return result;
}
