// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

#include <stdlib.h>
#include <string.h>

enum { MOD3129 = 1000000007 };

static int ***memo3129;
static int lim3129;

static int dfs3129(int i, int j, int k) {
    if (i < 0 || j < 0) return 0;
    if (i == 0) return (k == 1 && j <= lim3129) ? 1 : 0;
    if (j == 0) return (k == 0 && i <= lim3129) ? 1 : 0;
    if (memo3129[i][j][k] != -1) return memo3129[i][j][k];
    int res;
    if (k == 0)
        res = ((dfs3129(i - 1, j, 0) + dfs3129(i - 1, j, 1)) % MOD3129 - dfs3129(i - lim3129 - 1, j, 1) + MOD3129) % MOD3129;
    else
        res = ((dfs3129(i, j - 1, 0) + dfs3129(i, j - 1, 1)) % MOD3129 - dfs3129(i, j - lim3129 - 1, 0) + MOD3129) % MOD3129;
    return memo3129[i][j][k] = res;
}

int numberOfStableArrays(int zero, int one, int limit) {
    lim3129 = limit;
    memo3129 = malloc((zero + 1) * sizeof(int**));
    for (int i = 0; i <= zero; i++) {
        memo3129[i] = malloc((one + 1) * sizeof(int*));
        for (int j = 0; j <= one; j++) {
            memo3129[i][j] = malloc(2 * sizeof(int));
            memo3129[i][j][0] = memo3129[i][j][1] = -1;
        }
    }
    int ans = (dfs3129(zero, one, 0) + dfs3129(zero, one, 1)) % MOD3129;
    for (int i = 0; i <= zero; i++) {
        for (int j = 0; j <= one; j++) free(memo3129[i][j]);
        free(memo3129[i]);
    }
    free(memo3129);
    return ans;
}
