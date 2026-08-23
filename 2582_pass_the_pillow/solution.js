// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
    const cycle = 2 * (n - 1);
    const t = time % cycle;
    if (t < n) return 1 + t;
    return n - (t - (n - 1));
};
