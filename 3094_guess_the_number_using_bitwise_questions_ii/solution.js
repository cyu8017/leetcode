// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

/**
 * Definition of commonBits API.
 * @param {number} num
 * @return {number}
 * function commonBits(num) {}
 */
/**
 * @return {number}
 */
var findNumber = function() {
    let n = 0;
    for (let i = 0; i < 32; i++) {
        const count1 = commonBits(1 << i);
        const count2 = commonBits(1 << i);
        if (count1 > count2) n |= 1 << i;
    }
    return n;
};
