// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int abs3149(int x) { return x < 0 ? -x : x; }
static int *nums3149, n3149, **f3149, *ans3149, an3149;

static int dfs3149(int mask, int pre) {
    if (mask == (1 << n3149) - 1) return abs3149(pre - nums3149[0]);
    if (f3149[mask][pre] != -1) return f3149[mask][pre];
    int res = INT_MAX;
    for (int cur = 1; cur < n3149; cur++) {
        if (((mask >> cur) & 1) == 0) {
            int v = abs3149(pre - nums3149[cur]) + dfs3149(mask | (1 << cur), cur);
            if (v < res) res = v;
        }
    }
    return f3149[mask][pre] = res;
}

static void g3149(int mask, int pre) {
    ans3149[an3149++] = pre;
    if (mask == (1 << n3149) - 1) return;
    int res = dfs3149(mask, pre);
    for (int cur = 1; cur < n3149; cur++) {
        if (((mask >> cur) & 1) == 0) {
            if (abs3149(pre - nums3149[cur]) + dfs3149(mask | (1 << cur), cur) == res) {
                g3149(mask | (1 << cur), cur);
                break;
            }
        }
    }
}

int* findPermutation(int* nums, int numsSize, int* returnSize) {
    nums3149 = nums; n3149 = numsSize;
    f3149 = malloc((1 << n3149) * sizeof(int*));
    for (int i = 0; i < (1 << n3149); i++) {
        f3149[i] = malloc(n3149 * sizeof(int));
        for (int j = 0; j < n3149; j++) f3149[i][j] = -1;
    }
    ans3149 = malloc(n3149 * sizeof(int));
    an3149 = 0;
    g3149(1, 0);
    for (int i = 0; i < (1 << n3149); i++) free(f3149[i]);
    free(f3149);
    *returnSize = n3149;
    return ans3149;
}
