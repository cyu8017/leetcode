// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

/**
 * @param {number} n
 * @return {number}
 */
var monotoneIncreasingDigits = function(n) {
    const digits = String(n).split('');
    let mark = digits.length;
    for (let i = digits.length - 1; i > 0; i--) {
        if (digits[i] < digits[i - 1]) {
            digits[i - 1] = String.fromCharCode(digits[i - 1].charCodeAt(0) - 1);
            mark = i;
        }
    }
    for (let i = mark; i < digits.length; i++) digits[i] = '9';
    return parseInt(digits.join(''), 10);
};
