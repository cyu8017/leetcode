// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

#include <stdlib.h>
#include <string.h>

static int* nums3040;
static int n3040;
static int** memo3040;

static int imax(int a, int b) { return a > b ? a : b; }

static int dfs3040(int i, int j, int s) {
    if (j - i < 1) return 0;
    if (memo3040[i][j] != -1) return memo3040[i][j];
    int ans = 0;
    if (nums3040[i] + nums3040[i + 1] == s) ans = imax(ans, 1 + dfs3040(i + 2, j, s));
    if (nums3040[i] + nums3040[j] == s) ans = imax(ans, 1 + dfs3040(i + 1, j - 1, s));
    if (nums3040[j - 1] + nums3040[j] == s) ans = imax(ans, 1 + dfs3040(i, j - 2, s));
    return memo3040[i][j] = ans;
}

static int g3040(int i, int j, int s) {
    for (int a = 0; a < n3040; a++) for (int b = 0; b < n3040; b++) memo3040[a][b] = -1;
    return dfs3040(i, j, s);
}

int maxOperations(int* nums, int numsSize) {
    n3040 = numsSize;
    nums3040 = nums;
    memo3040 = (int**)malloc((size_t)n3040 * sizeof(int*));
    for (int i = 0; i < n3040; i++) memo3040[i] = (int*)malloc((size_t)n3040 * sizeof(int));
    int a = g3040(2, n3040 - 1, nums[0] + nums[1]);
    int b = g3040(0, n3040 - 3, nums[n3040 - 1] + nums[n3040 - 2]);
    int c = g3040(1, n3040 - 2, nums[0] + nums[n3040 - 1]);
    int ans = 1 + imax(a, imax(b, c));
    for (int i = 0; i < n3040; i++) free(memo3040[i]);
    free(memo3040);
    return ans;
}
