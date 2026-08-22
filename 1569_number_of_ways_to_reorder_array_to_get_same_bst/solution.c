// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

#include <stdlib.h>

static const int MOD1569 = 1000000007;
static int** choose1569;

static long long ways1569(int* values, int n) {
    if (n < 3) return 1;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int lc = 0, rc = 0;
    for (int i = 1; i < n; i++) {
        if (values[i] < values[0]) left[lc++] = values[i];
        else right[rc++] = values[i];
    }
    long long ans = (long long)choose1569[n - 1][lc] * ways1569(left, lc) % MOD1569 * ways1569(right, rc) % MOD1569;
    free(left);
    free(right);
    return ans;
}

int numOfWays(int* nums, int numsSize) {
    int n = numsSize;
    choose1569 = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        choose1569[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
        choose1569[i][0] = choose1569[i][i] = 1;
        for (int j = 1; j < i; j++) {
            choose1569[i][j] = (choose1569[i - 1][j - 1] + choose1569[i - 1][j]) % MOD1569;
        }
    }
    int ans = (int)((ways1569(nums, n) - 1 + MOD1569) % MOD1569);
    for (int i = 0; i <= n; i++) free(choose1569[i]);
    free(choose1569);
    return ans;
}
