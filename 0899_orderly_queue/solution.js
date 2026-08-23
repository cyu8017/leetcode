// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var orderlyQueue = function(s, k) {
    if (k > 1) return s.split("").sort().join("");
    let best = s;
    for (let i = 1; i < s.length; i++) {
        const cand = s.slice(i) + s.slice(0, i);
        if (cand < best) best = cand;
    }
    return best;
};
