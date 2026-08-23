// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const seen = new Set();
    for (const x of nums) if (x > 0) seen.add(x);
    return seen.size;
};
