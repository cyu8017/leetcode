// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

#include <stdlib.h>

typedef struct { int idx; long long val; } Pair;

int findMaximumLength(int* nums, int numsSize) {
    int n = numsSize;
    long long* pref = (long long*)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    int* dp = (int*)calloc(n + 1, sizeof(int));
    long long* last = (long long*)calloc(n + 1, sizeof(long long));
    Pair* dq = (Pair*)malloc((n + 2) * sizeof(Pair));
    int head = 0, tail = 0;
    dq[tail++] = (Pair){0, 0};
    for (int i = 1; i <= n; i++) {
        while (tail - head > 1 && dq[head + 1].val <= pref[i]) head++;
        int j = dq[head].idx;
        dp[i] = dp[j] + 1;
        last[i] = pref[i] - pref[j];
        long long val = pref[i] + last[i];
        while (tail > head && dq[tail - 1].val >= val) tail--;
        dq[tail++] = (Pair){i, val};
    }
    int ans = dp[n];
    free(pref); free(dp); free(last); free(dq);
    return ans;
}
