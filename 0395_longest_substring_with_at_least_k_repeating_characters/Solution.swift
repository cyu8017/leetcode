// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution {
    func longestSubstring(_ s: String, _ k: Int) -> Int {
        if s.isEmpty {
            return 0
        }

        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        for (char, count) in counts where count < k {
            let parts = s.split(separator: char, omittingEmptySubsequences: false)
            return parts.map { longestSubstring(String($0), k) }.max() ?? 0
        }

        return s.count
    }
}
