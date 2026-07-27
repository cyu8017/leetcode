// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

#include <stdlib.h>
#include <string.h>

int maxSumAfterPartitioning(int* arr, int arrSize, int k) {
    int* dp = (int*)calloc((size_t)(arrSize + 1), sizeof(int));
    for (int i = 1; i <= arrSize; i++) {
        int best = 0;
        int maxSize = k < i ? k : i;
        for (int size = 1; size <= maxSize; size++) {
            if (arr[i - size] > best) best = arr[i - size];
            int cand = dp[i - size] + best * size;
            if (cand > dp[i]) dp[i] = cand;
        }
    }
    int ans = dp[arrSize];
    free(dp);
    return ans;
}
