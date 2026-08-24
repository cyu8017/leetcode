// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution {
    fun partitionDisjoint(nums: IntArray): Int {
        val n = nums.size
        val minRight = IntArray(n)
        minRight[n - 1] = nums[n - 1]
        for (i in n - 2 downTo 0) minRight[i] = minOf(nums[i], minRight[i + 1])
        var maxLeft = nums[0]
        for (i in 1 until n) {
            if (maxLeft <= minRight[i]) return i
            maxLeft = maxOf(maxLeft, nums[i])
        }
        return n - 1
    }
}
