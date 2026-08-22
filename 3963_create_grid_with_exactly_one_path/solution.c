// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

#include <stdlib.h>
#include <string.h>

char** createGrid(int m, int n, int* returnSize) {
    char** ans = malloc((size_t)m * sizeof(char*));
    for (int i = 0; i < m; i++) {
        ans[i] = malloc((size_t)n + 1);
        for (int j = 0; j < n; j++) ans[i][j] = '#';
        ans[i][n] = 0;
    }
    for (int j = 0; j < n; j++) ans[0][j] = '.';
    for (int i = 0; i < m; i++) ans[i][n - 1] = '.';
    *returnSize = m;
    return ans;
}
