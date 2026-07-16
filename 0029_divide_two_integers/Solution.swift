// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

class Solution {
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        if dividend == Int32.min && divisor == -1 {
            return Int32.max
        }

        let negative = (dividend < 0) != (divisor < 0)
        var a = abs(Int64(dividend))
        var b = abs(Int64(divisor))
        var quotient: Int64 = 0

        for i in stride(from: 31, through: 0, by: -1) {
            if (a >> i) >= b {
                quotient += 1 << i
                a -= b << i
            }
        }

        return negative ? Int(-quotient) : Int(quotient)
    }
}
