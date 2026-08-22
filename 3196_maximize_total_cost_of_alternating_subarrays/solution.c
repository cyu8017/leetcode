// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

#include <stdlib.h>

static int n3196, *nums3196;
static long long f3196[100005][2];
static char vis3196[100005][2];

static long long dfs3196(int i, int j) {
    if (i >= n3196) return 0;
    if (vis3196[i][j]) return f3196[i][j];
    vis3196[i][j] = 1;
    long long res = (long long)nums3196[i] + dfs3196(i + 1, 1);
    if (j > 0) {
        long long t = (long long)(-nums3196[i]) + dfs3196(i + 1, 0);
        if (t > res) res = t;
    }
    return f3196[i][j] = res;
}

long long maximumTotalCost(int* nums, int numsSize) {
    n3196 = numsSize; nums3196 = nums;
    for (int i = 0; i < numsSize; i++) { vis3196[i][0] = vis3196[i][1] = 0; }
    return dfs3196(0, 0);
}
