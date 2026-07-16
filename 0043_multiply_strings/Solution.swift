// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

class Solution {
    func multiply(_ num1: String, _ num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0"
        }

        let num1Chars = Array(num1)
        let num2Chars = Array(num2)
        var positions = Array(repeating: 0, count: num1Chars.count + num2Chars.count)

        for i in stride(from: num1Chars.count - 1, through: 0, by: -1) {
            for j in stride(from: num2Chars.count - 1, through: 0, by: -1) {
                let product = Int(num1Chars[i].asciiValue! - 48) * Int(num2Chars[j].asciiValue! - 48)
                let low = i + j + 1
                let high = i + j
                let total = product + positions[low]
                positions[low] = total % 10
                positions[high] += total / 10
            }
        }

        var start = 0
        while start < positions.count && positions[start] == 0 {
            start += 1
        }

        if start == positions.count {
            return "0"
        }

        return positions[start...].map(String.init).joined()
    }
}
