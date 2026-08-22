// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

#include <stdlib.h>

int** seePeople(int** heights, int heightsSize, int* heightsColSize, int* returnSize, int** returnColumnSizes) {
    int m = heightsSize, n = heightsColSize[0];
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)calloc((size_t)n, sizeof(int));
        (*returnColumnSizes)[i] = n;
    }
    int* stack = (int*)malloc((size_t)(m > n ? m : n) * sizeof(int));
    for (int i = 0; i < m; i++) {
        int top = 0;
        for (int j = n - 1; j >= 0; j--) {
            int cnt = 0;
            while (top > 0 && heights[i][stack[top - 1]] < heights[i][j]) {
                top--;
                cnt++;
            }
            if (top > 0) cnt++;
            ans[i][j] += cnt;
            while (top > 0 && heights[i][stack[top - 1]] == heights[i][j]) top--;
            stack[top++] = j;
        }
    }
    for (int j = 0; j < n; j++) {
        int top = 0;
        for (int i = m - 1; i >= 0; i--) {
            int cnt = 0;
            while (top > 0 && heights[stack[top - 1]][j] < heights[i][j]) {
                top--;
                cnt++;
            }
            if (top > 0) cnt++;
            ans[i][j] += cnt;
            while (top > 0 && heights[stack[top - 1]][j] == heights[i][j]) top--;
            stack[top++] = i;
        }
    }
    free(stack);
    *returnSize = m;
    return ans;
}
