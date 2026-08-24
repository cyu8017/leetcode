// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
    func alternateDigitSum(_ n: Int) -> Int {
        var digits = [Int]()
        var x = n
        while x > 0 {
            digits.append(x % 10)
            x /= 10
        }
        var ans = 0, sign = 1
        for i in stride(from: digits.count - 1, through: 0, by: -1) {
            ans += sign * digits[i]
            sign = -sign
        }
        return ans
    }
}
