// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

#include <stdlib.h>
#include <string.h>

enum { INF3892 = 1LL << 60 };

static long long line3892(long long* cost, int left, int right, int choose) {
    if (choose == 0) return 0;
    if (left > right || choose > (right - left + 2) / 2) return INF3892;
    long long* prev2 = malloc((size_t)(choose + 1) * sizeof(long long));
    long long* prev1 = malloc((size_t)(choose + 1) * sizeof(long long));
    long long* current = malloc((size_t)(choose + 1) * sizeof(long long));
    prev2[0] = prev1[0] = 0;
    for (int j = 1; j <= choose; j++) prev2[j] = prev1[j] = INF3892;
    for (int i = left; i <= right; i++) {
        memcpy(current, prev1, (size_t)(choose + 1) * sizeof(long long));
        for (int j = 1; j <= choose; j++) {
            if (prev2[j - 1] != INF3892 && prev2[j - 1] + cost[i] < current[j])
                current[j] = prev2[j - 1] + cost[i];
        }
        long long* t = prev2; prev2 = prev1; prev1 = current; current = t;
    }
    long long ans = prev1[choose];
    free(prev2); free(prev1); free(current);
    return ans;
}

long long minOperations(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (k == 0) return 0;
    if (k > n / 2) return -1;
    long long* cost = calloc((size_t)n, sizeof(long long));
    for (int i = 0; i < n; i++) {
        int left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
        int need = left > right ? left : right;
        if (need >= nums[i]) cost[i] = (long long)need - nums[i] + 1;
    }
    long long answer = line3892(cost, 1, n - 1, k);
    long long withFirst = line3892(cost, 2, n - 2, k - 1);
    if (withFirst != INF3892) {
        withFirst += cost[0];
        if (withFirst < answer) answer = withFirst;
    }
    free(cost);
    if (answer == INF3892) return -1;
    return answer;
}
