// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    return Math.max(...accounts.map((row) => row.reduce((a, b) => a + b, 0)));
};
