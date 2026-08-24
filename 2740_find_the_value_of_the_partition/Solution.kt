// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
    fun findValueOfPartition(nums: IntArray): Int {
        nums.sort()
        var ans = Int.MAX_VALUE
        for (i in 1 until nums.size) ans = minOf(ans, nums[i] - nums[i - 1])
        return ans
    }
}
