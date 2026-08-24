// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

class Solution {
    func solveEquation(_ equation: String) -> String {
        let eq = equation.firstIndex(of: "=")!
        let left = parse(String(equation[..<eq]))
        let right = parse(String(equation[equation.index(after: eq)...]))
        let coef = left[0] - right[0]
        let constant = right[1] - left[1]
        if coef == 0 { return constant == 0 ? "Infinite solutions" : "No solution" }
        return "x=\(constant / coef)"
    }

    private func parse(_ expr: String) -> [Int] {
        let chars = Array(expr)
        var coef = 0
        var constant = 0
        var i = 0
        while i < chars.count {
            var sign = 1
            if chars[i] == "+" || chars[i] == "-" {
                sign = chars[i] == "-" ? -1 : 1
                i += 1
            }
            var value = 0
            var hasDigit = false
            while i < chars.count && chars[i] >= "0" && chars[i] <= "9" {
                hasDigit = true
                value = value * 10 + Int(String(chars[i]))!
                i += 1
            }
            if i < chars.count && chars[i] == "x" {
                coef += sign * (hasDigit ? value : 1)
                i += 1
            } else {
                constant += sign * value
            }
        }
        return [coef, constant]
    }
}
