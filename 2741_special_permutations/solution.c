// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

#include <stdlib.h>
#include <string.h>

static int* nums2741;
static int n2741;
static int** memo2741;

static int dfs2741(int mask, int last) {
    const int MOD = 1000000007;
    if (mask == (1 << n2741) - 1) return 1;
    if (memo2741[mask][last] != -1) return memo2741[mask][last];
    int res = 0;
    for (int i = 0; i < n2741; i++) {
        if (mask & (1 << i)) continue;
        if (nums2741[i] % nums2741[last] == 0 || nums2741[last] % nums2741[i] == 0)
            res = (res + dfs2741(mask | (1 << i), i)) % MOD;
    }
    return memo2741[mask][last] = res;
}

int specialPerm(int* nums, int numsSize) {
    const int MOD = 1000000007;
    nums2741 = nums;
    n2741 = numsSize;
    int N = 1 << n2741;
    memo2741 = (int**)malloc((size_t)N * sizeof(int*));
    for (int i = 0; i < N; i++) {
        memo2741[i] = (int*)malloc((size_t)n2741 * sizeof(int));
        for (int j = 0; j < n2741; j++) memo2741[i][j] = -1;
    }
    int ans = 0;
    for (int i = 0; i < n2741; i++)
        ans = (ans + dfs2741(1 << i, i)) % MOD;
    for (int i = 0; i < N; i++) free(memo2741[i]);
    free(memo2741);
    return ans;
}
