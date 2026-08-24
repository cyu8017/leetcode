// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

class Solution {
    func evenNumberBitwiseORs(_ nums: [Int]) -> Int {
        var ans = 0
        for x in nums where x % 2 == 0 { ans |= x }
        return ans
    }
}
