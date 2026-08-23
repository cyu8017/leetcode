// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

/**
 * @param {number[]} amount
 * @return {number}
 */
var fillCups = function(amount) {
    let a = amount[0], b = amount[1], c = amount[2];
    if (a < b) { const t = a; a = b; b = t; }
    if (a < c) { const t = a; a = c; c = t; }
    if (b < c) { const t = b; b = c; c = t; }
    if (a >= b + c) return a;
    return Math.floor((a + b + c + 1) / 2);
};
