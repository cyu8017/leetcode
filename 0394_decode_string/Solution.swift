// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

class Solution {
    func decodeString(_ s: String) -> String {
        var stack: [(String, Int)] = []
        var current = ""
        var number = 0

        for char in s {
            if char >= "0" && char <= "9" {
                number = number * 10 + Int(String(char))!
            } else if char == "[" {
                stack.append((current, number))
                current = ""
                number = 0
            } else if char == "]" {
                let (previous, count) = stack.removeLast()
                current = previous + String(repeating: current, count: count)
            } else {
                current.append(char)
            }
        }

        return current
    }
}
