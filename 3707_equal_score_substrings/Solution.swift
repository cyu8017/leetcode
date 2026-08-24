// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

class Solution {
    func scoreBalance(_ s: String) -> Bool {
        let chars = Array(s)
        var l = 0, r = 0
        for c in chars { r += Int(c.asciiValue! - 96) }
        if chars.count > 1 {
            for i in 0..<(chars.count - 1) {
                let x = Int(chars[i].asciiValue! - 96)
                l += x
                r -= x
                if l == r { return true }
            }
        }
        return false
    }
}
