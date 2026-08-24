// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/


class Solution {
    fun maximumTripletValue(nums: IntArray): Long {
        val n = nums.size
        var ans = 0L
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                for (k in j + 1 until n) {
                    val cand = 1L * (nums[i] - nums[j]) * nums[k]
                    if (cand > ans) ans = cand
                }
            }
        }
        return ans
    }
}
