// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    const parts = nums.map(String);
    parts.sort((a, b) => (b + a).localeCompare(a + b));
    return parts[0] === "0" ? "0" : parts.join("");
};