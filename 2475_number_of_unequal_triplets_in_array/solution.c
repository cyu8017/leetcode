// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

#include <stdlib.h>
#include <string.h>

int unequalTriplets(int* nums, int numsSize) {
    int cnt[1001] = {0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    int ans = 0, left = 0, n = numsSize;
    for (int x = 0; x <= 1000; x++) {
        int c = cnt[x];
        if (!c) continue;
        int right = n - left - c;
        ans += left * c * right;
        left += c;
    }
    return ans;
}
