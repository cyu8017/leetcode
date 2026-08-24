// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution {
    fun hasTrailingZeros(nums: IntArray): Boolean {
        var even = 0
        for (v in nums) {
            if (v % 2 == 0) {
                even++
                if (even >= 2) return true
            }
        }
        return false
    }
}
