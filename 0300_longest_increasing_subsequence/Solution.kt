// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        val piles = mutableListOf<Int>()
        for (num in nums) {
            var left = 0
            var right = piles.size
            while (left < right) {
                val mid = (left + right) / 2
                if (piles[mid] < num) {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if (left == piles.size) {
                piles.add(num)
            } else {
                piles[left] = num
            }
        }
        return piles.size
    }
}
