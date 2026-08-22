// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

#include <stdlib.h>
#include <string.h>

int sumOfPower(int* nums, int numsSize, int k) {
    const int mod = 1000000007;
    int n = numsSize;
    int** f = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        f[i] = (int*)calloc((size_t)(k + 1), sizeof(int));
    }
    f[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            f[i][j] = (int)((2LL * f[i - 1][j]) % mod);
            if (j >= nums[i - 1]) f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % mod;
        }
    }
    int ans = f[n][k];
    for (int i = 0; i <= n; i++) free(f[i]);
    free(f);
    return ans;
}
