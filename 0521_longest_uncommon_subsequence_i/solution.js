// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution {
    findLUSlength(a, b) {
        return a !== b ? Math.max(a.length, b.length) : -1;
    }
}

module.exports = { Solution };
