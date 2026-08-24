// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution {
    fun maxSubsequence(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val arr = Array(n) { intArrayOf(nums[it], it) }
        arr.sortWith(compareByDescending { it[0] })
        val idx = IntArray(k) { arr[it][1] }
        idx.sort()
        return IntArray(k) { nums[idx[it]] }
    }
}
