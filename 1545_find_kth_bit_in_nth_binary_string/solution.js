// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    let invert = false;
    let length = (1 << n) - 1;
    while (k !== 1) {
        const middle = Math.floor(length / 2) + 1;
        if (k === middle) return invert ? "0" : "1";
        if (k > middle) {
            k = length - k + 1;
            invert = !invert;
        }
        length = Math.floor(length / 2);
    }
    return invert ? "1" : "0";
};
