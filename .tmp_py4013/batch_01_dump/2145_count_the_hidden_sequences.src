// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

/**
 * @param {number[]} differences
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var numberOfArrays = function(differences, lower, upper) {
    let cur = 0, mn = 0, mx = 0;
    for (const d of differences) {
        cur += d;
        mn = Math.min(mn, cur);
        mx = Math.max(mx, cur);
    }
    const res = (upper - lower) - (mx - mn) + 1;
    return res < 0 ? 0 : res;
};
