// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const last = new Map();
    let best = 0;
    let start = 0;

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (last.has(ch) && last.get(ch) >= start) {
            start = last.get(ch) + 1;
        }
        last.set(ch, i);
        best = Math.max(best, i - start + 1);
    }

    return best;
};
