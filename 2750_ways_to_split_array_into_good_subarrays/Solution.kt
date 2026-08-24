// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
    fun numberOfGoodSubarraySplits(nums: IntArray): Int {
        val MOD = 1_000_000_007
        val ones = ArrayList<Int>()
        for (i in nums.indices) if (nums[i] == 1) ones.add(i)
        if (ones.isEmpty()) return 0
        var ans = 1L
        for (i in 1 until ones.size) {
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        }
        return ans.toInt()
    }
}
