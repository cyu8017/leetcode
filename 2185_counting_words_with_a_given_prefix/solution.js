// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    let ans = 0;
    for (const w of words)
        if (w.length >= pref.length && w.startsWith(pref)) ans++;
    return ans;
};
