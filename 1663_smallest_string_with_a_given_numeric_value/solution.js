// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function(n, k) {
    const a = Array(n).fill("a");
    k -= n;
    for (let i = n - 1; i >= 0; i--) {
        const d = Math.min(25, k);
        a[i] = String.fromCharCode(97 + d);
        k -= d;
    }
    return a.join("");
};
