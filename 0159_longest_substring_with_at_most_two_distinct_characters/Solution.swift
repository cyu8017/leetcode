// LeetCode 0159 - Longest Substring with At Most Two Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution {
    func lengthOfLongestSubstringTwoDistinct(_ s: String) -> Int {
        let characters = Array(s)
        var counts: [Character: Int] = [:]
        var left = 0
        var best = 0
        for right in characters.indices {
            counts[characters[right], default: 0] += 1
            while counts.count > 2 {
                let character = characters[left]
                counts[character]! -= 1
                if counts[character] == 0 {
                    counts[character] = nil
                }
                left += 1
            }
            best = max(best, right - left + 1)
        }
        return best
    }
}