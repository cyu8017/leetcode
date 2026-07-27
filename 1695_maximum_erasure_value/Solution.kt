// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

class Solution {
    fun maximumUniqueSubarray(nums: IntArray): Int {
        val seen = HashMap<Int, Int>()
        var left = 0
        var cur = 0
        var best = 0
        for (right in nums.indices) {
            val x = nums[right]
            val prev = seen[x]
            if (prev != null && prev >= left) {
                while (left <= prev) {
                    cur -= nums[left]
                    left++
                }
            }
            seen[x] = right
            cur += x
            best = maxOf(best, cur)
        }
        return best
    }
}
