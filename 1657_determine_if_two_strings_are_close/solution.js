// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) return false;
    const count = (s) => {
        const c = Array(26).fill(0);
        for (const ch of s) c[ch.charCodeAt(0) - 97]++;
        return c;
    };
    const a = count(word1), b = count(word2);
    for (let i = 0; i < 26; i++) {
        if ((a[i] === 0) !== (b[i] === 0)) return false;
    }
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);
    return a.every((v, i) => v === b[i]);
};
