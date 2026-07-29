// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

#include <stdlib.h>

static int* beautiful(int n, int* returnSize) {
    if (n == 1) {
        int* a = (int*)malloc(sizeof(int));
        a[0] = 1;
        *returnSize = 1;
        return a;
    }
    int ls, rs;
    int* left = beautiful((n + 1) / 2, &ls);
    int* right = beautiful(n / 2, &rs);
    int* ans = (int*)malloc((size_t)(ls + rs) * sizeof(int));
    for (int i = 0; i < ls; i++) ans[i] = 2 * left[i] - 1;
    for (int i = 0; i < rs; i++) ans[ls + i] = 2 * right[i];
    free(left); free(right);
    *returnSize = ls + rs;
    return ans;
}

int* beautifulArray(int n, int* returnSize) {
    return beautiful(n, returnSize);
}
