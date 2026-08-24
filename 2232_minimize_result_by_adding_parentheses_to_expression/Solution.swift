// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution {
    func minimizeResult(_ expression: String) -> String {
        let plus = expression.firstIndex(of: "+")!
        let left = String(expression[..<plus])
        let right = String(expression[expression.index(after: plus)...])
        var bestVal = Int.max
        var best = ""
        for i in 0..<left.count {
            for j in 1...right.count {
                let a = String(left.prefix(i))
                let b = String(left.dropFirst(i))
                let c = String(right.prefix(j))
                let d = String(right.dropFirst(j))
                var val = Int(b)! + Int(c)!
                if !a.isEmpty { val *= Int(a)! }
                if !d.isEmpty { val *= Int(d)! }
                if val < bestVal {
                    bestVal = val
                    best = a + "(" + b + "+" + c + ")" + d
                }
            }
        }
        return best
    }
}
