// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

#include <stdbool.h>

int minCapability(int* nums, int numsSize, int k) {
    int lo = nums[0], hi = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < lo) lo = nums[i];
        if (nums[i] > hi) hi = nums[i];
    }
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int cnt = 0;
        for (int i = 0; i < numsSize; ) {
            if (nums[i] <= mid) { cnt++; i += 2; }
            else i++;
        }
        if (cnt >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
