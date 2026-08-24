// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution {
    fun countBadPairs(nums: IntArray): Long {
        val n = nums.size.toLong()
        val total = n * (n - 1) / 2
        val freq = HashMap<Int, Long>()
        var good = 0L
        for (i in nums.indices) {
            val key = nums[i] - i
            good += freq.getOrDefault(key, 0L)
            freq[key] = freq.getOrDefault(key, 0L) + 1
        }
        return total - good
    }
}
