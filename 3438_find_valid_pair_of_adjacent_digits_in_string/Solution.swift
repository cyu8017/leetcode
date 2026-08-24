// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution {
    func findValidPair(_ s: String) -> String {
        let chars = Array(s)
        var freq = Array(repeating: 0, count: 10)
        for c in chars { freq[Int(c.asciiValue! - 48)] += 1 }
        if chars.count >= 2 {
            for i in 0..<(chars.count - 1) {
                let a = Int(chars[i].asciiValue! - 48)
                let b = Int(chars[i + 1].asciiValue! - 48)
                if a != b && freq[a] == a && freq[b] == b { return String(chars[i...i+1]) }
            }
        }
        return ""
    }
}
