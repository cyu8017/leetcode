// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    return Math.max(...[...n].map(Number));
};
