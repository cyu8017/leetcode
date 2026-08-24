// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

/**
 * @param {string[]} words
 * @param {string} s
 * @return {number}
 */
var countPrefixes = function(words, s) {
    let ans = 0;
    for (const w of words)
        if (w.length <= s.length && s.startsWith(w)) ans++;
    return ans;
};
