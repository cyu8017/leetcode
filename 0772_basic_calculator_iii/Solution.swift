// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

class Solution {
    func calculate(_ s: String) -> Int {
        let expr = Array(s.filter { !$0.isWhitespace })
        var i = 0
        func parse() -> Int {
            var stack = [Int]()
            var num = 0
            var sign: Character = "+"
            while i < expr.count {
                let ch = expr[i]
                if ch.isNumber { num = num * 10 + Int(String(ch))! }
                else if ch == "(" {
                    i += 1
                    num = parse()
                }
                if (!ch.isNumber && ch != "(") || i == expr.count - 1 {
                    if ch == "+" || ch == "-" || ch == "*" || ch == "/" || ch == ")" || i == expr.count - 1 {
                        if sign == "+" { stack.append(num) }
                        else if sign == "-" { stack.append(-num) }
                        else if sign == "*" { stack[stack.count - 1] *= num }
                        else if sign == "/" {
                            let top = stack.removeLast()
                            stack.append(Int((Double(top) / Double(num)).rounded(.towardZero)))
                        }
                        if ch == ")" { return stack.reduce(0, +) }
                        sign = ch
                        num = 0
                    }
                }
                i += 1
            }
            return stack.reduce(0, +)
        }
        return parse()
    }
}
