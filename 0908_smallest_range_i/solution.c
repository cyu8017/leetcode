// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

int smallestRangeI(int* nums, int numsSize, int k) {
    int mn = nums[0], mx = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    int diff = mx - mn - 2 * k;
    return diff > 0 ? diff : 0;
}
