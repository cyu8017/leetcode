// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    const n = bits.length;
    while (i < n - 1) i += bits[i] === 1 ? 2 : 1;
    return i === n - 1;
};
