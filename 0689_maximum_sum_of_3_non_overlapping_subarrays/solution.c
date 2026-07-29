// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

#include <stdlib.h>

int* maxSumOfThreeSubarrays(int* nums, int numsSize, int k, int* returnSize) {
    int windows = numsSize - k + 1;
    int* sums = (int*)malloc((size_t)windows * sizeof(int));
    int total = 0;
    for (int i = 0; i < k; i++) total += nums[i];
    sums[0] = total;
    for (int i = 1; i < windows; i++) {
        total += nums[i + k - 1] - nums[i - 1];
        sums[i] = total;
    }
    int* left = (int*)malloc((size_t)windows * sizeof(int));
    int* right = (int*)malloc((size_t)windows * sizeof(int));
    int best = 0;
    for (int i = 0; i < windows; i++) {
        if (sums[i] > sums[best]) best = i;
        left[i] = best;
    }
    best = windows - 1;
    for (int i = windows - 1; i >= 0; i--) {
        if (sums[i] >= sums[best]) best = i;
        right[i] = best;
    }
    int* answer = (int*)malloc(3 * sizeof(int));
    int bestTotal = -1;
    for (int mid = k; mid < windows - k; mid++) {
        int l = left[mid - k], r = right[mid + k];
        int t = sums[l] + sums[mid] + sums[r];
        if (t > bestTotal) {
            bestTotal = t;
            answer[0] = l; answer[1] = mid; answer[2] = r;
        }
    }
    free(sums); free(left); free(right);
    *returnSize = 3;
    return answer;
}
