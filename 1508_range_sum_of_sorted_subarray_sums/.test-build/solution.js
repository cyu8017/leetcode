"use strict";
// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
// @ts-nocheck
function rangeSum(nums, n, left, right) {
    const values = [];
    for (let i = 0; i < n; i++) {
        let total = 0;
        for (let j = i; j < n; j++) {
            total += nums[j];
            values.push(total);
        }
    }
    values.sort((a, b) => a - b);
    let sum = 0;
    for (let i = left - 1; i < right; i++)
        sum += values[i];
    return sum % 1000000007;
}
