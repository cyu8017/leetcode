// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

#include <stdlib.h>
#include <string.h>

long long maxSum(int* nums, int numsSize, int m, int l, int r) {
    int n = numsSize;
    long long* prefix = calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    long long* dp = calloc((size_t)(n + 1), sizeof(long long));
    long long bestSelected = -(1LL << 62);
    for (int count = 1; count <= m; count++) {
        long long* next = malloc((size_t)(n + 1) * sizeof(long long));
        memcpy(next, dp, (size_t)(n + 1) * sizeof(long long));
        int* deque = malloc((size_t)(n + 1) * sizeof(int));
        int dqh = 0, dqt = 0;
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                long long value = dp[addIndex] - prefix[addIndex];
                while (dqt > dqh) {
                    int last = deque[dqt - 1];
                    if (dp[last] - prefix[last] > value) break;
                    dqt--;
                }
                deque[dqt++] = addIndex;
            }
            int minIndex = end - r;
            while (dqt > dqh && deque[dqh] < minIndex) dqh++;
            if (dqt > dqh) {
                long long candidate = prefix[end] + dp[deque[dqh]] - prefix[deque[dqh]];
                if (candidate > next[end]) next[end] = candidate;
                if (candidate > bestSelected) bestSelected = candidate;
            }
            if (next[end - 1] > next[end]) next[end] = next[end - 1];
        }
        free(dp); free(deque);
        dp = next;
    }
    free(prefix); free(dp);
    return bestSelected;
}
