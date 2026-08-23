// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function(word1, word2) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word1.length; i++) {
        freq[word1.charCodeAt(i) - 97]++;
        freq[word2.charCodeAt(i) - 97]--;
    }
    for (const v of freq) if (v > 3 || v < -3) return false;
    return true;
};
