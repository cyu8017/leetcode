// LeetCode 0400 - Nth Digit
// https://leetcode.com/problems/nth-digit/

class Solution {
    func findNthDigit(_ n: Int) -> Int {
        var position = n
        var digits = 1
        var count = 9
        var start = 1

        while position > digits * count {
            position -= digits * count
            digits += 1
            count *= 10
            start *= 10
        }

        let number = start + (position - 1) / digits
        let numberString = String(number)
        let index = numberString.index(numberString.startIndex, offsetBy: (position - 1) % digits)
        return Int(String(numberString[index]))!
    }
}
