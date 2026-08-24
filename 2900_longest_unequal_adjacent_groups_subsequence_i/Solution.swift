// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution {
    func getLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        var ans = [words[0]]
        var last = groups[0]
        for i in 1..<words.count where groups[i] != last {
            ans.append(words[i])
            last = groups[i]
        }
        return ans
    }
}
