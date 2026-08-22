// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

#include <stdlib.h>
#include <string.h>

static int imax(int a, int b) { return a > b ? a : b; }

int maximumProcessableQueries(int* nums, int numsSize, int* queries, int queriesSize) {
    int n = numsSize, m = queriesSize;
    int** f = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) f[i] = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int j = n - 1; j >= i; j--) {
            if (i > 0) {
                int t = (f[i-1][j] < m && nums[i-1] >= queries[f[i-1][j]]) ? 1 : 0;
                f[i][j] = imax(f[i][j], f[i-1][j] + t);
            }
            if (j + 1 < n) {
                int t = (f[i][j+1] < m && nums[j+1] >= queries[f[i][j+1]]) ? 1 : 0;
                f[i][j] = imax(f[i][j], f[i][j+1] + t);
            }
            if (f[i][j] == m) {
                for (int a = 0; a < n; a++) free(f[a]);
                free(f);
                return m;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int t = (f[i][i] < m && nums[i] >= queries[f[i][i]]) ? 1 : 0;
        ans = imax(ans, f[i][i] + t);
    }
    for (int a = 0; a < n; a++) free(f[a]);
    free(f);
    return ans;
}
