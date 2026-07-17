"use strict";
// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/
function maxAscendingSum(nums) {
    let best = nums[0];
    let cur = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            cur += nums[i];
        }
        else {
            cur = nums[i];
        }
        best = Math.max(best, cur);
    }
    return best;
}
