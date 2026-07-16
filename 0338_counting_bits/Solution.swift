// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

class Solution {
    func countBits(_ n: Int) -> [Int] {
        var result = Array(repeating: 0, count: n + 1)
        if n == 0 {
            return result
        }
        for index in 1...n {
            result[index] = result[index & (index - 1)] + 1
        }
        return result
    }
}
