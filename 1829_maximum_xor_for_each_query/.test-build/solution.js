"use strict";
// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/
function getMaximumXor(nums, maximumBit) {
    const limit = (1 << maximumBit) - 1;
    let current = 0;
    for (const num of nums)
        current ^= num;
    const result = [];
    for (let i = nums.length - 1; i >= 0; i--) {
        result.push(current ^ limit);
        current ^= nums[i];
    }
    return result;
}
