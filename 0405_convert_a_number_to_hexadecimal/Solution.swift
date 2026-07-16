// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution {
    func toHex(_ num: Int) -> String {
        if num == 0 {
            return "0"
        }

        let digits = Array("0123456789abcdef")
        var value = UInt32(truncatingIfNeeded: num)
        var result: [Character] = []

        while value != 0 {
            result.append(digits[Int(value & 15)])
            value >>= 4
        }

        return String(result.reversed())
    }
}
