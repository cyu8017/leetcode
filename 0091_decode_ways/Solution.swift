// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

class Solution {
    func numDecodings(_ s: String) -> Int {
        let chars = Array(s)
        if chars.isEmpty || chars[0] == "0" {
            return 0
        }

        var prev2 = 1
        var prev1 = 1

        for i in 1..<chars.count {
            var current = 0
            if chars[i] != "0" {
                current += prev1
            }
            let two = Int(String(chars[i - 1...i]))!
            if two >= 10 && two <= 26 {
                current += prev2
            }
            prev2 = prev1
            prev1 = current
        }

        return prev1
    }
}
