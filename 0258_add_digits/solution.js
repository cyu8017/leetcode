// LeetCode 0258 - Add Digits
// https://leetcode.com/problems/add-digits/

/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if (num === 0) {
        return 0;
    }
    return 1 + (num - 1) % 9;
};
