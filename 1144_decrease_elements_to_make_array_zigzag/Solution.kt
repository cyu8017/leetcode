// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    fun movesToMakeZigzag(nums: IntArray): Int {
        fun cost(start: Int): Int {
            var ans = 0
            var i = start
            while (i < nums.size) {
                val left = if (i > 0) nums[i - 1] else Int.MAX_VALUE
                val right = if (i + 1 < nums.size) nums[i + 1] else Int.MAX_VALUE
                ans += maxOf(0, nums[i] - minOf(left, right) + 1)
                i += 2
            }
            return ans
        }
        return minOf(cost(0), cost(1))
    }
}
