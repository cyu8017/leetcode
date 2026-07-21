"use strict";
// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
function minOperations(nums) {
    let ops = 0;
    let prev = nums[0];
    for (let i = 1; i < nums.length; i++) {
        let value = nums[i];
        if (value <= prev) {
            const needed = prev + 1;
            ops += needed - value;
            prev = needed;
        }
        else {
            prev = value;
        }
    }
    return ops;
}
