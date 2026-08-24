// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    let ans = 0;
    for (const x of nums) if (x < k) ans++;
    return ans;
};
