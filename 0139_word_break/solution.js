// LeetCode 0139 - Word Break
// https://leetcode.com/problems/word-break/

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const words = new Set(wordDict);
    const possible = Array(s.length + 1).fill(false);
    possible[0] = true;

    for (let end = 1; end <= s.length; end += 1) {
        for (let start = 0; start < end; start += 1) {
            if (possible[start] && words.has(s.slice(start, end))) {
                possible[end] = true;
                break;
            }
        }
    }

    return possible[s.length];
};