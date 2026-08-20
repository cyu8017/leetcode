// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

class Solution {
    func largestOddNumber(_ num: String) -> String {
        let chars = Array(num)
        for i in stride(from: chars.count - 1, through: 0, by: -1) {
            if let d = chars[i].wholeNumberValue, d % 2 == 1 {
                return String(chars[0...i])
            }
        }
        return ""
    }
}
