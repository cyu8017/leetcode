// LeetCode 1716 - Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    const weeks = Math.floor(n / 7);
    const days = n % 7;
    return weeks * 28 + 7 * weeks * (weeks - 1) / 2 + days * (weeks + 1) + days * (days - 1) / 2;
};
