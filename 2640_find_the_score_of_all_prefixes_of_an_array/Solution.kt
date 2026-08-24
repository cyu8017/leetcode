// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    fun findPrefixScore(nums: IntArray): LongArray {
        val ans = LongArray(nums.size)
        var mx = 0
        var sum = 0L
        for (i in nums.indices) {
            if (nums[i] > mx) mx = nums[i]
            sum += nums[i] + mx
            ans[i] = sum
        }
        return ans
    }
}
