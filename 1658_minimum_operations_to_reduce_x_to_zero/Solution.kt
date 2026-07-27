// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        val target = nums.sum() - x
        if (target < 0) return -1
        var best = -1
        var left = 0
        var cur = 0
        for (right in nums.indices) {
            cur += nums[right]
            while (cur > target) {
                cur -= nums[left]
                left++
            }
            if (cur == target) best = maxOf(best, right - left + 1)
        }
        return if (best < 0) -1 else nums.size - best
    }
}
