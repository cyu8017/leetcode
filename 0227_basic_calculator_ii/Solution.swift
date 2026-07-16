// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

class Solution {
    func calculate(_ s: String) -> Int {
        var stack: [Int] = []
        var number = 0
        var operator: Character = "+"

        for (index, ch) in s.enumerated() {
            if ch.isNumber {
                number = number * 10 + Int(ch.wholeNumberValue!)
            }
            if ch == "+" || ch == "-" || ch == "*" || ch == "/" || index == s.count - 1 {
                switch operator {
                case "+":
                    stack.append(number)
                case "-":
                    stack.append(-number)
                case "*":
                    stack[stack.count - 1] = stack.removeLast() * number
                case "/":
                    stack[stack.count - 1] = stack.removeLast() / number
                default:
                    break
                }
                operator = ch
                number = 0
            }
        }

        return stack.reduce(0, +)
    }
}
