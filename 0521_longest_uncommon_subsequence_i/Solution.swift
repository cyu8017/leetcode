// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution {
    func findLUSlength(_ a: String, _ b: String) -> Int {
        return a != b ? max(a.count, b.count) : -1
    }
}
