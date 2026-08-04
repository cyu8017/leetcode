// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution {
    fun maxAlternatingSum(nums: IntArray): Long {
        var even = 0L
        var odd = 0L
        for (x in nums) {
            val ne = maxOf(even, odd + x)
            val no = maxOf(odd, even - x)
            even = ne
            odd = no
        }
        return even
    }
}
