// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

class Solution {
    func monotoneIncreasingDigits(_ n: Int) -> Int {
        var digits = Array(String(n))
        var mark = digits.count
        for i in stride(from: digits.count - 1, through: 1, by: -1) {
            if digits[i] < digits[i - 1] {
                digits[i - 1] = Character(String(Int(String(digits[i - 1]))! - 1))
                mark = i
            }
        }
        if mark < digits.count {
            for i in mark..<digits.count { digits[i] = "9" }
        }
        return Int(String(digits))!
    }
}
