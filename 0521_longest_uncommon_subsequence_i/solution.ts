// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

export class Solution {
    findLUSlength(a: string, b: string): number {
        return a !== b ? Math.max(a.length, b.length) : -1;
    }
}
