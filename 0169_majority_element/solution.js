// LeetCode 0169 - Majority Element
// https://leetcode.com/problems/majority-element/

/**
 * Finds the majority value with Boyer-Moore voting.
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candidate;
    let count = 0;

    for (const number of nums) {
        if (count === 0) {
            candidate = number;
        }
        count += number === candidate ? 1 : -1;
    }
    return candidate;
};