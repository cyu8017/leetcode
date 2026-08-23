// LeetCode 2745 - Construct the Longest New String
// https://leetcode.com/problems/construct-the-longest-new-string/

/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var longestString = function(x, y, z) {
    if (x < y) return (2 * x + 1 + z) * 2;
    if (y < x) return (2 * y + 1 + z) * 2;
    return (x + y + z) * 2;
};
