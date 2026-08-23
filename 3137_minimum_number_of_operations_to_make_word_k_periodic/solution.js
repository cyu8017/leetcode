// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumOperationsToMakeKPeriodic = function(word, k) {
    const cnt = new Map();
    const n = word.length;
    let mx = 0;
    for (let i = 0; i < n; i += k) {
        const s = word.substring(i, i + k);
        const v = (cnt.get(s) || 0) + 1;
        cnt.set(s, v);
        mx = Math.max(mx, v);
    }
    return Math.floor(n / k) - mx;
};
