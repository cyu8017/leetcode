// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

int longestMonotonicSubarray(int* nums, int numsSize) {
    int ans = 1, t = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] < nums[i]) { t++; if (t > ans) ans = t; }
        else t = 1;
    }
    t = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] > nums[i]) { t++; if (t > ans) ans = t; }
        else t = 1;
    }
    return ans;
}
