// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

#include <stdlib.h>

static int best_pair(int* prefix, int n, int a, int b) {
    int bestA = 0, ans = 0;
    for (int i = a + b; i <= n; i++) {
        int sumA = prefix[i - b] - prefix[i - b - a];
        if (sumA > bestA) bestA = sumA;
        int sumB = prefix[i] - prefix[i - b];
        int total = bestA + sumB;
        if (total > ans) ans = total;
    }
    return ans;
}

int maxSumTwoNoOverlap(int* nums, int numsSize, int firstLen, int secondLen) {
    int* prefix = (int*)malloc((size_t)(numsSize + 1) * sizeof(int));
    prefix[0] = 0;
    for (int i = 0; i < numsSize; i++) prefix[i + 1] = prefix[i] + nums[i];
    int a = best_pair(prefix, numsSize, firstLen, secondLen);
    int b = best_pair(prefix, numsSize, secondLen, firstLen);
    free(prefix);
    return a > b ? a : b;
}
