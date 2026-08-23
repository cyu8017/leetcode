// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getLongestSubsequence = function(words, groups) {
    const ans = [words[0]];
    let last = groups[0];
    for (let i = 1; i < words.length; i++) {
        if (groups[i] !== last) {
            ans.push(words[i]);
            last = groups[i];
        }
    }
    return ans;
};
