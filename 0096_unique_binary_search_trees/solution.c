// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

#include <stdlib.h>

int numTrees(int n) {
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    dp[0] = 1;
    for (int nodes = 1; nodes <= n; ++nodes) {
        for (int root = 1; root <= nodes; ++root) {
            dp[nodes] += dp[root - 1] * dp[nodes - root];
        }
    }
    int result = dp[n];
    free(dp);
    return result;
}
