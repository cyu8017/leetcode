// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution {
    func lengthOfLongestSubstringKDistinct(_ s: String, _ k: Int) -> Int {
        if k == 0 {
            return 0
        }

        var counts: [Character: Int] = [:]
        var left = 0
        var best = 0
        let chars = Array(s)

        for right in 0..<chars.count {
            counts[chars[right], default: 0] += 1
            while counts.count > k {
                counts[chars[left], default: 0] -= 1
                if counts[chars[left]] == 0 {
                    counts.removeValue(forKey: chars[left])
                }
                left += 1
            }
            best = max(best, right - left + 1)
        }

        return best
    }
}
