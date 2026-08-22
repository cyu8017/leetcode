// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

int upperBound(int* nums, int numsSize, int target) {
    int lo = 0, hi = numsSize;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (nums[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
