// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution {
    fun sortedSquares(nums: IntArray): IntArray {
        var n = nums.size
        var ans = IntArray(n)
        var i = 0
        var j = n - 1
        for (k in n - 1 downTo 0) {
            if (kotlin.math.abs(nums[i]) > kotlin.math.abs(nums[j])) {
                ans[k] = nums[i] * nums[i]
                i++
            } else {
                ans[k] = nums[j] * nums[j]
                j--
            }
        }
        return ans
    }
}
