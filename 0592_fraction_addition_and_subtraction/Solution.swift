// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution {
    func fractionAddition(_ expression: String) -> String {
        let chars = Array(expression)
        var numerator = 0
        var denominator = 1
        var i = 0
        let len = chars.count
        while i < len {
            var sign = 1
            if chars[i] == "+" || chars[i] == "-" {
                if chars[i] == "-" { sign = -1 }
                i += 1
            }
            var a = 0
            while i < len && chars[i] >= "0" && chars[i] <= "9" {
                a = a * 10 + Int(String(chars[i]))!
                i += 1
            }
            a *= sign
            i += 1
            var b = 0
            while i < len && chars[i] >= "0" && chars[i] <= "9" {
                b = b * 10 + Int(String(chars[i]))!
                i += 1
            }
            numerator = numerator * b + a * denominator
            denominator *= b
            let g = gcd(abs(numerator), abs(denominator))
            numerator /= g
            denominator /= g
        }
        return "\(numerator)/\(denominator)"
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
