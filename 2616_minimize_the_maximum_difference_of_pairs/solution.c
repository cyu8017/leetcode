// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimizeMax(int* nums, int numsSize, int p) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int lo = 0, hi = nums[numsSize - 1] - nums[0];
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int cnt = 0;
        for (int i = 0; i + 1 < numsSize; ) {
            if (nums[i + 1] - nums[i] <= mid) { cnt++; i += 2; }
            else i++;
        }
        if (cnt >= p) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
