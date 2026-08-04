// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {boolean}
 */
var isPrefixString = function(s, words) {
    let cur = "";
    for (const w of words) {
        cur += w;
        if (cur === s) return true;
        if (cur.length > s.length || !s.startsWith(cur)) return false;
    }
    return false;
};
