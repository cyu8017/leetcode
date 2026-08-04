// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

class Solution {
    fun maxSumRangeQuery(nums: IntArray, requests: Array<IntArray>): Int {
        val mod = 1_000_000_007
        val diff = IntArray(nums.size + 1)
        for (r in requests) {
            diff[r[0]]++
            diff[r[1] + 1]--
        }
        for (i in 1 until nums.size) diff[i] += diff[i - 1]
        val freq = diff.copyOf(nums.size)
        nums.sort()
        freq.sort()
        var ans = 0L
        for (i in nums.indices) {
            ans = (ans + 1L * nums[i] * freq[i]) % mod
        }
        return ans.toInt()
    }
}
