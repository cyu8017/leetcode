// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/


class Solution {
    fun findUnsortedSubarray(nums: IntArray): Int {
        val n = nums.size
        var left = -1
        var right = -2
        var maxSeen = nums[0]
        var minSeen = nums[n - 1]
        for (i in 0 until n) {
            maxSeen = maxOf(maxSeen, nums[i])
            if (nums[i] < maxSeen) right = i
            val j = n - 1 - i
            minSeen = minOf(minSeen, nums[j])
            if (nums[j] > minSeen) left = j
        }
        return right - left + 1
    }
}
