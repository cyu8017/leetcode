// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    let s = String(n);
    const parts = [];
    while (s) {
        parts.push(s.slice(-3));
        s = s.slice(0, -3);
    }
    return parts.reverse().join(".");
};
