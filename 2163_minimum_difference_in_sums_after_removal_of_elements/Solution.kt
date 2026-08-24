// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

import java.util.Collections
import java.util.PriorityQueue

class Solution {
    fun minimumDifference(nums: IntArray): Long {
        val n = nums.size / 3
        val left = LongArray(nums.size)
        val right = LongArray(nums.size)
        val hmax = PriorityQueue<Int>(Collections.reverseOrder())
        var sum = 0L
        for (i in 0 until n) {
            hmax.offer(nums[i])
            sum += nums[i]
        }
        left[n - 1] = sum
        for (i in n until 2 * n) {
            hmax.offer(nums[i])
            sum += nums[i]
            sum -= hmax.poll()
            left[i] = sum
        }
        val hmin = PriorityQueue<Int>()
        sum = 0L
        for (i in nums.size - 1 downTo 2 * n) {
            hmin.offer(nums[i])
            sum += nums[i]
        }
        right[2 * n] = sum
        for (i in 2 * n - 1 downTo n) {
            hmin.offer(nums[i])
            sum += nums[i]
            sum -= hmin.poll()
            right[i] = sum
        }
        var ans = left[n - 1] - right[n]
        for (i in n until 2 * n) ans = minOf(ans, left[i] - right[i + 1])
        return ans
    }
}
