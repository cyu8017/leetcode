// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

class Solution {
    func convertToBase7(_ num: Int) -> String {
        if num == 0 {
            return "0"
        }
        let negative = num < 0
        var value = abs(num)
        var digits: [String] = []
        while value > 0 {
            digits.append(String(value % 7))
            value /= 7
        }
        let result = digits.reversed().joined()
        return negative ? "-\(result)" : result
    }
}
