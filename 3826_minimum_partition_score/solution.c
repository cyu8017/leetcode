// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

#include <stdlib.h>
#include <string.h>

enum { INF3826 = (1LL << 62) };

static long long* prefix3826;
static long long* previous3826;
static long long* current3826;

static long long value3826(int left, int right) {
    long long sum = prefix3826[right] - prefix3826[left];
    return sum * (sum + 1) / 2;
}

static void compute3826(int lo, int hi, int optLo, int optHi) {
    if (lo > hi) return;
    int mid = (lo + hi) / 2;
    int bestIndex = -1;
    int end = optHi;
    if (mid - 1 < end) end = mid - 1;
    for (int split = optLo; split <= end; split++) {
        if (previous3826[split] == INF3826) continue;
        long long candidate = previous3826[split] + value3826(split, mid);
        if (candidate < current3826[mid]) {
            current3826[mid] = candidate;
            bestIndex = split;
        }
    }
    if (bestIndex == -1) bestIndex = optLo;
    compute3826(lo, mid - 1, optLo, bestIndex);
    compute3826(mid + 1, hi, bestIndex, optHi);
}

long long minPartitionScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    prefix3826 = (long long*)calloc((size_t)n + 1, sizeof(long long));
    for (int i = 0; i < n; i++) prefix3826[i + 1] = prefix3826[i] + nums[i];
    previous3826 = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    previous3826[0] = 0;
    for (int i = 1; i <= n; i++) previous3826[i] = INF3826;
    for (int parts = 1; parts <= k; parts++) {
        current3826 = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
        for (int i = 0; i <= n; i++) current3826[i] = INF3826;
        compute3826(parts, n, parts - 1, n - 1);
        free(previous3826);
        previous3826 = current3826;
    }
    long long ans = previous3826[n];
    free(prefix3826); free(previous3826);
    return ans;
}
