// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    fun uniformArray(nums1: IntArray): Boolean {
        var mn = Int.MAX_VALUE
        for (x in nums1) {
            if (x % 2 == 1 && x < mn) mn = x
        }
        for (x in nums1) {
            if (x % 2 == 0 && mn != Int.MAX_VALUE && x < mn) return false
        }
        return true
    }
}
