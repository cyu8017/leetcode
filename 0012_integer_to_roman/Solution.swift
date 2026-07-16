// LeetCode 0012 - Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

class Solution {
    func intToRoman(_ num: Int) -> String {
        let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        let symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        var value = num
        var result = ""

        for i in values.indices {
            while value >= values[i] {
                result += symbols[i]
                value -= values[i]
            }
        }

        return result
    }
}
