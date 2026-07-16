// LeetCode 0161 - One Edit Distance
// https://leetcode.com/problems/one-edit-distance/

/**
 * Determines whether exactly one edit transforms one string into another.
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isOneEditDistance = function(s, t) {
    if (Math.abs(s.length - t.length) > 1 || s === t) {
        return false;
    }
    if (s.length > t.length) {
        [s, t] = [t, s];
    }

    let index = 0;
    while (index < s.length && s[index] === t[index]) {
        index++;
    }
    return s.length === t.length
        ? s.slice(index + 1) === t.slice(index + 1)
        : s.slice(index) === t.slice(index + 1);
};