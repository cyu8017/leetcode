// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/


class Solution {
    fun arrayNesting(nums: IntArray): Int {
        var best = 0
        for (i in nums.indices) {
            if (nums[i] < 0) continue
            var length = 0
            var j = i
            while (nums[j] >= 0) {
                val nxt = nums[j]
                nums[j] = -1
                j = nxt
                length++
            }
            best = maxOf(best, length)
        }
        return best
    }
}
