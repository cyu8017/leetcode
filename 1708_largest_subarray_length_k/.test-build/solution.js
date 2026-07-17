"use strict";
// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/
function largestSubarray(nums, k) {
    let start = 0;
    for (let i = 1; i + k <= nums.length; i++) {
        if (nums[i] > nums[start]) {
            start = i;
        }
    }
    return nums.slice(start, start + k);
}
