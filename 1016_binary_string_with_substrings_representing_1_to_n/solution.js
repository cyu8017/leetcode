// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

/**
 * @param {string} s
 * @param {number} n
 * @return {boolean}
 */
var queryString = function(s, n) {
    for (let i = n; i > Math.floor(n / 2); i--) {
        if (!s.includes(i.toString(2))) return false;
    }
    return true;
};
