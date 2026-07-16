// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution {
    func diffWaysToCompute(_ expression: String) -> [Int] {
        if expression.allSatisfy({ $0.isNumber }) {
            return [Int(expression)!]
        }
        var result: [Int] = []
        var index = expression.startIndex
        while index < expression.endIndex {
            let operatorChar = expression[index]
            if operatorChar == "+" || operatorChar == "-" || operatorChar == "*" {
                let left = diffWaysToCompute(String(expression[..<index]))
                let next = expression.index(after: index)
                let right = diffWaysToCompute(String(expression[next...]))
                for leftValue in left {
                    for rightValue in right {
                        switch operatorChar {
                        case "+":
                            result.append(leftValue + rightValue)
                        case "-":
                            result.append(leftValue - rightValue)
                        default:
                            result.append(leftValue * rightValue)
                        }
                    }
                }
            }
            index = expression.index(after: index)
        }
        return result
    }
}
