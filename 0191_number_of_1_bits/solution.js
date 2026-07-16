// LeetCode 0191 - Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let count = 0;
    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
};