// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution {
    fun countPartitions(nums: IntArray): Int {
        var total = 0
        for (x in nums) { total += x }
        var ans = 0
        var left = 0
        for (i in 0 until nums.size - 1) {
            left += nums[i]
            if ((left - (total - left)) % 2 == 0) ans++
        }
        return ans
    }
}
