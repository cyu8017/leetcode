// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution {
    func longestValidSubstring(_ word: String, _ forbidden: [String]) -> Int {
        let forbid = Set(forbidden)
        let maxLen = forbidden.map(\.count).max() ?? 0
        let chars = Array(word)
        var ans = 0
        var right = chars.count - 1
        for left in stride(from: chars.count - 1, through: 0, by: -1) {
            var k = left
            while k <= right && k - left + 1 <= maxLen {
                if forbid.contains(String(chars[left...k])) {
                    right = k - 1
                    break
                }
                k += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
