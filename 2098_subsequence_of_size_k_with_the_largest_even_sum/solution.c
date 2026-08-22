// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

long long largestEvenSum(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpDesc);
    long long sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];
    if (sum % 2 == 0) return sum;
    long long ans = -1;
    int oddIn = -1, evenIn = -1;
    for (int i = k - 1; i >= 0; i--) {
        if (nums[i] % 2 == 1 && oddIn == -1) oddIn = i;
        if (nums[i] % 2 == 0 && evenIn == -1) evenIn = i;
    }
    int oddOut = -1, evenOut = -1;
    for (int i = k; i < numsSize; i++) {
        if (nums[i] % 2 == 1 && oddOut == -1) oddOut = i;
        if (nums[i] % 2 == 0 && evenOut == -1) evenOut = i;
    }
    if (oddIn != -1 && evenOut != -1) {
        long long cand = sum - nums[oddIn] + nums[evenOut];
        if (cand > ans) ans = cand;
    }
    if (evenIn != -1 && oddOut != -1) {
        long long cand = sum - nums[evenIn] + nums[oddOut];
        if (cand > ans) ans = cand;
    }
    return ans;
}
