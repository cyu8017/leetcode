// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
    func validDigit(_ n: Int, _ x: Int) -> Bool {
        var n = n
        var hasX = false
        while n > 9 {
            hasX = hasX || (n % 10 == x)
            n /= 10
        }
        return hasX && (n != x)
    }
}
