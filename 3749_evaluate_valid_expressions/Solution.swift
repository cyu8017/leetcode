// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

class Solution {
    private var expression = [Character]()

    func evaluateExpression(_ expression: String) -> Int {
        self.expression = Array(expression)
        return parse(0).0
    }

    private func parse(_ i: Int) -> (Int, Int) {
        let ch = expression[i]
        if ch.isNumber || ch == "-" {
            var j = i
            if expression[j] == "-" { j += 1 }
            while j < expression.count && expression[j].isNumber { j += 1 }
            let val = Int(String(expression[i..<j]))!
            return (val, j)
        }
        var j = i
        while expression[j] != "(" { j += 1 }
        let op = String(expression[i..<j])
        j += 1
        let p1 = parse(j)
        j = p1.1 + 1
        let p2 = parse(j)
        j = p2.1 + 1
        var res = 0
        if op == "add" { res = p1.0 + p2.0 }
        else if op == "sub" { res = p1.0 - p2.0 }
        else if op == "mul" { res = p1.0 * p2.0 }
        else if op == "div" { res = p1.0 / p2.0 }
        return (res, j)
    }
}
