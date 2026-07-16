// LeetCode 0163 - Missing Ranges
// https://leetcode.com/problems/missing-ranges/

/**
 * Returns inclusive ranges missing from the supplied bounds.
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number[][]}
 */
var findMissingRanges = function(nums, lower, upper) {
    const result = [];
    let previous = lower - 1;

    for (const number of [...nums, upper + 1]) {
        if (number - previous >= 2) {
            result.push([previous + 1, number - 1]);
        }
        previous = number;
    }
    return result;
};