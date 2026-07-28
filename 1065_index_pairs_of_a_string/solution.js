// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

/**
 * @param {string} text
 * @param {string[]} words
 * @return {number[][]}
 */
var indexPairs = function(text, words) {
    const wordSet = new Set(words);
    const ans = [];
    const n = text.length;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            if (wordSet.has(text.slice(i, j + 1))) ans.push([i, j]);
        }
    }
    return ans;
};
