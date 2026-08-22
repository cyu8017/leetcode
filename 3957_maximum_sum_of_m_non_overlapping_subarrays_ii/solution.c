// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { long long value; int count; } St3957;

static int better3957(St3957 a, St3957 b) {
    return a.value > b.value || (a.value == b.value && a.count > b.count);
}

static long long* prefix3957;
static int n3957, l3957, r3957;

static St3957 run3957(long long penalty) {
    St3957* dp = calloc((size_t)(n3957 + 1), sizeof(St3957));
    int* deque = malloc((size_t)(n3957 + 1) * sizeof(int));
    int dqh = 0, dqt = 0;
    for (int end = 1; end <= n3957; end++) {
        int addIndex = end - l3957;
        if (addIndex >= 0) {
            while (dqt > dqh) {
                int b = deque[dqt - 1];
                St3957 left = {dp[addIndex].value - prefix3957[addIndex], dp[addIndex].count};
                St3957 right = {dp[b].value - prefix3957[b], dp[b].count};
                if (!better3957(left, right)) break;
                dqt--;
            }
            deque[dqt++] = addIndex;
        }
        int minIndex = end - r3957;
        while (dqt > dqh && deque[dqh] < minIndex) dqh++;
        dp[end] = dp[end - 1];
        if (dqt > dqh) {
            int start = deque[dqh];
            St3957 take = {dp[start].value + prefix3957[end] - prefix3957[start] - penalty, dp[start].count + 1};
            if (better3957(take, dp[end])) dp[end] = take;
        }
    }
    St3957 res = dp[n3957];
    free(dp); free(deque);
    return res;
}

long long maxSum(int* nums, int numsSize, int m, int l, int r) {
    n3957 = numsSize; l3957 = l; r3957 = r;
    prefix3957 = calloc((size_t)(n3957 + 1), sizeof(long long));
    for (int i = 0; i < n3957; i++) prefix3957[i + 1] = prefix3957[i] + nums[i];
    St3957 unconstrained = run3957(0);
    if (unconstrained.count > 0 && unconstrained.count <= m) {
        long long ans = unconstrained.value;
        free(prefix3957);
        return ans;
    }
    if (unconstrained.count > m) {
        long long bound = 0;
        for (int i = 0; i < n3957; i++) bound += nums[i] >= 0 ? nums[i] : -nums[i];
        long long low = 0, high = bound + 1;
        while (low < high) {
            long long mid = low + (high - low + 1) / 2;
            if (run3957(mid).count >= m) low = mid;
            else high = mid - 1;
        }
        St3957 state = run3957(low);
        long long ans = state.value + low * m;
        free(prefix3957);
        return ans;
    }
    const long long infinity = 1LL << 60;
    long long bestSingle = -infinity;
    int* deque = malloc((size_t)(n3957 + 1) * sizeof(int));
    int dqh = 0, dqt = 0;
    for (int end = 1; end <= n3957; end++) {
        int addIndex = end - l;
        if (addIndex >= 0) {
            while (dqt > dqh && prefix3957[deque[dqt - 1]] >= prefix3957[addIndex]) dqt--;
            deque[dqt++] = addIndex;
        }
        int minIndex = end - r;
        while (dqt > dqh && deque[dqh] < minIndex) dqh++;
        if (dqt > dqh) {
            long long sum = prefix3957[end] - prefix3957[deque[dqh]];
            if (sum > bestSingle) bestSingle = sum;
        }
    }
    free(deque); free(prefix3957);
    return bestSingle;
}
