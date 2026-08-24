// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    func longestSemiRepetitiveSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, left = 0, lastPair = -1
        for right in chars.indices {
            if right > 0 && chars[right] == chars[right - 1] {
                if lastPair >= left { left = lastPair + 1 }
                lastPair = right - 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
