"use strict";
// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/
function maximumWealth(accounts) {
    return Math.max(...accounts.map((row) => row.reduce((a, b) => a + b, 0)));
}
