// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
    fun sumOfSquares(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            if (n % (i + 1) == 0) ans += nums[i] * nums[i]
        }
        return ans
    }
}
