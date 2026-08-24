// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    fun isIdealPermutation(nums: IntArray): Boolean {
        for (i in 0 until nums.size) {
            if (kotlin.math.abs(nums[i] - i) > 1) return false
        }
        return true
    }
}
