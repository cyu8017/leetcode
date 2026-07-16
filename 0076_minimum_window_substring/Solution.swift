// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
        if t.isEmpty {
            return ""
        }

        var need: [Character: Int] = [:]
        for ch in t {
            need[ch, default: 0] += 1
        }

        let required = need.count
        var formed = 0
        var window: [Character: Int] = [:]
        let chars = Array(s)
        var left = 0
        var bestLen = Int.max
        var bestLeft = 0

        for right in 0..<chars.count {
            let ch = chars[right]
            window[ch, default: 0] += 1
            if let count = need[ch], window[ch] == count {
                formed += 1
            }

            while formed == required {
                if right - left + 1 < bestLen {
                    bestLen = right - left + 1
                    bestLeft = left
                }

                let leftCh = chars[left]
                window[leftCh, default: 0] -= 1
                if let count = need[leftCh], window[leftCh, default: 0] < count {
                    formed -= 1
                }
                left += 1
            }
        }

        if bestLen == Int.max {
            return ""
        }

        return String(chars[bestLeft..<(bestLeft + bestLen)])
    }
}
