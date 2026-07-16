// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    const result = [];
    const size = 1 << n;
    for (let i = 0; i < size; i++) {
        result.push(i ^ (i >> 1));
    }
    return result;
};
