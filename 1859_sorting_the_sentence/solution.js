// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    const tokens = s.split(" ");
    const ordered = new Array(tokens.length);
    for (const token of tokens) {
        ordered[Number(token[token.length - 1]) - 1] = token.slice(0, -1);
    }
    return ordered.join(" ");
};
