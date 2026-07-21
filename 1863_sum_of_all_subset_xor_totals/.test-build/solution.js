"use strict";
// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/
function subsetXORSum(nums) {
    let bits = 0;
    for (const num of nums)
        bits |= num;
    let total = 0;
    for (let bit = 1; bit <= bits; bit <<= 1) {
        if (bits & bit)
            total += bit;
    }
    return total << (nums.length - 1);
}
