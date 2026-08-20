// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution {
    func parseBoolExpr(_ expression: String) -> Bool {
        var stack: [Character] = []
        for ch in expression {
            if ch == ")" {
                var values: [Bool] = []
                while let last = stack.last, !"&|!".contains(last) {
                    let token = stack.removeLast()
                    if token == "t" || token == "f" {
                        values.append(token == "t")
                    }
                }
                let op = stack.removeLast()
                if op == "!" {
                    stack.append(values[0] ? "f" : "t")
                } else if op == "&" {
                    stack.append(values.allSatisfy { $0 } ? "t" : "f")
                } else {
                    stack.append(values.contains(true) ? "t" : "f")
                }
            } else if ch != "," {
                stack.append(ch)
            }
        }
        return stack.last == "t"
    }
}
