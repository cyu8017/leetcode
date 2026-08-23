// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if (dividend === -2147483648 && divisor === -1) {
        return 2147483647;
    }

    const negative = (dividend < 0) ^ (divisor < 0);
    let a = Math.abs(dividend);
    let b = Math.abs(divisor);

    let quotient = 0;
    for (let i = 31; i >= 0; i--) {
        if ((a >> i) >= b) {
            quotient += 1 << i;
            a -= b << i;
        }
    }

    return negative ? -quotient : quotient;
};
