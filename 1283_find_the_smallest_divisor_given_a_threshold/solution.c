// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

#include <stdlib.h>

int smallestDivisor(int* nums, int numsSize, int threshold) {
    int lo = 1, hi = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > hi) hi = nums[i];
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        long long sum = 0;
        for (int i = 0; i < numsSize; i++) sum += (nums[i] + mid - 1) / mid;
        if (sum <= threshold) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
