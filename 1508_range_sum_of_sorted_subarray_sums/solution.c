// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int rangeSum(int* nums, int numsSize, int n, int left, int right) {
    (void)numsSize;
    int total = n * (n + 1) / 2;
    int* values = (int*)malloc((size_t)total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            values[idx++] = sum;
        }
    }
    qsort(values, (size_t)total, sizeof(int), cmpInt);
    long long ans = 0;
    for (int i = left - 1; i < right; i++) ans += values[i];
    free(values);
    return (int)(ans % 1000000007LL);
}
