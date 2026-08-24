// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution {
    func validSubstringCount(_ word1: String, _ word2: String) -> Int {
        let w1 = Array(word1)
        var need = Array(repeating: 0, count: 26)
        var required = 0
        for c in word2 {
            let i = Int(c.asciiValue! - 97)
            if need[i] == 0 { required += 1 }
            need[i] += 1
        }
        var have = Array(repeating: 0, count: 26)
        var formed = 0
        var ans = 0
        var l = 0
        for r in 0..<w1.count {
            let c = Int(w1[r].asciiValue! - 97)
            have[c] += 1
            if have[c] == need[c] && need[c] > 0 { formed += 1 }
            while formed == required && l <= r {
                ans += w1.count - r
                let c2 = Int(w1[l].asciiValue! - 97)
                if have[c2] == need[c2] && need[c2] > 0 { formed -= 1 }
                have[c2] -= 1
                l += 1
            }
        }
        return ans
    }
}
