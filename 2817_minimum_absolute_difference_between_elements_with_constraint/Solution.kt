// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

import java.util.TreeSet

class Solution {
    fun minAbsoluteDifference(nums: MutableList<Int>, x: Int): Int {
        if (x == 0) {
            var ans0 = Int.MAX_VALUE
            for (i in 1 until nums.size) {
                ans0 = minOf(ans0, kotlin.math.abs(nums[i] - nums[i - 1]))
            }
            return ans0
        }
        var ans = Int.MAX_VALUE
        val arr = TreeSet<Int>()
        for (i in x until nums.size) {
            arr.add(nums[i - x])
            val cur = nums[i]
            val ceil = arr.ceiling(cur)
            if (ceil != null) ans = minOf(ans, ceil - cur)
            val floor = arr.floor(cur)
            if (floor != null) ans = minOf(ans, cur - floor)
        }
        return ans
    }
}
