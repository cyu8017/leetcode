// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
    func myAtoi(_ s: String) -> Int {
        let chars = Array(s)
        var i = 0
        while i < chars.count && chars[i] == " " {
            i += 1
        }
        if i >= chars.count {
            return 0
        }

        var sign = 1
        if chars[i] == "-" {
            sign = -1
            i += 1
        } else if chars[i] == "+" {
            i += 1
        }

        var result = 0
        while i < chars.count, let digit = chars[i].wholeNumberValue {
            if result > (Int32.max - digit) / 10 {
                return sign == -1 ? Int(Int32.min) : Int(Int32.max)
            }
            result = result * 10 + digit
            i += 1
        }

        return sign * result
    }
}
