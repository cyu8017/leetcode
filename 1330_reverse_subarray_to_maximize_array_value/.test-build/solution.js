"use strict";
// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/
function maxValueAfterReverse(nums) {
    let base = 0;
    for (let i = 0; i < nums.length - 1; i++)
        base += Math.abs(nums[i] - nums[i + 1]);
    let gain = 0, low = 1e9, high = -1e9;
    for (let i = 0; i < nums.length - 1; i++) {
        const a = nums[i], b = nums[i + 1];
        gain = Math.max(gain, Math.abs(nums[0] - b) - Math.abs(a - b), Math.abs(nums[nums.length - 1] - a) - Math.abs(a - b));
        low = Math.min(low, Math.max(a, b));
        high = Math.max(high, Math.min(a, b));
    }
    return base + Math.max(gain, 2 * (high - low));
}
