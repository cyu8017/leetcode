// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var canBeEqual = function(s1, s2) {
    const a = [s1[0], s1[2]].sort().join('');
    const b = [s2[0], s2[2]].sort().join('');
    const c = [s1[1], s1[3]].sort().join('');
    const d = [s2[1], s2[3]].sort().join('');
    return a === b && c === d;
};
