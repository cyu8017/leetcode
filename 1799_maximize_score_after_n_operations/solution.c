// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

#include <stdlib.h>

static int gcdInt(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static int dp(int mask, int n, const int* nums, int* memo) {
    if (mask == (1 << n) - 1) return 0;
    if (memo[mask] != -1) return memo[mask];
    int bits = 0;
    for (int m = mask; m; m &= m - 1) bits++;
    int step = bits / 2 + 1;
    int best = 0;
    for (int i = 0; i < n; i++) {
        if (mask >> i & 1) continue;
        for (int j = i + 1; j < n; j++) {
            if (mask >> j & 1) continue;
            int score = step * gcdInt(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j), n, nums, memo);
            if (score > best) best = score;
        }
    }
    memo[mask] = best;
    return best;
}

int maxScore(int* nums, int numsSize) {
    int total = 1 << numsSize;
    int* memo = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; i++) memo[i] = -1;
    int ans = dp(0, numsSize, nums, memo);
    free(memo);
    return ans;
}
