// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    const x = n ^ (n >>> 1);
    return (x & (x + 1)) === 0;
};
