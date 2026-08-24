// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

class Solution {
    func numDecodings(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        var prev2 = 1
        var prev1 = one(chars[0])
        if chars.count >= 2 {
            for i in 1..<chars.count {
                let cur = (one(chars[i]) * prev1 + two(chars[i - 1], chars[i]) * prev2) % mod
                prev2 = prev1
                prev1 = cur
            }
        }
        return prev1
    }

    private func one(_ ch: Character) -> Int {
        if ch == "*" { return 9 }
        if ch == "0" { return 0 }
        return 1
    }

    private func two(_ a: Character, _ b: Character) -> Int {
        if a == "*" && b == "*" { return 15 }
        if a == "*" { return b <= "6" ? 2 : 1 }
        if b == "*" {
            if a == "1" { return 9 }
            if a == "2" { return 6 }
            return 0
        }
        let value = Int(String(a))! * 10 + Int(String(b))!
        return value >= 10 && value <= 26 ? 1 : 0
    }
}
