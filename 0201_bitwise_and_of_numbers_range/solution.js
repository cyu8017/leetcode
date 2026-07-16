// LeetCode 0201 - Bitwise AND of Numbers Range
// https://leetcode.com/problems/bitwise-and-of-numbers-range/

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function(left, right) {
    let shift = 0;
    while (left < right) {
        left >>= 1;
        right >>= 1;
        shift += 1;
    }
    return left << shift;
};