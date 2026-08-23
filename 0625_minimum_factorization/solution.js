// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

/**
 * @param {number} num
 * @return {number}
 */
var smallestFactorization = function(num) {
    if (num < 10) return num;
    const digits = [];
    for (let digit = 9; digit >= 2; --digit) {
        while (num % digit === 0) {
            digits.push(digit);
            num = Math.floor(num / digit);
        }
    }
    if (num !== 1) return 0;
    let result = 0;
    for (let i = digits.length - 1; i >= 0; --i) {
        result = result * 10 + digits[i];
        if (result > 2147483647) return 0;
    }
    return result;
};
