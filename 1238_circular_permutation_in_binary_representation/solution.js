// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

/**
 * @param {number} n
 * @param {number} start
 * @return {number[]}
 */
var circularPermutation = function(n, start) {
    const limit = 1 << n;
    const answer = [];
    for (let i = 0; i < limit; i++) {
        answer.push(start ^ i ^ (i >> 1));
    }
    return answer;
};
