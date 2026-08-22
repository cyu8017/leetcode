// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int countPairs(int* nums, int n, int distance) {
    int count = 0, left = 0;
    for (int right = 0; right < n; right++) {
        while (nums[right] - nums[left] > distance) {
            left++;
        }
        count += right - left;
    }
    return count;
}

int smallestDistancePair(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int lo = 0, hi = nums[numsSize - 1] - nums[0];
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (countPairs(nums, numsSize, mid) >= k) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}
