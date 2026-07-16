// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n === 0) {
        return 1.0;
    }

    let exp = n;
    if (exp < 0) {
        x = 1.0 / x;
        exp = -exp;
    }

    let result = 1.0;
    let current = x;

    while (exp) {
        if (exp & 1) {
            result *= current;
        }
        current *= current;
        exp >>= 1;
    }

    return result;
};
