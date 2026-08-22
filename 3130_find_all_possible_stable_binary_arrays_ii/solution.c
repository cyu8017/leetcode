// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

#include <stdlib.h>

enum { MOD3130 = 1000000007 };

static int ***memo3130;
static int lim3130;

static int dfs3130(int i, int j, int k) {
    if (i < 0 || j < 0) return 0;
    if (i == 0) return (k == 1 && j <= lim3130) ? 1 : 0;
    if (j == 0) return (k == 0 && i <= lim3130) ? 1 : 0;
    if (memo3130[i][j][k] != -1) return memo3130[i][j][k];
    int res;
    if (k == 0)
        res = ((dfs3130(i - 1, j, 0) + dfs3130(i - 1, j, 1)) % MOD3130 - dfs3130(i - lim3130 - 1, j, 1) + MOD3130) % MOD3130;
    else
        res = ((dfs3130(i, j - 1, 0) + dfs3130(i, j - 1, 1)) % MOD3130 - dfs3130(i, j - lim3130 - 1, 0) + MOD3130) % MOD3130;
    return memo3130[i][j][k] = res;
}

int numberOfStableArrays(int zero, int one, int limit) {
    lim3130 = limit;
    memo3130 = malloc((zero + 1) * sizeof(int**));
    for (int i = 0; i <= zero; i++) {
        memo3130[i] = malloc((one + 1) * sizeof(int*));
        for (int j = 0; j <= one; j++) {
            memo3130[i][j] = malloc(2 * sizeof(int));
            memo3130[i][j][0] = memo3130[i][j][1] = -1;
        }
    }
    int ans = (dfs3130(zero, one, 0) + dfs3130(zero, one, 1)) % MOD3130;
    for (int i = 0; i <= zero; i++) {
        for (int j = 0; j <= one; j++) free(memo3130[i][j]);
        free(memo3130[i]);
    }
    free(memo3130);
    return ans;
}
