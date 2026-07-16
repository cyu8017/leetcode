// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var last = [Character: Int]()
        var best = 0
        var start = 0
        let chars = Array(s)

        for i in chars.indices {
            let ch = chars[i]
            if let prev = last[ch], prev >= start {
                start = prev + 1
            }
            last[ch] = i
            best = max(best, i - start + 1)
        }

        return best
    }
}
