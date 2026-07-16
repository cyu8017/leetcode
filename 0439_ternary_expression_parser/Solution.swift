// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

class Solution {
    func parseTernary(_ expression: String) -> String {
        if !expression.contains("?") {
            return expression
        }

        let chars = Array(expression)
        var separator = 2
        var depth = 0
        for index in 2..<chars.count {
            switch chars[index] {
            case "?":
                depth += 1
            case ":":
                if depth == 0 {
                    separator = index
                    if chars[0] == "T" {
                        return parseTernary(String(chars[2..<separator]))
                    }
                    return parseTernary(String(chars[(separator + 1)...]))
                }
                depth -= 1
            default:
                break
            }
        }

        if chars[0] == "T" {
            return parseTernary(String(chars[2..<separator]))
        }
        return parseTernary(String(chars[(separator + 1)...]))
    }
}
