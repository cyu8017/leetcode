// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

class Solution {
    fun numberOfGoodPartitions(nums: IntArray): Int {
        val mod = 1000000007
        var last = HashMap<Int, Int>()
        for (i in 0 until nums.size) { last[nums[i]] = i }
        var ans = 1
        var end = 0
        for (i in 0 until nums.size) {
            if (last[nums[i]] > end) end = last[nums[i]]
            if (i == end && i != nums.size - 1) ans = (ans * 2L % mod)
        }
        return ans
    }
}
