// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

class Solution {
    func isUgly(_ n: Int) -> Bool {
        var value = n
        if value <= 0 {
            return false
        }
        for factor in [2, 3, 5] {
            while value % factor == 0 {
                value /= factor
            }
        }
        return value == 1
    }
}
