// LeetCode 0172 - Factorial Trailing Zeroes
// https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution {
    func trailingZeroes(_ n: Int) -> Int {
        var value = n
        var count = 0
        while value > 0 {
            value /= 5
            count += value
        }
        return count
    }
}