// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

class Solution {
    func sequentialDigits(_ low: Int, _ high: Int) -> [Int] {
        let digits = "123456789"
        var ans: [Int] = []
        for length in 2...9 {
            for start in 0...(9 - length) {
                let s = String(digits[digits.index(digits.startIndex, offsetBy: start)..<digits.index(digits.startIndex, offsetBy: start + length)])
                let num = Int(s)!
                if num >= low && num <= high { ans.append(num) }
            }
        }
        return ans
    }
}
