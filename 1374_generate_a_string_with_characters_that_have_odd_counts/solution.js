// LeetCode 1374 - Generate A String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    return n % 2 ? "a".repeat(n) : "a".repeat(n - 1) + "b";
};
