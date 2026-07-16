// LeetCode 0357 - Count Numbers with Unique Digits
// https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution {
    func countNumbersWithUniqueDigits(_ n: Int) -> Int {
        if n == 0 {
            return 1
        }

        var total = 10
        var unique = 9
        var available = 9

        if n >= 2 {
            for _ in 2...n {
                unique *= available
                available -= 1
                total += unique
            }
        }

        return total
    }
}
