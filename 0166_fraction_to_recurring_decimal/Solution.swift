// LeetCode 0166 - Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution {
    func fractionToDecimal(_ numerator: Int, _ denominator: Int) -> String {
        if numerator == 0 { return "0" }
        let sign = (numerator < 0) != (denominator < 0) ? "-" : ""
        let dividend = abs(numerator)
        let divisor = abs(denominator)
        let integer = dividend / divisor
        var remainder = dividend % divisor
        if remainder == 0 { return sign + String(integer) }

        var parts = [sign + String(integer), "."]
        var seen = [Int: Int]()
        while remainder != 0 {
            if let index = seen[remainder] {
                parts.insert("(", at: index)
                parts.append(")")
                break
            }
            seen[remainder] = parts.count
            remainder *= 10
            parts.append(String(remainder / divisor))
            remainder %= divisor
        }
        return parts.joined()
    }
}