// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let i = 0;
    let j = 0;
    const out = [];
    while (i < word1.length || j < word2.length) {
        if (i < word1.length) {
            out.push(word1[i]);
            i++;
        }
        if (j < word2.length) {
            out.push(word2[j]);
            j++;
        }
    }
    return out.join("");
};
