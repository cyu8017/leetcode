// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution {
    func hasTrailingZeros(_ nums: [Int]) -> Bool {
        var even = 0
        for v in nums where v % 2 == 0 {
            even += 1
            if even >= 2 { return true }
        }
        return false
    }
}
