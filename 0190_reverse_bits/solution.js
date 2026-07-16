// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

/**
 * @param {number} n
 * @return {number}
 */
var reverseBits = function(n) {
    let result = 0;
    for (let bit = 0; bit < 32; bit++) {
        result = (result << 1) | (n & 1);
        n >>>= 1;
    }
    return result >>> 0;
};