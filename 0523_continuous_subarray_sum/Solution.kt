// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

class Solution {
    fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
        val remainders = mutableMapOf(0 to -1)
        var prefix = 0
        for ((index, num) in nums.withIndex()) {
            prefix += num
            val mod = if (k != 0) prefix % k else prefix
            val previous = remainders[mod]
            if (previous != null) {
                if (index - previous >= 2) {
                    return true
                }
            } else {
                remainders[mod] = index
            }
        }
        return false
    }
}
