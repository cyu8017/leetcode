// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    const neg = n[0] === "-";
    const start = neg ? 1 : 0;
    for (let i = start; i < n.length; i++) {
        const d = Number(n[i]);
        if (neg) {
            if (d > x) return n.slice(0, i) + String(x) + n.slice(i);
        } else if (d < x) {
            return n.slice(0, i) + String(x) + n.slice(i);
        }
    }
    return n + String(x);
};
