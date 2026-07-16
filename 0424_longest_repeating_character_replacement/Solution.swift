// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution {
    func characterReplacement(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        var counts: [Character: Int] = [:]
        var left = 0
        var best = 0
        var maxCount = 0

        for right in chars.indices {
            counts[chars[right], default: 0] += 1
            maxCount = max(maxCount, counts[chars[right]]!)
            while (right - left + 1) - maxCount > k {
                counts[chars[left], default: 0] -= 1
                left += 1
            }
            best = max(best, right - left + 1)
        }

        return best
    }
}
