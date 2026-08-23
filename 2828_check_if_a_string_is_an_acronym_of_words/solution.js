// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    if (words.length !== s.length) return false;
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (!w.length || w[0] !== s[i]) return false;
    }
    return true;
};
