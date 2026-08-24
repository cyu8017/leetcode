// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

class Solution {
    fun longestSubarray(nums: IntArray, k: Int): Int {
        var cnt = HashMap<Int, Int>()
        var ans = 0
        var cur = 0
        var l = 0
        for (r in 0 until nums.size) {
            if (cnt.merge(nums[r], 1, { a, b -> a + b }) == 2) cur++
            while (cur > k) {
                if (cnt.merge(nums[l], -1, { a, b -> a + b }) == 1) cur--
                l++
            }
            ans = maxOf(ans, r - l + 1)
        }
        return ans
    }
}
