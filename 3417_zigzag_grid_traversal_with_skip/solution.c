// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

#include <stdlib.h>
#include <stdbool.h>

int* zigzagTraversal(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int m = gridSize, n = gridColSize[0];
    int* ans = (int*)malloc(m * n * sizeof(int));
    int an = 0; bool skip = false;
    for (int i = 0; i < m; i++) {
        if (i % 2 == 0) {
            for (int j = 0; j < n; j++) { if (!skip) ans[an++] = grid[i][j]; skip = !skip; }
        } else {
            for (int j = n - 1; j >= 0; j--) { if (!skip) ans[an++] = grid[i][j]; skip = !skip; }
        }
    }
    *returnSize = an;
    return ans;
}
