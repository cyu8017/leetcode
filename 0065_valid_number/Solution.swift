// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

class Solution {
    func isNumber(_ s: String) -> Bool {
        var seenDigit = false
        var seenDot = false
        var seenExp = false
        let chars = Array(s)

        for i in 0..<chars.count {
            let ch = chars[i]

            if ch >= "0" && ch <= "9" {
                seenDigit = true
            } else if ch == "+" || ch == "-" {
                if i > 0 && chars[i - 1] != "e" && chars[i - 1] != "E" {
                    return false
                }
            } else if ch == "e" || ch == "E" {
                if seenExp || !seenDigit {
                    return false
                }
                seenExp = true
                seenDigit = false
                seenDot = false
            } else if ch == "." {
                if seenDot || seenExp {
                    return false
                }
                seenDot = true
            } else {
                return false
            }
        }

        return seenDigit
    }
}
