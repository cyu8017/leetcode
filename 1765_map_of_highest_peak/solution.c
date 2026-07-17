// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** highestPeak(int** isWater, int isWaterSize, int* isWaterColSize,
                  int* returnSize, int** returnColumnSizes) {
    int m = isWaterSize;
    int n = isWaterColSize[0];
    int** dist = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) {
        dist[i] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) {
            dist[i][j] = -1;
        }
    }
    int* queue = (int*)malloc((size_t)m * n * sizeof(int));
    int head = 0;
    int tail = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (isWater[i][j]) {
                dist[i][j] = 0;
                queue[tail++] = i * n + j;
            }
        }
    }
    const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (head < tail) {
        int cell = queue[head++];
        int i = cell / n;
        int j = cell % n;
        for (int d = 0; d < 4; d++) {
            int x = i + dirs[d][0];
            int y = j + dirs[d][1];
            if (x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1) {
                dist[x][y] = dist[i][j] + 1;
                queue[tail++] = x * n + y;
            }
        }
    }
    free(queue);
    *returnSize = m;
    return dist;
}
