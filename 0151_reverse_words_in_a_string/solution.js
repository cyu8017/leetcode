// LeetCode 0151 - Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

/**
 * Reverses the order of words, collapsing excess whitespace.
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.trim().split(/\s+/).reverse().join(" ");
};