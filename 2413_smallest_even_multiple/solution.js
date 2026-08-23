// LeetCode 2413 - Smallest Even Multiple
// https://leetcode.com/problems/smallest-even-multiple/

/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
    return n % 2 === 0 ? n : n * 2;
};
