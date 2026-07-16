// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

class Solution {
    func calculate(_ s: String) -> Int {
        var stack = [Int]()
        var result = 0
        var number = 0
        var sign = 1
        for char in s {
            if char >= "0" && char <= "9" {
                number = number * 10 + Int(char.unicodeScalars.first!.value - 48)
            } else if char == "+" || char == "-" {
                result += sign * number
                number = 0
                sign = char == "+" ? 1 : -1
            } else if char == "(" {
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            } else if char == ")" {
                result += sign * number
                number = 0
                result *= stack.removeLast()
                result += stack.removeLast()
            }
        }
        result += sign * number
        return result
    }
}
